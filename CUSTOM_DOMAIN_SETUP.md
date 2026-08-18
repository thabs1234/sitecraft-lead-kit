# Custom domain — leads.sitecraftsa.co.za

The landing page currently lives at:
**https://thabs1234.github.io/sitecraft-lead-kit/**

To put it on **https://leads.sitecraftsa.co.za** you need TWO things:
1. A registered domain (`sitecraftsa.co.za`) — **not registered yet** (DNS lookup returns Non-existent domain).
2. DNS records pointing at GitHub Pages.

## Step 1 — Register the domain
Buy `sitecraftsa.co.za` from any ZA registrar (e.g. xneelo, Afrihost, Register.Domains,
Hexonet). Cost ~R99–R200/year. This is a payment step only you can do.

## Step 2 — Add DNS records at your registrar
Once registered, create these records:

**A record (apex NOT needed since we use a subdomain):**
```
Type: A
Name: leads
Value: 185.199.108.153
TTL:   3600 (or automatic)
```
Repeat the A record for each of GitHub's four IPs:
- 185.199.108.153
- 185.199.109.153
- 185.199.110.153
- 185.199.111.153

**If your registrar supports CNAME flattening / ALIAS for the subdomain instead, you can use:**
```
Type: CNAME
Name: leads
Value: thabs1234.github.io
```

## Step 3 — The GitHub side is already configured
This repo already contains a `CNAME` file with `leads.sitecraftsa.co.za`, and the
Pages custom domain has been set via the GitHub API. Status will read `pending`
until DNS propagates (can take minutes to 48h).

Verify / re-apply if needed:
```
gh api -X PUT /repos/thabs1234/sitecraft-lead-kit/pages \
  -f "source[branch]=master" -f "source[path]=/" \
  -f "cname=leads.sitecraftsa.co.za"
```

## Step 4 — Enforce HTTPS
After DNS resolves, GitHub auto-provisions an SSL cert (usually within 1 hour).
Pages setting `https_enforced: true` is already on.

## Alternative (no new domain cost)
Skip the custom domain and just use the free Pages URL, or add a subdomain on a
domain you already own by repeating Step 2 with your existing registrar.
