// Google Apps Script — SiteCraft SA lead auto-fill (runs INSIDE Google Sheets, no Python needed)
// How to install:
//   1. Open your lead-tracker Google Sheet (or make a copy of sitecraft_sa_lead_tracker.xlsx -> upload to Drive -> open in Sheets).
//   2. Extensions -> Apps Script -> paste this whole file -> Save.
//   3. Reload the Sheet -> a "SiteCraft" menu appears with two actions.
//
// Sheets expected:
//   - "Leads"   : the tracker (Date,Business,Trade,Town,Contact,Red flags,Outreach,Replied,Meeting,Closed,Setup,Monthly)
//   - "Import"  : paste raw prospects here with columns: business, trade, town, contact, red_flags
//                 (red_flags = semicolon-separated text e.g. "no website;under 20 reviews")
//   - Set WEBHOOK_URL below to your n8n webhook to also push leads out via WhatsApp.

var WEBHOOK_URL = ""; // <- paste your n8n webhook URL here, or leave blank to skip sending

function onOpen() {
  SpreadsheetApp.getUi().createMenu("SiteCraft")
    .addItem("Import prospects -> Leads", "importProspects")
    .addItem("Push new leads to n8n", "pushNewLeads")
    .addToUi();
}

function getOrCreateSheet(name) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName(name);
  if (!sh) sh = ss.insertSheet(name);
  return sh;
}

function countRedFlags(text) {
  if (!text) return 0;
  return text.split(";").map(function(s){return s.trim();}).filter(function(s){return s.length>0;}).length;
}

function importProspects() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var src = getOrCreateSheet("Import");
  var dst = getOrCreateSheet("Leads");

  var sData = src.getDataRange().getValues();
  if (sData.length < 2) { SpreadsheetApp.getUi().alert("Import sheet is empty."); return; }

  // header row
  var headers = sData[0].map(function(h){return String(h).trim().toLowerCase();});
  function col(name){ return headers.indexOf(name); }
  var cBiz=col("business"), cTrade=col("trade"), cTown=col("town"),
      cContact=col("contact"), cRF=col("red_flags");

  // find next empty row in Leads (col B = business)
  var lData = dst.getDataRange().getValues();
  var startRow = 2;
  for (var i = 1; i < lData.length; i++) {
    if (lData[i][1] === "" || lData[i][1] == null) { startRow = i + 1; break; }
    if (i === lData.length - 1) startRow = lData.length + 1;
  }

  var added = 0;
  for (var r = 1; r < sData.length; r++) {
    var row = sData[r];
    var biz = row[cBiz]; if (!biz) continue;
    var rfText = row[cRF] || "";
    var rfCount = countRedFlags(rfText);
    var outRow = [
      new Date(),                 // Date
      biz,                        // Business
      row[cTrade] || "",          // Trade
      row[cTown] || "",           // Town
      row[cContact] || "",        // Contact
      rfCount,                    // Red flags (count)
      "", "", "", "", "", ""      // outreach, replied, meeting, closed, setup, monthly
    ];
    dst.getRange(startRow, 1, 1, outRow.length).setValues([outRow]);
    startRow++;
    added++;
  }
  SpreadsheetApp.getUi().alert("Imported " + added + " leads into the Leads sheet.");
}

function pushNewLeads() {
  if (!WEBHOOK_URL) { SpreadsheetApp.getUi().alert("Set WEBHOOK_URL in the script first."); return; }
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var dst = getOrCreateSheet("Leads");
  var data = dst.getDataRange().getValues();
  var sent = 0;
  for (var i = 1; i < data.length; i++) {
    var row = data[i];
    var business = row[1], contact = row[4], trade = row[2], town = row[3];
    var pushed = row[12]; // col M (index 12) used as "pushed?" flag
    if (business && contact && !pushed) {
      var payload = {business:business, trade:trade, town:town, contact:contact};
      try {
        UrlFetchApp.fetch(WEBHOOK_URL, {
          method: "post",
          contentType: "application/json",
          payload: JSON.stringify(payload)
        });
        dst.getRange(i+1, 13).setValue("sent"); // mark col M
        sent++;
      } catch(e) { Logger.log("Failed for " + business + ": " + e); }
    }
  }
  SpreadsheetApp.getUi().alert("Pushed " + sent + " new leads to n8n webhook.");
}
