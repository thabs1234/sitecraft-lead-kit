#!/usr/bin/env python3
"""Generate sitecraft_sa_guide.pdf from the guide content using reportlab."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, ListFlowable, ListItem, HRFlowable,
                                KeepTogether)

ACCENT = colors.HexColor("#16a34a")
ACCENT2 = colors.HexColor("#0ea5e9")
GOLD = colors.HexColor("#f59e0b")
CARD = colors.HexColor("#f8fafc")
BORDER = colors.HexColor("#e2e8f0")
FG = colors.HexColor("#0f172a")
MUTED = colors.HexColor("#475569")

ss = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=ss["Title"], textColor=colors.white, fontSize=23, leading=27, spaceAfter=6)
SUB = ParagraphStyle("SUB", parent=ss["Normal"], textColor=colors.white, fontSize=12, leading=15)
H2 = ParagraphStyle("H2", parent=ss["Heading2"], textColor=ACCENT, fontSize=15, spaceBefore=14, spaceAfter=4)
H3 = ParagraphStyle("H3", parent=ss["Heading3"], textColor=FG, fontSize=12.5, spaceBefore=8, spaceAfter=2)
BODY = ParagraphStyle("BODY", parent=ss["Normal"], textColor=FG, fontSize=10.5, leading=14, spaceAfter=4)
SMALL = ParagraphStyle("SMALL", parent=ss["Normal"], textColor=MUTED, fontSize=9, leading=12)
CODE = ParagraphStyle("CODE", parent=ss["Normal"], textColor=colors.white, backColor=colors.HexColor("#0f172a"),
                      fontSize=9, leading=12, borderPadding=4, leftIndent=2)
WA = ParagraphStyle("WA", parent=ss["Normal"], textColor=colors.HexColor("#052e16"), backColor=colors.HexColor("#dcfce7"),
                    fontSize=9.5, leading=13, borderPadding=6, spaceAfter=6)
MONEY = ParagraphStyle("MONEY", parent=ss["Normal"], textColor=colors.HexColor("#422006"), backColor=colors.HexColor("#fef3c7"),
                       fontSize=10, leading=14, borderPadding=6)
BUL = ParagraphStyle("BUL", parent=BODY, leftIndent=10, spaceAfter=2)

def header_table():
    data = [[Paragraph("How to Make Money with Google Maps in South Africa", H1)],
            [Paragraph("A free, step-by-step guide — adapted from the \"$800 in 4 hours\" Google Maps challenge for SiteCraft SA local businesses.", SUB)]]
    t = Table(data, colWidths=[170*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), ACCENT),
        ("LEFTPADDING",(0,0),(-1,-1),16),("RIGHTPADDING",(0,0),(-1,-1),16),
        ("TOPPADDING",(0,0),(0,0),14),("BOTTOMPADDING",(0,-1),(-1,-1),12),
        ("LINEBEFORE",(0,0),(0,-1),4,ACCENT2),
    ]))
    return t

def card(flowables):
    t = Table([[flowables]], colWidths=[170*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),CARD),
        ("BOX",(0,0),(-1,-1),0.75,BORDER),
        ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),
        ("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),8),
    ]))
    return t

def bullets(items):
    return ListFlowable(
        [ListItem(Paragraph(i, BODY), leftIndent=6, value="•") for i in items],
        bulletType="bullet", start="•", leftIndent=12)

story = []
story.append(header_table())
story.append(Spacer(1, 8))
story.append(Paragraph("Your offer: <b>R1,500 setup + R450 / month</b>", ParagraphStyle("badge",parent=BODY,backColor=GOLD,textColor=colors.HexColor("#422006"),borderPadding=4,leftIndent=2)))
story.append(Spacer(1, 6))
story.append(Paragraph("This guide shows you exactly how to find small South African businesses with weak Google listings, pitch them a done-for-you online presence, and close at <b>R1,500 once-off + R450/month</b>. Zero startup cost. Works in a single afternoon.", BODY))

# 1
story.append(Paragraph("1. Validate the idea (5 minutes, free)", H2))
story.append(card([
    bullets([
        "Go to <b>trends.google.com</b>. Search <b>\"Google Business Profile\"</b> and <b>\"small business marketing South Africa\"</b>. Confirm steady interest over 5 years.",
        "Open Google Maps and search a trade in your town (e.g. <font face='Courier'>plumber Polokwane</font>). If dozens of listings look unfinished, the opportunity is real.",
        "Only target areas where you speak the local language (English / Afrikaans / Zulu / Xhosa).",
    ]),
    Paragraph("Rule: only pursue a niche that isn't a \"sinking ship.\"", SMALL)
]))

# 2
story.append(Paragraph("2. Learn the skill for free (≈42 minutes)", H2))
story.append(card([Paragraph("Google runs a <b>free \"Google Business Profile\" course on Skillshop</b> (Google's own training platform). Take it so you can honestly say you're <b>Google-trained</b> and know how to claim, verify and optimise profiles. That credibility is what gets owners to trust you.", BODY)]))

# 3
story.append(Paragraph("3. Find prospects on Google Maps", H2))
story.append(Paragraph("A — Pick your hunting ground", H3))
story.append(Paragraph("Start with <b>smaller towns</b> (less competition for attention): Polokwane, Nelspruit, Kimberley, Bloemfontein, Gqeberha/PE, Rustenburg, George, Upington. Later move to richer segments (dentists, accountants, attorneys, estate agents).", BODY))
story.append(Paragraph("B — Run the searches", H3))
story.append(Paragraph("On <font face='Courier'>maps.google.com</font>, one town at a time:", BODY))
story.append(Paragraph("\"&lt;trade&gt; in &lt;town&gt;\" &nbsp; \"&lt;trade&gt; near &lt;town&gt;\" &nbsp; \"&lt;trade&gt; &lt;suburb&gt;, &lt;town&gt;\"", CODE))
story.append(Paragraph("<b>Trade starter list:</b> salon, beauty spa, nail tech, plumber, electrician, painter, pet groomer, car wash, takeaway, coffee shop, mechanic, tutor, photographer, baker, cleaning service.", BODY))
story.append(Paragraph("C — Spot the weak profiles (red flags)", H3))
story.append(card([Paragraph("A business is worth contacting if it shows <b>2 or more</b> of these:", BODY),
    bullets([
        "Listing says <b>\"Claim this business\"</b> (never claimed)",
        "<b>No website</b> link",
        "<b>Few / low reviews</b> (under ~20, or under 4.0★)",
        "<b>Few photos</b> (under 5) or poor images",
        "<b>Missing hours / phone / address</b>",
        "<b>No posts</b> in the last 3+ months",
        "<b>Weak or blank</b> description / category",
        "Ranks low when you search the trade + town",
    ]),
    Paragraph("Skip polished businesses (100+ reviews, pro photos, active posts) — hard to sell, don't need you yet.", SMALL)
]))

# 4
story.append(Paragraph("4. Outreach — WhatsApp first (SA default)", H2))
story.append(Paragraph("SA owners answer WhatsApp far more than unknown calls. Message without saving the number using Click-to-Chat:", BODY))
story.append(Paragraph("https://wa.me/27XXXXXXXXX?text=...  (replace leading 0 with 27)", CODE))
story.append(Paragraph("WhatsApp opener:", H3))
story.append(Paragraph("Hi {Name}, I'm Thabang from SiteCraft SA 👋\n\nI was searching for \"{trade}s in {town}\" on Google Maps and noticed your business doesn't have a claimed Google profile / website yet.\n\nThat means locals searching for you right now can't easily find you. I help small businesses like yours get found — a done-for-you Google Business Profile + simple website for a once-off R1,500, then R450/month to keep it topped up.\n\nCan I send you a free 2-minute look at what your listing could be? No strings.", WA))
story.append(Paragraph("Follow-up (if no reply in 2 days):", H3))
story.append(Paragraph("Hi {Name} 👋 just following up. Even a basic Google profile gets you showing up when someone nearby searches \"{trade} {town}\". I'll send the free mini-audit either way — want me to?", WA))
story.append(Paragraph("Cold-call script (when you have a number & want speed):", H3))
story.append(Paragraph("Hi, my name is Thabang from SiteCraft SA. I help small {trade} businesses in {town} show up on Google Maps when customers search.\n\nI noticed your listing isn't claimed yet — that's free visibility you're missing. I set these up properly for a once-off R1,500 and R450 a month to keep it running. Can I send you a quick free check of your listing?", WA))

# 5
story.append(Paragraph("5. The free mini-audit (your closer)", H2))
story.append(card([
    Paragraph("Before asking for money, send a 1-page screenshot + notes showing:", BODY),
    bullets([
        "Their current listing <b>as customers see it</b> (screenshot from Maps).",
        "What's missing (the red flags from step 3C).",
        "A mock of the improved profile (claimed, correct info, 8–10 photos, posts, a \"Call/Book\" button).",
        "The math: <i>\"X% of {town} searches for {trade} — each one is a missed call today.\"</i>",
    ]),
    Paragraph("This is the exact \"free assessment\" prospects ask for. It builds trust and makes R1,500 feel like a steal.", SMALL)
]))

# 6
story.append(Paragraph("6. Close & price", H2))
story.append(Paragraph("<b>Setup: R1,500 once-off</b> (claim + optimise profile, build simple site, photos, posts).  <b>Monthly: R450</b> (keep posts fresh, reply to reviews, add photos, report views/calls).", MONEY))
story.append(Spacer(1,4))
story.append(Paragraph("To hit day-1 cash fast, close <b>1 setup</b>. The R450s are your recurring engine. Unblock hesitant owners with a guarantee: <i>\"Pay R1,200 if I don't get you 5 new reviews in 30 days\"</i> or first month free.", BODY))
story.append(Paragraph("Reference result from the challenge: closed 2 × $250 + 1 × $200 = $700 in 4 hours. Your R1,500 setup is the SA equivalent — and you keep the monthly income.", SMALL))

# 7
story.append(Paragraph("7. Deliver (so they stay & refer)", H2))
story.append(bullets([
    "Claim & verify their Google Business Profile.",
    "Fill every field: hours, services, description, correct map pin.",
    "Upload 8–10 real photos (ask them to send, or use stock + their logo).",
    "Add posts (offers, hours, \"now open\").",
    "Build the simple site (your R1,500 product) and link it.",
    "Monthly (R450): keep posts fresh, reply to reviews, add photos, report views/calls.",
]))

# 8 table
story.append(Paragraph("8. Your 4-hour blitz", H2))
blitz = [["Time","Task"],
         ["0:00–0:15","Validate niche + pick town/trade"],
         ["0:15–1:00","Maps prospecting → lead list of 20+"],
         ["1:00–1:45","Send 20 WhatsApp openers"],
         ["1:45–2:30","Send free mini-audits to replies"],
         ["2:30–3:30","Call warm replies, handle objections, close"],
         ["3:30–4:00","Invoice setup, schedule delivery, book follow-ups"]]
bt = Table(blitz, colWidths=[35*mm,135*mm])
bt.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,0),CARD),
    ("GRID",(0,0),(-1,-1),0.5,BORDER),
    ("FONTSIZE",(0,0),(-1,-1),9.5),
    ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),
    ("LEFTPADDING",(0,0),(-1,-1),6),
]))
story.append(bt)

# 9 tracker table
story.append(Paragraph("9. Lead tracker", H2))
track = [["Date","Business","Trade","Town","Contact","Red flags","Sent?","Replied?","Meeting","Closed?","Value"],
         ["","","","","","","","","","",""],
         ["","","","","","","","","","",""],
         ["","","","","","","","","","",""]]
tt = Table(track, colWidths=[16*mm,22*mm,16*mm,16*mm,22*mm,20*mm,10*mm,13*mm,16*mm,13*mm,14*mm])
tt.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,0),CARD),
    ("GRID",(0,0),(-1,-1),0.5,BORDER),
    ("FONTSIZE",(0,0),(-1,-1),7.5),
    ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),
    ("LEFTPADDING",(0,0),(-1,-1),3),("RIGHTPADDING",(0,0),(-1,-1),3),
]))
story.append(tt)
story.append(Paragraph("Target: 20–30 prospects/week → ~3–5 closes → R4,500–R7,500 setup + R1,350–R2,250/mo recurring.", SMALL))

# principles
story.append(Paragraph("Principles that make this work", H2))
story.append(bullets([
    "<b>Over-deliver</b> → long-term client → easy upsell. <i>\"Selling to an existing client is ~100× easier than acquiring a new one.\"</i>",
    "Win-win: more visibility for them = recurring income for you.",
    "Validate before you build. Learn free. Start with the easiest segment.",
    "He missed the target only by running out of time — <b>speed of follow-up is the whole game</b>.",
]))

story.append(Spacer(1,10))
story.append(HRFlowable(width="100%", color=BORDER))
story.append(Paragraph("SiteCraft SA — done-for-you websites for South African local businesses.  R1,500 setup + R450/month · WhatsApp: +27 74 508 6001 · lehauthabang@gmail.com.  Guide adapted from the \"I Tried Making $800 in 4 Hours with Google Maps\" challenge (AI Founders, 2023).", SMALL))

doc = SimpleDocTemplate("sitecraft_sa_guide.pdf", pagesize=A4,
                        leftMargin=20*mm, rightMargin=20*mm, topMargin=16*mm, bottomMargin=14*mm,
                        title="SiteCraft SA — Google Maps Money Guide",
                        author="SiteCraft SA")
doc.build(story)
print("PDF built: sitecraft_sa_guide.pdf")
