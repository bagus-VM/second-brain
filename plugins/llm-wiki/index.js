/**
 * LLM Wiki: a Karpathy-style interlinked markdown knowledge base for DeepSeek Harness.
 *
 * The plugin contributes two things:
 *  - the `llm-wiki` skill, which carries the conventions the agent must follow;
 *  - four deterministic tools for the mechanical parts of that workflow, so the model
 *    does not have to re-author a scanner each session: orientation, linting, source
 *    ingestion with body hashing, and log appends.
 *
 * No dependencies: everything here is plain JavaScript over Node built-ins.
 */

import { createHash } from 'node:crypto'
import { existsSync, readFileSync } from 'node:fs'
import { mkdir, readdir, readFile, stat, writeFile } from 'node:fs/promises'
import { homedir } from 'node:os'
import { dirname, isAbsolute, join } from 'node:path'
import { fileURLToPath } from 'node:url'

const SKILL_NAME = 'llm-wiki'

/** The skill ships in titstack's layout: <name>/SKILL.md alongside agents/ and references/. */
const BUNDLED_SKILL_DIR = fileURLToPath(new URL('./skills/llm-wiki/', import.meta.url))

const SKILL_FALLBACK_DESCRIPTION =
  "Karpathy's LLM Wiki: build and maintain a persistent, compounding knowledge base as interlinked markdown pages, with ingest, query, and lint workflows over a raw-sources-plus-pages vault."

const DEFAULTS = {
  wikiPath: '',
  registerSkill: true,
  skillFile: '',
  schemaFile: 'SCHEMA.md',
  indexFile: 'index.md',
  logFile: 'log.md',
  rawDir: 'raw',
  archiveDir: '_archive',
  maxPageLines: 200,
  staleDays: 90,
  logRotateEntries: 500,
  excludeDirs: [],
}

/** Directories that never hold wiki pages. */
const SKIP_DIRS = new Set([
  '.git', '.obsidian', '.kilo', '.vscode', '.github', '.dsh', '.pytest_cache',
  '__pycache__', 'node_modules', '.venv', 'venv', 'env', 'dist', 'build', 'target',
  'raw', '_archive', 'assets', '.cache', '.next', '.trash',
])

const RAW_KINDS = {
  article: 'articles',
  paper: 'papers',
  transcript: 'transcripts',
  note: 'notes',
  other: 'notes',
}

// ---------------------------------------------------------------------------
// small utilities
// ---------------------------------------------------------------------------

function configOf(config) {
  return { ...DEFAULTS, ...(config ?? {}) }
}

function expandHome(value) {
  if (typeof value !== 'string' || value.length === 0) return value
  if (value === '~') return homedir()
  if (value.startsWith('~/') || value.startsWith('~\\')) return join(homedir(), value.slice(2))
  return isAbsolute(value) ? value : value
}

function today() {
  const now = new Date()
  const pad = (n) => String(n).padStart(2, '0')
  return `${now.getFullYear()}-${pad(now.getMonth() + 1)}-${pad(now.getDate())}`
}

/**
 * Read a titstack-style skill document: YAML frontmatter, then the instruction body.
 * Only the `name` and `description` scalars are needed, so no YAML parser is involved.
 */
function parseSkillDocument(text) {
  const match = /^---\r?\n([\s\S]*?)\r?\n---[ \t]*\r?\n?/.exec(text)
  if (match === null) return { data: {}, body: text }
  const data = {}
  for (const line of match[1].split(/\r?\n/)) {
    if (/^\s/.test(line)) continue
    const colon = line.indexOf(':')
    if (colon <= 0) continue
    data[line.slice(0, colon).trim()] = line
      .slice(colon + 1)
      .trim()
      .replace(/^["']/, '')
      .replace(/["']$/, '')
  }
  return { data, body: text.slice(match[0].length) }
}

/**
 * Resolution order for the skill body, so an installed titstack copy wins over the
 * bundled one and edits there take effect on the next activation:
 *   explicit `skillFile`, `$AGENTS_HOME/skills`, `~/.agents/skills`, bundled.
 */
function skillCandidates(config) {
  const files = []
  if (typeof config.skillFile === 'string' && config.skillFile.trim().length > 0) {
    files.push(expandHome(config.skillFile.trim()))
  }
  const agentsHome = process.env.AGENTS_HOME
  if (typeof agentsHome === 'string' && agentsHome.trim().length > 0) {
    files.push(join(agentsHome.trim(), 'skills', SKILL_NAME, 'SKILL.md'))
  }
  files.push(join(homedir(), '.agents', 'skills', SKILL_NAME, 'SKILL.md'))
  files.push(join(BUNDLED_SKILL_DIR, 'SKILL.md'))
  return files
}

function loadSkill(config) {
  for (const file of skillCandidates(config)) {
    if (!existsSync(file)) continue
    try {
      const parsed = parseSkillDocument(readFileSync(file, 'utf8'))
      if (parsed.body.trim().length === 0) continue
      return { file, dir: dirname(file), data: parsed.data, body: parsed.body }
    } catch {
      /* unreadable candidate: try the next one */
    }
  }
  return {
    file: null,
    dir: BUNDLED_SKILL_DIR,
    data: {},
    body: '# LLM Wiki\n\nThe skill body is missing. Reinstall the @local/dsh-llm-wiki bundle.\n',
  }
}

function sha256(text) {
  return createHash('sha256').update(text, 'utf8').digest('hex')
}

function posix(rel) {
  return rel.split('\\').join('/')
}

function slugify(title) {
  const slug = String(title)
    .toLowerCase()
    .normalize('NFKD')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
  return slug.length > 0 ? slug.slice(0, 96) : 'untitled'
}

async function exists(path) {
  try {
    await stat(path)
    return true
  } catch {
    return false
  }
}

async function mapLimit(items, limit, fn) {
  const out = new Array(items.length)
  let next = 0
  const workers = Array.from({ length: Math.min(limit, items.length) }, async () => {
    while (true) {
      const index = next++
      if (index >= items.length) return
      out[index] = await fn(items[index], index)
    }
  })
  await Promise.all(workers)
  return out
}

function clip(text, max) {
  if (typeof text !== 'string') return ''
  return text.length <= max ? text : `${text.slice(0, max - 1)}…`
}

// ---------------------------------------------------------------------------
// markdown parsing
// ---------------------------------------------------------------------------

const FRONTMATTER = /^---\r?\n([\s\S]*?)\r?\n---[ \t]*\r?\n?/

function parseScalar(raw) {
  const value = raw.trim()
  if (value.length === 0) return ''
  if (value.startsWith('[')) {
    const inner = value.replace(/^\[/, '').replace(/\]$/, '').trim()
    if (inner.length === 0) return []
    return inner.split(',').map((part) => unquote(part.trim())).filter((part) => part.length > 0)
  }
  if (value === 'true') return true
  if (value === 'false') return false
  return unquote(value)
}

function unquote(value) {
  if (value.length >= 2 && ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'")))) {
    return value.slice(1, -1)
  }
  return value
}

function parseFrontmatter(text) {
  const match = FRONTMATTER.exec(text)
  if (match === null) return { data: null, body: text }
  const data = {}
  for (const line of match[1].split(/\r?\n/)) {
    if (line.trim().length === 0 || /^\s/.test(line)) continue
    const colon = line.indexOf(':')
    if (colon <= 0) continue
    const key = line.slice(0, colon).trim()
    data[key] = parseScalar(line.slice(colon + 1))
  }
  return { data, body: text.slice(match[0].length) }
}

function asList(value) {
  if (Array.isArray(value)) return value.map((item) => String(item))
  if (typeof value === 'string' && value.length > 0) return [value]
  return []
}

/** Every `[[target]]` / `[[target|label]]` / `[[target#heading]]` target in a body. */
function wikilinks(text) {
  const out = []
  const pattern = /\[\[([^\]\n]+?)\]\]/g
  let match
  while ((match = pattern.exec(text)) !== null) {
    const before = match.index > 0 ? text[match.index - 1] : ''
    const raw = match[1]
    const target = raw.split('|')[0].split('#')[0].trim()
    if (target.length === 0) continue
    if (/^(https?:|mailto:)/i.test(target)) continue
    out.push({ target, embedded: before === '!' })
  }
  return out
}

function linkKey(target) {
  return posix(target).replace(/\.md$/i, '').replace(/^\/+/, '').toLowerCase()
}

function baseKey(target) {
  const normalized = linkKey(target)
  const slash = normalized.lastIndexOf('/')
  return slash === -1 ? normalized : normalized.slice(slash + 1)
}

// ---------------------------------------------------------------------------
// filesystem walking
// ---------------------------------------------------------------------------

async function walkMarkdown(dir, options = {}, rel = '') {
  const { skip = new Set(), skipRoots = new Set(), depth = 8 } = options
  const found = []
  if (depth < 0) return found
  let entries
  try {
    entries = await readdir(dir, { withFileTypes: true })
  } catch {
    return found
  }
  for (const entry of entries) {
    const name = entry.name
    const childRel = rel.length === 0 ? name : `${rel}/${name}`
    if (entry.isDirectory()) {
      const key = name.toLowerCase()
      if (rel.length === 0 && skipRoots.has(key)) continue
      if (skip.has(key)) continue
      found.push(...(await walkMarkdown(join(dir, name), { ...options, depth: depth - 1 }, childRel)))
      continue
    }
    if (entry.isFile() && /\.md$/i.test(name)) found.push(childRel)
  }
  return found
}

async function looksLikeWiki(dir) {
  if (!(await exists(dir))) return false
  for (const name of ['index.md', 'log.md', 'SCHEMA.md']) {
    if (await exists(join(dir, name))) return true
  }
  return false
}

async function detectRoot(ctx, config, explicit) {
  if (typeof explicit === 'string' && explicit.trim().length > 0) return expandHome(explicit.trim())
  if (typeof config.wikiPath === 'string' && config.wikiPath.trim().length > 0) return expandHome(config.wikiPath.trim())
  const fromEnv = process.env.WIKI_PATH
  if (typeof fromEnv === 'string' && fromEnv.trim().length > 0) return expandHome(fromEnv.trim())

  const bases = []
  try {
    const working = ctx.get('workingDirectory')
    if (working && typeof working.defaultDirectory === 'string') bases.push(working.defaultDirectory)
  } catch {
    /* service absent */
  }
  bases.push(process.cwd())
  for (const base of new Set(bases)) {
    for (const name of ['second-brain', 'wiki']) {
      const candidate = join(base, name)
      if (await looksLikeWiki(candidate)) return candidate
    }
  }
  return join(homedir(), 'wiki')
}

async function readIfPresent(path) {
  try {
    return await readFile(path, 'utf8')
  } catch {
    return null
  }
}

// ---------------------------------------------------------------------------
// orientation
// ---------------------------------------------------------------------------

async function orient(ctx, config, args) {
  const root = await detectRoot(ctx, config, args?.wikiPath)
  const lines = []
  const present = await exists(root)
  lines.push(`Wiki root: ${root}`)
  if (!present) {
    lines.push('Status: NOT FOUND')
    lines.push('')
    lines.push('No wiki exists at that path. To initialize one: create raw/{articles,papers,transcripts,assets},')
    lines.push('entities/, concepts/, comparisons/, queries/, then write SCHEMA.md, index.md, and log.md.')
    lines.push('Pass `wikiPath` explicitly if the wiki lives somewhere else.')
    return lines.join('\n')
  }

  const [schema, index, log] = await Promise.all([
    readIfPresent(join(root, config.schemaFile)),
    readIfPresent(join(root, config.indexFile)),
    readIfPresent(join(root, config.logFile)),
  ])

  lines.push('Status: found')
  lines.push(`Backbone: ${config.schemaFile} ${schema === null ? 'MISSING' : 'ok'} | ${config.indexFile} ${index === null ? 'MISSING' : 'ok'} | ${config.logFile} ${log === null ? 'MISSING' : 'ok'}`)

  const skip = new Set([...SKIP_DIRS, ...config.excludeDirs.map((name) => String(name).toLowerCase())])
  const pages = await walkMarkdown(root, { skip })
  const byTop = new Map()
  for (const page of pages) {
    const slash = page.indexOf('/')
    const top = slash === -1 ? '(root)' : page.slice(0, slash)
    byTop.set(top, (byTop.get(top) ?? 0) + 1)
  }
  lines.push(`Pages: ${pages.length} markdown file(s) outside ${config.rawDir}/`)
  const groups = [...byTop.entries()].sort((a, b) => b[1] - a[1])
  if (groups.length > 0) {
    lines.push(`Top-level spread: ${groups.map(([name, count]) => `${name} (${count})`).join(', ')}`)
  }

  if (schema !== null) {
    const domain = /^##\s+Domain\s*$([\s\S]*?)(?=^##\s)/m.exec(schema)
    const summary = domain === null ? clip(schema.replace(/\r/g, '').trim(), 320) : clip(domain[1].trim(), 320)
    lines.push('')
    lines.push('Schema domain:')
    for (const line of summary.split('\n').filter((entry) => entry.trim().length > 0).slice(0, 8)) {
      lines.push(`  ${line.trim()}`)
    }
  } else {
    lines.push('')
    lines.push(`No ${config.schemaFile}: conventions, frontmatter, and the tag taxonomy are undefined.`)
  }

  if (index !== null) {
    // Index headers are prose ("**Total pages:** 856 (vault + study)"), so pull the
    // number and the date out instead of echoing the whole decorated line.
    const total = /total pages\s*[:：]\s*([^\n|]+)/i.exec(index)
    const updated = /last updated\s*[:：]\s*([^\n|]+)/i.exec(index)
    const totalPages = total === null ? null : /(\d[\d,]*)/.exec(total[1])?.[1] ?? null
    const lastUpdated = updated === null
      ? null
      : /(\d{4}-\d{2}-\d{2})/.exec(updated[1])?.[1] ?? updated[1].replace(/[*_`]/g, '').trim()
    lines.push('')
    lines.push(`Index: ${index.split('\n').length} lines${totalPages === null ? '' : `, claims ${totalPages} pages`}${lastUpdated === null ? '' : `, last updated ${lastUpdated}`}`)
    const headings = index.split(/\r?\n/).filter((line) => /^##\s+/.test(line)).map((line) => line.replace(/^##\s+/, '').trim())
    if (headings.length > 0) lines.push(`Sections: ${headings.join(', ')}`)
  }

  if (log !== null) {
    const entries = log.split(/\r?\n/).filter((line) => /^##\s+\[/.test(line))
    const wanted = Math.max(1, Math.min(Number(args?.logLines ?? 12) || 12, 50))
    lines.push('')
    lines.push(`Log: ${entries.length} entries${entries.length > config.logRotateEntries ? ` (over ${config.logRotateEntries}: rotate to log-YYYY.md)` : ''}`)
    if (entries.length > 0) {
      lines.push(`Recent activity:`)
      for (const entry of entries.slice(-wanted)) lines.push(`  ${entry.replace(/^##\s+/, '').trim()}`)
    }
  }

  lines.push('')
  lines.push('Next: read the pages this work touches before writing. Never modify raw/. Update index and log afterwards.')
  return lines.join('\n')
}

// ---------------------------------------------------------------------------
// lint
// ---------------------------------------------------------------------------

function taxonomyOf(schema) {
  if (schema === null) return null
  const section = /^##\s+Tag Taxonomy\s*$([\s\S]*?)(?=^##\s|\Z)/im.exec(schema)
  if (section === null) return null
  const stop = new Set([
    'the', 'and', 'for', 'with', 'from', 'add', 'new', 'tag', 'tags', 'top', 'level', 'example',
    'rule', 'every', 'page', 'must', 'appear', 'here', 'before', 'using', 'this', 'that', 'they',
    'use', 'domains', 'domain', 'define', 'only', 'first', 'then', 'not', 'are', 'its', 'can',
    'models', 'people', 'orgs', 'techniques', 'meta', 'comparison', 'timeline', 'controversy',
    'prediction', 'model', 'architecture', 'benchmark', 'training', 'person', 'company', 'lab',
    'open', 'source', 'optimization', 'fine', 'tuning', 'inference', 'alignment', 'data',
  ])
  const tags = new Set()
  for (const token of section[1].toLowerCase().match(/[a-z][a-z0-9-]{2,}/g) ?? []) {
    if (!stop.has(token)) tags.add(token)
  }
  return tags.size >= 5 ? tags : null
}

async function lint(ctx, config, args) {
  const root = await detectRoot(ctx, config, args?.wikiPath)
  if (!(await exists(root))) {
    return `No wiki at ${root}. Run wiki_orient with a correct wikiPath, or initialize a wiki first.`
  }

  const sample = Math.max(1, Math.min(Number(args?.limit ?? 25) || 25, 100))
  const staleDays = Number(args?.staleDays ?? config.staleDays) || config.staleDays
  const maxLines = Number(args?.maxPageLines ?? config.maxPageLines) || config.maxPageLines
  const checkHashes = args?.checkSourceHashes !== false

  const skip = new Set([...SKIP_DIRS, ...config.excludeDirs.map((name) => String(name).toLowerCase())])
  const relPaths = await walkMarkdown(root, { skip })
  const schema = await readIfPresent(join(root, config.schemaFile))
  const indexText = await readIfPresent(join(root, config.indexFile))
  const logText = await readIfPresent(join(root, config.logFile))
  const taxonomy = taxonomyOf(schema)

  const pages = await mapLimit(relPaths, 32, async (rel) => {
    const path = join(root, rel)
    let text = ''
    try {
      text = await readFile(path, 'utf8')
    } catch {
      return null
    }
    const parsed = parseFrontmatter(text)
    return {
      rel,
      text,
      data: parsed.data,
      body: parsed.body,
      links: wikilinks(parsed.body),
      lines: text.split(/\r?\n/).length,
    }
  })
  const present = pages.filter((page) => page !== null)

  // name resolution: Obsidian resolves a wikilink by basename or by vault-relative path.
  const byName = new Map()
  for (const page of present) {
    const rel = linkKey(page.rel)
    const base = baseKey(page.rel)
    if (!byName.has(base)) byName.set(base, [])
    byName.get(base).push(page.rel)
    if (!byName.has(rel)) byName.set(rel, [])
    byName.get(rel).push(page.rel)
  }

  const inbound = new Map()
  const broken = []
  const ambiguous = []
  for (const page of present) {
    for (const link of page.links) {
      const key = linkKey(link.target)
      const matches = byName.get(key)
      if (matches === undefined || matches.length === 0) {
        broken.push({ from: page.rel, target: link.target })
        continue
      }
      if (matches.length > 1) ambiguous.push({ from: page.rel, target: link.target, matches: matches.length })
      for (const target of matches) {
        if (target === page.rel) continue
        if (!inbound.has(target)) inbound.set(target, new Set())
        inbound.get(target).add(page.rel)
      }
    }
  }

  const orphans = present.filter((page) => !inbound.has(page.rel)).map((page) => page.rel)

  const indexLower = (indexText ?? '').toLowerCase()
  const indexLinks = new Set(wikilinks(indexText ?? '').map((link) => linkKey(link.target)))
  const indexGaps = indexText === null
    ? []
    : present.filter((page) => {
      const base = baseKey(page.rel)
      return !indexLinks.has(base) && !indexLinks.has(linkKey(page.rel)) && !indexLower.includes(base)
    }).map((page) => page.rel)

  const missingFields = []
  const badTags = []
  const contested = []
  const oversized = []
  const stale = []
  const now = Date.now()
  const staleMs = staleDays * 86_400_000

  for (const page of present) {
    if (page.lines > maxLines) oversized.push({ rel: page.rel, lines: page.lines })

    if (page.data === null) {
      if (config.requireFrontmatter === true) missingFields.push({ rel: page.rel, missing: ['frontmatter'] })
      continue
    }
    const missing = ['title', 'created', 'updated', 'type', 'tags', 'sources'].filter((field) => page.data[field] === undefined || page.data[field] === '')
    if (missing.length > 0) missingFields.push({ rel: page.rel, missing })

    if (taxonomy !== null) {
      const unknown = asList(page.data.tags).map((tag) => tag.toLowerCase()).filter((tag) => !taxonomy.has(tag))
      if (unknown.length > 0) badTags.push({ rel: page.rel, tags: unknown })
    }

    const confidence = typeof page.data.confidence === 'string' ? page.data.confidence.toLowerCase() : ''
    const conflicts = asList(page.data.contradictions)
    if (page.data.contested === true || conflicts.length > 0 || confidence === 'low') {
      contested.push({
        rel: page.rel,
        reason: page.data.contested === true ? 'contested' : conflicts.length > 0 ? 'contradictions' : 'confidence: low',
      })
    }

    const updated = typeof page.data.updated === 'string' ? Date.parse(page.data.updated) : Number.NaN
    if (Number.isFinite(updated) && now - updated > staleMs) {
      stale.push({ rel: page.rel, updated: page.data.updated })
    }
  }

  const drift = []
  if (checkHashes) {
    const rawRoot = join(root, config.rawDir)
    if (await exists(rawRoot)) {
      const rawFiles = await walkMarkdown(rawRoot, { skip })
      await mapLimit(rawFiles, 24, async (rel) => {
        const path = join(rawRoot, rel)
        let text = ''
        try {
          text = await readFile(path, 'utf8')
        } catch {
          return
        }
        const parsed = parseFrontmatter(text)
        const stored = parsed.data?.sha256
        if (typeof stored !== 'string' || stored.length === 0) return
        const actual = sha256(parsed.body)
        if (actual !== stored) drift.push({ rel: `${config.rawDir}/${rel}`, stored: stored.slice(0, 12), actual: actual.slice(0, 12) })
      })
    }
  }

  const logEntries = logText === null ? 0 : logText.split(/\r?\n/).filter((line) => /^##\s+\[/.test(line)).length

  const blocks = []
  const section = (title, items, format, hint) => {
    blocks.push('')
    blocks.push(`${title}: ${items.length}`)
    for (const item of items.slice(0, sample)) blocks.push(`  - ${format(item)}`)
    if (items.length > sample) blocks.push(`  - … ${items.length - sample} more (raise limit to see more)`)
    if (items.length > 0 && hint) blocks.push(`  → ${hint}`)
  }

  const header = [
    `Wiki lint: ${root}`,
    `${present.length} page(s) scanned${indexText === null ? ', index MISSING' : ''}${schema === null ? `, ${config.schemaFile} MISSING (tag audit skipped)` : ''}${taxonomy === null && schema !== null ? ', tag taxonomy not detected (tag audit skipped)' : ''}`,
  ]

  section('Broken wikilinks', broken, (item) => `${item.from} → [[${item.target}]]`, 'Fix these first: they are dead references.')
  section('Orphan pages (no inbound links)', orphans, (item) => item, 'Link each page from at least one other page, or archive it.')
  section('Missing from index.md', indexGaps, (item) => item, 'Add each page to the index under its section.')
  section('Raw source drift', drift, (item) => `${item.rel} (stored ${item.stored}…, actual ${item.actual}…)`, 'Raw files are immutable; confirm with the user before re-ingesting.')
  section('Contested or low-confidence pages', contested, (item) => `${item.rel} (${item.reason})`, 'Review these before quoting them as settled fact.')
  section('Stale pages', stale, (item) => `${item.rel} (updated ${item.updated})`, `No update within ${staleDays} days.`)
  section('Oversized pages', oversized, (item) => `${item.rel} (${item.lines} lines)`, `Past ${maxLines} lines: split into sub-topics.`)
  section('Tags outside the taxonomy', badTags, (item) => `${item.rel} (${item.tags.join(', ')})`, `Add new tags to ${config.schemaFile} first.`)
  section('Frontmatter gaps', missingFields, (item) => `${item.rel} (missing ${item.missing.join(', ')})`, 'Frontmatter drives filtering and staleness checks.')

  const total = broken.length + orphans.length + indexGaps.length + drift.length + contested.length + stale.length + oversized.length + badTags.length + missingFields.length
  const out = [...header]
  if (total === 0) {
    out.push('', 'No findings. The wiki is consistent.')
  } else {
    out.push('')
    out.push(`Findings: ${total} across ${present.length} page(s). Severity order: broken links > orphans > index gaps > source drift > contested > stale > oversized > tags > frontmatter.`)
    out.push(...blocks)
  }
  out.push('')
  out.push(`Log: ${logEntries} entries${logEntries > config.logRotateEntries ? ` (over ${config.logRotateEntries}: rotate to log-YYYY.md)` : ''}.`)
  if (total > 0) out.push('Append one summary entry with wiki_log when you finish acting on these findings.')
  if (ambiguous.length > 0) out.push(`Note: ${ambiguous.length} wikilink(s) resolve to more than one page by basename.`)
  return out.join('\n')
}

// ---------------------------------------------------------------------------
// ingest
// ---------------------------------------------------------------------------

async function ingest(ctx, config, args) {
  const title = typeof args?.title === 'string' ? args.title.trim() : ''
  if (title.length === 0) return 'wiki_ingest needs a title describing the source.'

  const root = await detectRoot(ctx, config, args?.wikiPath)
  const kind = typeof args?.kind === 'string' && RAW_KINDS[args.kind] !== undefined ? args.kind : 'article'
  const subdir = RAW_KINDS[kind]

  let body = typeof args?.content === 'string' ? args.content : ''
  if (body.length === 0 && typeof args?.sourceFile === 'string' && args.sourceFile.trim().length > 0) {
    const sourcePath = expandHome(args.sourceFile.trim())
    try {
      body = await readFile(isAbsolute(sourcePath) ? sourcePath : join(process.cwd(), sourcePath), 'utf8')
    } catch (error) {
      return `Could not read sourceFile "${args.sourceFile}": ${error?.message ?? error}. Extract the text first (web_fetch for URLs, read for files) and pass it as content.`
    }
  }
  if (body.trim().length === 0) {
    return 'wiki_ingest needs the source text: pass `content`, or `sourceFile` pointing at a UTF-8 text file.'
  }

  const hashed = sha256(body)
  const rel = `${config.rawDir}/${subdir}/${slugify(title)}.md`
  const path = join(root, rel)
  const frontmatter = [
    '---',
    `title: ${title.replace(/\r?\n/g, ' ')}`,
    ...(typeof args?.sourceUrl === 'string' && args.sourceUrl.trim().length > 0 ? [`source_url: ${args.sourceUrl.trim()}`] : []),
    `ingested: ${today()}`,
    `sha256: ${hashed}`,
    '---',
    '',
  ].join('\n')
  const document = `${frontmatter}${body}`

  const previous = await readIfPresent(path)
  if (previous !== null) {
    const stored = parseFrontmatter(previous).data?.sha256
    if (typeof stored === 'string' && stored === hashed) {
      return [
        `Status: unchanged`,
        `Raw source: ${rel}`,
        `sha256: ${hashed}`,
        '',
        'The stored copy still matches this content. Nothing was written; skip re-processing it and continue with the takeaways.',
      ].join('\n')
    }
    if (args?.force !== true) {
      return [
        `Status: drift`,
        `Raw source: ${rel}`,
        `stored sha256: ${typeof stored === 'string' ? stored : '(none)'}`,
        `incoming sha256: ${hashed}`,
        '',
        'The source changed since it was last ingested (or was ingested without a hash). raw/ is immutable, so nothing was written.',
        'Tell the user both hashes and ask whether the new version supersedes the old one; re-run with force: true only after they agree.',
      ].join('\n')
    }
  }

  if (args?.dryRun === true) {
    return [
      `Status: dry-run (${previous === null ? 'would create' : 'would replace'})`,
      `Raw source: ${rel}`,
      `sha256: ${hashed}`,
      `bytes: ${Buffer.byteLength(document, 'utf8')}`,
      '',
      'Nothing was written. Re-run without dryRun to store it.',
    ].join('\n')
  }

  await mkdir(dirname(path), { recursive: true })
  await writeFile(path, document, 'utf8')

  const status = previous === null ? 'created' : 'replaced'
  return [
    `Status: ${status}`,
    `Raw source: ${rel}`,
    `sha256: ${hashed}`,
    `bytes: ${Buffer.byteLength(document, 'utf8')}`,
    '',
    'Next: check index.md and grep the wiki for the entities and concepts this source mentions,',
    'then create or update pages above the schema thresholds, cross-link them, update index.md,',
    'and append one entry with wiki_log.',
  ].join('\n')
}

// ---------------------------------------------------------------------------
// log
// ---------------------------------------------------------------------------

async function appendLog(ctx, config, args) {
  const root = await detectRoot(ctx, config, args?.wikiPath)
  if (!(await exists(root))) return `No wiki at ${root}. Check wikiPath.`

  const action = typeof args?.action === 'string' && args.action.trim().length > 0 ? args.action.trim() : 'update'
  const subject = typeof args?.subject === 'string' ? args.subject.trim() : ''
  if (subject.length === 0) return 'wiki_log needs a subject: the source title, page, or query being recorded.'

  const files = asList(args?.files).map((file) => file.trim()).filter((file) => file.length > 0)
  const notes = typeof args?.notes === 'string' ? args.notes.trim() : ''
  const date = typeof args?.date === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(args.date.trim()) ? args.date.trim() : today()
  const path = join(root, config.logFile)

  let text = await readIfPresent(path)
  let created = false
  if (text === null) {
    text = `# Wiki Log\n\n> Chronological record of all wiki actions. Append-only.\n> Format: \`## [YYYY-MM-DD] action | subject\`\n\n`
    created = true
  }

  const entry = [
    `## [${date}] ${action} | ${subject}`,
    ...files.map((file) => `- ${file}`),
    ...(notes.length > 0 ? [`- ${notes}`] : []),
    '',
  ].join('\n')
  const separator = text.endsWith('\n\n') ? '' : text.endsWith('\n') ? '\n' : '\n\n'
  const next = `${text}${separator}${entry}`

  await mkdir(dirname(path), { recursive: true })
  await writeFile(path, next, 'utf8')

  const entries = next.split(/\r?\n/).filter((line) => /^##\s+\[/.test(line)).length
  const warning = entries > config.logRotateEntries
    ? `\nWarning: ${entries} entries exceeds ${config.logRotateEntries}. Rotate now: rename ${config.logFile} to log-${new Date().getFullYear()}.md and start a fresh log.`
    : ''

  return [
    `${created ? 'Created' : 'Appended to'} ${config.logFile}: ${entries} entries.`,
    `## [${date}] ${action} | ${subject}`,
    ...files.map((file) => `  - ${file}`),
    ...(notes.length > 0 ? [`  - ${notes}`] : []),
    warning,
  ].filter((line) => line.length > 0).join('\n')
}

// ---------------------------------------------------------------------------
// tool plumbing
// ---------------------------------------------------------------------------

/** Every tool returns one text block; the model reads the report, not a JSON tree. */
function textTool(name, description, parameters, run, concurrencySafe = false) {
  return {
    name,
    description,
    parameters,
    ...(concurrencySafe ? { isConcurrencySafe: () => true } : {}),
    output: {
      schema: {
        type: 'object',
        properties: { text: { type: 'string' } },
        required: ['text'],
        additionalProperties: false,
      },
      render(_args, value) {
        return [{ type: 'text', text: typeof value?.text === 'string' ? value.text : '' }]
      },
    },
    async execute(args, exec) {
      return { text: await run(args ?? {}, exec) }
    },
  }
}

const WIKI_PATH_PARAM = {
  type: 'string',
  description: 'Absolute wiki root. Omit to use the configured or detected wiki.',
}

const TOOL_DEFINITIONS = (config, ctx) => [
  textTool(
    'wiki_orient',
    'Orient in a markdown LLM wiki before working in it: reads SCHEMA.md, index.md, and the recent log, then reports page counts per top-level directory and any missing backbone file. Call this first in a session and again before an ingest or query on an unfamiliar wiki.',
    {
      type: 'object',
      properties: {
        wikiPath: WIKI_PATH_PARAM,
        logLines: { type: 'integer', description: 'How many recent log entries to show (1-50, default 12).' },
      },
      additionalProperties: false,
    },
    (args) => orient(ctx, config, args),
    true,
  ),
  textTool(
    'wiki_lint',
    'Audit a markdown LLM wiki for consistency: broken [[wikilinks]], orphan pages, pages missing from index.md, raw-source hash drift, contested or low-confidence pages, stale pages, oversized pages, tags outside the schema taxonomy, frontmatter gaps, and log rotation. Read-only; returns findings grouped by severity with paths.',
    {
      type: 'object',
      properties: {
        wikiPath: WIKI_PATH_PARAM,
        checkSourceHashes: { type: 'boolean', description: 'Recompute sha256 for raw/ sources (default true).' },
        staleDays: { type: 'integer', description: 'Age in days before a page counts as stale (default 90).' },
        maxPageLines: { type: 'integer', description: 'Line count that makes a page a split candidate (default 200).' },
        limit: { type: 'integer', description: 'Samples listed per category (1-100, default 25).' },
      },
      additionalProperties: false,
    },
    (args) => lint(ctx, config, args),
    true,
  ),
  textTool(
    'wiki_ingest',
    'Store one source in a markdown LLM wiki under raw/, with source_url, ingested date, and a sha256 of the body only. Reports created / unchanged / drift so a re-ingest of the same source is skipped when identical and never silently overwrites an immutable raw file. Pass the extracted text as content, or a UTF-8 text file as sourceFile.',
    {
      type: 'object',
      properties: {
        title: { type: 'string', description: 'Descriptive source title; becomes the raw file name.' },
        content: { type: 'string', description: 'The source text to store.' },
        sourceFile: { type: 'string', description: 'Path to a UTF-8 text file to read instead of content.' },
        sourceUrl: { type: 'string', description: 'Original URL, recorded in frontmatter.' },
        kind: { type: 'string', enum: ['article', 'paper', 'transcript', 'note', 'other'], description: 'Selects the raw/ subdirectory (default article).' },
        wikiPath: WIKI_PATH_PARAM,
        force: { type: 'boolean', description: 'Replace a raw file whose hash drifted. Only after the user agrees.' },
        dryRun: { type: 'boolean', description: 'Report what would be written without writing it.' },
      },
      required: ['title'],
      additionalProperties: false,
    },
    (args) => ingest(ctx, config, args),
  ),
  textTool(
    'wiki_log',
    'Append one entry to a markdown LLM wiki log.md: `## [YYYY-MM-DD] action | subject` plus the files touched. Use after every ingest, update, query, lint, create, archive, or delete, so the log stays a complete chronological record.',
    {
      type: 'object',
      properties: {
        action: { type: 'string', description: 'ingest, update, query, lint, create, archive, or delete.' },
        subject: { type: 'string', description: 'What the entry is about: source title, page, or query.' },
        files: { type: 'array', items: { type: 'string' }, description: 'Files created or updated by this action.' },
        notes: { type: 'string', description: 'One extra line of context, such as an issue count.' },
        wikiPath: WIKI_PATH_PARAM,
        date: { type: 'string', description: 'YYYY-MM-DD override; defaults to today.' },
      },
      required: ['action', 'subject'],
      additionalProperties: false,
    },
    (args) => appendLog(ctx, config, args),
  ),
]

export const name = 'llm-wiki'
export const inject = ['tools', 'skills']

export function apply(ctx, config) {
  const resolved = configOf(config)

  if (resolved.registerSkill !== false) {
    const skill = loadSkill(resolved)
    ctx.effect(() => ctx.skills.register({
      name: SKILL_NAME,
      description: typeof skill.data.description === 'string' && skill.data.description.length > 0
        ? skill.data.description
        : SKILL_FALLBACK_DESCRIPTION,
      whenToUse: 'Use for creating, ingesting into, querying, or linting a markdown wiki, knowledge base, second brain, or Obsidian vault.',
      source: 'custom',
      resourceBase: { kind: 'directory', path: skill.dir },
      metadata: {
        version: '1.0.0',
        category: 'research',
        tags: ['wiki', 'knowledge-base', 'markdown', 'notes'],
        skillFile: skill.file ?? 'bundled',
      },
      content: skill.body,
    }))
  }

  for (const tool of TOOL_DEFINITIONS(resolved, ctx)) {
    ctx.effect(() => ctx.tools.register(tool))
  }
}
