// Cloudflare Worker: proxy to Kiwi.com Tequila API
// Holds KIWI_API_KEY secret, never exposes it to the browser.

const KIWI_API = "https://api.tequila.kiwi.com";

function corsHeaders(origin) {
  return {
    "Access-Control-Allow-Origin": origin || "*",
    "Access-Control-Allow-Methods": "GET, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Content-Type": "application/json",
  };
}

function badRequest(msg, origin) {
  return new Response(JSON.stringify({ error: msg }), {
    status: 400,
    headers: corsHeaders(origin),
  });
}

async function fetchJson(url, apiKey) {
  const res = await fetch(url, {
    headers: {
      "apikey": apiKey,
      "Accept": "application/json",
    },
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`Kiwi HTTP ${res.status}: ${text.slice(0, 500)}`);
  }
  return res.json();
}

export default {
  async fetch(request, env, ctx) {
    const allowedOrigin = env.ALLOWED_ORIGIN || "*";
    const requestOrigin = request.headers.get("Origin") || allowedOrigin;
    const originToUse = allowedOrigin === "*" ? requestOrigin : allowedOrigin;

    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: corsHeaders(originToUse) });
    }

    if (request.method !== "GET") {
      return new Response(JSON.stringify({ error: "Method not allowed" }), {
        status: 405,
        headers: corsHeaders(originToUse),
      });
    }

    const url = new URL(request.url);
    const path = url.pathname;

    if (path === "/search") {
      const origin = url.searchParams.get("origin");
      const destination = url.searchParams.get("destination") || "DPS";
      const dateFrom = url.searchParams.get("date_from");
      const dateTo = url.searchParams.get("date_to");
      const returnFrom = url.searchParams.get("return_from");
      const returnTo = url.searchParams.get("return_to");
      const tripType = url.searchParams.get("trip_type") || "one-way";

      if (!origin || !dateFrom || !dateTo) {
        return badRequest("Missing required params: origin, date_from, date_to", originToUse);
      }

      const params = new URLSearchParams({
        fly_from: origin,
        fly_to: destination,
        date_from: dateFrom,
        date_to: dateTo,
        curr: "EUR",
        sort: "price",
        limit: "5",
        one_for_city: "0",
        one_per_date: "0",
        partner_market: "de",
        locale: "en",
      });

      if (tripType === "round-trip" && returnFrom && returnTo) {
        params.set("return_from", returnFrom);
        params.set("return_to", returnTo);
      }

      try {
        const data = await fetchJson(`${KIWI_API}/v2/search?${params.toString()}`, env.KIWI_API_KEY);
        return new Response(JSON.stringify(data), {
          status: 200,
          headers: corsHeaders(originToUse),
        });
      } catch (err) {
        return new Response(JSON.stringify({ error: err.message }), {
          status: 502,
          headers: corsHeaders(originToUse),
        });
      }
    }

    if (path === "/locations") {
      const term = url.searchParams.get("term");
      if (!term) {
        return badRequest("Missing required param: term", originToUse);
      }
      try {
        const data = await fetchJson(
          `${KIWI_API}/locations/query?term=${encodeURIComponent(term)}&location_types=airport&limit=10&active_only=true`,
          env.KIWI_API_KEY
        );
        return new Response(JSON.stringify(data), {
          status: 200,
          headers: corsHeaders(originToUse),
        });
      } catch (err) {
        return new Response(JSON.stringify({ error: err.message }), {
          status: 502,
          headers: corsHeaders(originToUse),
        });
      }
    }

    return new Response(JSON.stringify({ error: "Not found" }), {
      status: 404,
      headers: corsHeaders(originToUse),
    });
  },
};
