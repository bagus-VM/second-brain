# Bali Budget Dashboard

A free, self-hosted flight search dashboard for a trip to Bali. Lives on GitHub Pages. Prices come from the Kiwi.com Tequila API via a Cloudflare Worker so your API key never touches the browser.

## What's inside

```
bali-budget/
├── docs/
│   └── index.html          # GitHub Pages dashboard
├── worker/
│   ├── src/index.js        # Cloudflare Worker proxy
│   ├── wrangler.toml       # Worker config
│   └── package.json        # Wrangler tooling
└── .github/workflows/
    └── deploy-pages.yml    # Auto-deploy docs/ to GitHub Pages
```

## Architecture

```
Browser (GitHub Pages)
        |
        |  CORS request
        v
Cloudflare Worker (holds KIWI_API_KEY secret)
        |
        |  signed request with apikey
        v
Kiwi.com Tequila API
```

## Prerequisites

- GitHub account
- Cloudflare account
- Free Kiwi.com Tequila API key: https://tequila.kiwi.com

## Setup

### 1. Fork / create the repo

Push this project to a GitHub repository named `bali-budget`.

### 2. Enable GitHub Pages

Go to **Settings → Pages**:
- Source: **GitHub Actions**

Push to `main` or run the `deploy-pages.yml` workflow manually. Your site will be at `https://YOUR_USERNAME.github.io/bali-budget`.

### 3. Deploy the Cloudflare Worker

```bash
cd worker
npm install
npx wrangler login

# Set secrets
npx wrangler secret put KIWI_API_KEY
# paste your Kiwi API key

npx wrangler secret put ALLOWED_ORIGIN
# paste your GitHub Pages URL, e.g. https://yourusername.github.io

npx wrangler deploy
```

Copy the deployed Worker URL (e.g. `https://bali-budget-worker.youraccount.workers.dev`).

### 4. Connect frontend to Worker

Edit `docs/index.html` and replace:

```js
const WORKER_URL = "https://bali-budget-worker.YOUR_SUBDOMAIN.workers.dev";
```

with your actual Worker URL. Commit and push. GitHub Actions will redeploy the page.

## Worker endpoints

- `GET /locations?term=helsinki`
  Returns matching airports/cities from Kiwi.

- `GET /search?origin=HEL&destination=DPS&date_from=2026-09-01&date_to=2026-09-01&trip_type=one-way`
  Returns cheapest flights. For round-trip, also pass `return_from` and `return_to`.

## Security notes

- Never commit `KIWI_API_KEY` to git. It lives only in Cloudflare secrets.
- Set `ALLOWED_ORIGIN` to your GitHub Pages URL in production; do not leave it as `*`.
- The worker does not log or store queries.

## Costs

- GitHub Pages: free for public repos (100 GB soft bandwidth limit)
- Cloudflare Workers: free tier includes 100,000 requests/day
- Kiwi Tequila API: free tier available

## Next steps

- Add accommodation section using Amadeus Hotel API or Travelpayouts.
- Add a running total budget (flights + hotels + activities).
- Cache Worker responses with Cloudflare KV to reduce API calls.
