# from sheets import log_assignment
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def get_google_sheet(sheet_name="PHY132_Unit_3_project"):
    print(f"🔍 Attempting to open Google Sheet named: {sheet_name}")
    
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "secrets/project-assignment-bot.json", scope
    )
    client = gspread.authorize(creds)

    # List all accessible spreadsheets
    print("✅ Authenticated. Available sheets:")
    for s in client.openall():
        print(" -", s.title)

    sheet = client.open(sheet_name)
    print("📄 Successfully opened:", sheet.title)

    # List all worksheet titles
    print("📋 Worksheets:")
    for ws in sheet.worksheets():
        print("   •", ws.title)

    return sheet.sheet1  # Try to get the first worksheet

def log_assignment(category, title, student_id):
    try:
        print("Connecting to sheet...")
        sheet = get_google_sheet()
        print("Connected.")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sheet.append_row([category, title, student_id, timestamp])
        print("Row appended.")
    except Exception as e:
        print("❌ ERROR logging assignment:", e)
        
# Should create a row in your sheet
log_assignment("Debug", "Direct call test", "STUDENT_XYZ")
print("✅ If you see this, the call was made.")