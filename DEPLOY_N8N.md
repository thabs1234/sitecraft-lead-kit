# Deploy to n8n — one-click-ish import

n8n has no Heroku-style "Deploy" button, but it can **import a workflow directly from a URL**.
Use the raw JSON hosted in this repo so you never copy-paste JSON by hand.

## Option A — Import from URL (fastest)
1. Open your n8n instance (cloud or self-hosted).
2. Click **"+ Add workflow" → "Import from URL"** (or **Workflows → Import from URL**).
3. Paste this raw URL:
   ```
   https://raw.githubusercontent.com/thabs1234/sitecraft-lead-kit/master/sitecraft_maps_pipeline_n8n.json
   ```
4. Click **Import**. The 6-node pipeline appears:
   `Webhook → SerpApi Maps → Score red flags → Filter ≥2 → Append to Sheet → Send WhatsApp`.

## Option B — Paste JSON
1. Open `sitecraft_maps_pipeline_n8n.json` from this repo, copy all.
2. In n8n: **Import from File / Clipboard → Paste JSON → Import**.

## After import — 4 things to wire
| Step | Where | What |
|---|---|---|
| 1 | n8n **Env vars** | Add `SERP_API_KEY` (SerpApi Google Maps engine). Without it, scraping won't run. |
| 2 | `SerpApi — Google Maps` node | Already references `{{ $env.SERP_API_KEY }}`. Confirm it resolves. |
| 3 | `Append to Google Sheet` node | Add Google Sheets OAuth2 creds; replace `REPLACE_WITH_GOOGLE_SHEET_ID` with your tracker sheet ID. |
| 4 | `Send WhatsApp opener` node | Add Twilio API creds; set `from` to your WA sender (see `TWILIO_WHATSAPP_SETUP.md`). |

## Activate
- Click **Active** on the workflow, or hit **Execute Workflow** to test once.
- Trigger via the Webhook node: `POST https://<your-n8n>/webhook/sitecraft-lead-pipeline`
  with body `{"trade":"plumber","town":"Polokwane"}`.
- Leads with **≥2 red flags** auto-append to your Sheet and get a WhatsApp opener.

## Connect the landing page
Set `window.SITECRAFT_N8N_WEBHOOK` on `index.html` to your webhook URL so form
submissions also flow into this pipeline. (Edit in the repo, re-commit, Pages rebuilds.)
