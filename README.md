# SiteCraft SA — Google Maps Lead Kit

A done-for-you lead-generation kit for **SiteCraft SA** (R1,500 setup + R450/month websites for South African local businesses), adapted from the *"I Tried Making $800 in 4 Hours with Google Maps"* challenge (AI Founders, 2023).

Everything you need to find weak Google Business Profiles, pitch them on WhatsApp, and close at R1,500 + R450/mo — plus automation to scale it.

## 📦 What's inside

| File | What it is |
|---|---|
| `index.html` | **Live landing page** (lead magnet) — captures name/business/WhatsApp, fires `window.hermes.send` + wa.me button, posts to an n8n webhook when configured. Hosted on GitHub Pages. |
| `sitecraft_sa_guide.pdf` | The free, printable step-by-step guide (3 pages). |
| `sitecraft_sa_guide.html` | Same guide as web page (print-to-PDF ready). |
| `sitecraft_sa_playbook.md` | Full operating playbook: niche validation, Maps search template, red-flag checklist, WhatsApp + call scripts, 4-hour blitz. |
| `sitecraft_sa_lead_tracker.xlsx` | Working lead tracker (Leads / Summary / How-to tabs) with dropdowns + live formulas (reply rate, close rate, revenue). |
| `import_leads.py` | Auto-fill the tracker from a CSV of prospects (verified). Includes a `scrape_maps()` stub that activates with `SERP_API_KEY`. |
| `leads_input.csv` | Sample CSV of 5 SA businesses (format reference for `import_leads.py`). |
| `sitecraft_maps_pipeline_n8n.json` | n8n workflow: Webhook → SerpApi Maps → score red flags → filter ≥2 → append to Google Sheet → send WhatsApp opener. |
| `build_guide_pdf.py`, `build_tracker_xlsx.py` | Regenerate the PDF / XLSX from scratch. |

## 🚀 Quick start (manual)
1. Open `sitecraft_sa_playbook.md` and read §3–§4.
2. On Google Maps, search `"<trade> in <town>"` (e.g. `plumber Polokwane`).
3. For each weak profile, add a row in `sitecraft_sa_lead_tracker.xlsx` (count red flags).
4. Send the WhatsApp opener from the guide / playbook.
5. On a win: set `Closed? = Yes`, fill `Setup (R1,500)` + `Monthly (R450)`. The Summary tab tallies revenue.
6. Bulk-import a list: drop rows into `leads_input.csv`, then `python import_leads.py`.

## ⚡ Automate it (n8n)
1. Import `sitecraft_maps_pipeline_n8n.json` into n8n.
2. Set `SERP_API_KEY` (SerpApi Google Maps engine) in n8n env.
3. Add your Google Sheets + Twilio WhatsApp credentials; replace the GSheet ID.
4. Trigger the webhook with `{"trade":"plumber","town":"Polokwane"}` — leads flow into the sheet and get a WA opener automatically.
5. Point the landing page's `window.SITECRAFT_N8N_WEBHOOK` at the webhook so form leads also flow in.

## 🌐 Live landing page
Hosted at: `https://thabs1234.github.io/sitecraft-lead-kit/`
(Replace with your actual Pages URL after publish.)

## Notes
- The live Maps scrape + WhatsApp send require API keys/credentials — they're coded but not run here (no browser/keys on the build host).
- `import_leads.py`'s `scrape_maps()` is a no-op until `SERP_API_KEY` / `GOOGLE_MAPS_API_KEY` is set.

© SiteCraft SA · WhatsApp +27 74 508 6001 · lehauthabang@gmail.com
