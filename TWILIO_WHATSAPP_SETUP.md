# Twilio WhatsApp — n8n node config (copy-paste ready)

Drop this into your n8n workflow in place of the "Send WhatsApp opener" node
(export your current workflow, edit the JSON, re-import — or add a Twilio node manually
and paste the "parameters" values below).

## Twilio credentials needed (in n8n: Credentials → New → Twilio API)
- Account SID      : from console.twilio.com (starts AC...)
- Auth Token       : from the same console page
- Messaging Service: optional; the node uses From/To instead
IMPORTANT: your Twilio sender MUST be a WhatsApp-enabled number.
  - For testing: use Twilio's sandbox (join by messaging the sandbox code).
  - For production: request a WhatsApp Sender (business profile) in Twilio Console.

## Node parameters (paste into the Twilio node's "parameters" object)
{
  "resource": "message",
  "operation": "send",
  "from": "whatsapp:+14155238886",          // Twilio sandbox / your WA sender
  "to": "whatsapp:{{ $json.contact }}",      // lead's phone from previous node
  "body": "Hi {{ $json.business }}, I'm Thabang from SiteCraft SA. I noticed your Google listing for {{ $json.trade }} in {{ $json.town }} isn't fully set up yet — that's free visibility you're missing. I set these up properly (claimed profile + simple site) for R1,500 once-off + R450/month. Can I send a free 2-min look at what your listing could be?",
  "mediaUrl": "https://thabs1234.github.io/sitecraft-lead-kit/sitecraft_sa_guide.pdf"  // attach the guide
}

## Full node JSON snippet (for in-file edits)
{
  "parameters": {
    "resource": "message",
    "operation": "send",
    "from": "whatsapp:+14155238886",
    "to": "=whatsapp:{{ $json.contact }}",
    "body": "Hi {{ $json.business }}, I'm Thabang from SiteCraft SA. I noticed your Google listing for {{ $json.trade }} in {{ $json.town }} isn't fully set up yet — that's free visibility you're missing. I set these up properly (claimed profile + simple site) for R1,500 once-off + R450/month. Can I send a free 2-min look at what your listing could be?",
    "mediaUrl": "https://thabs1234.github.io/sitecraft-lead-kit/sitecraft_sa_guide.pdf"
  },
  "name": "Send WhatsApp opener",
  "type": "n8n-nodes-base.twilio",
  "typeVersion": 1,
  "position": [1440, 300],
  "credentials": { "twilioApi": "your-twilio-cred" }
}

## Phone-number formatting gotcha
Twilio requires E.164. South African numbers from Maps scrape may arrive as
"074 508 6001" or "+27 74 508 6001". Add a Function node BEFORE this one to normalise:
const norm = (s) => "+27" + s.replace(/\D/g,'').replace(/^0/, '').slice(-9);
return [{ json: { ...items[0].json, contact: norm(items[0].json.contact) } }];
