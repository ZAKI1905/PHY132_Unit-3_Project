import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import streamlit as st

# def get_google_sheet(sheet_name="PHY132_Unit_3_project"):
#     print(f"🔍 Attempting to open Google Sheet named: {sheet_name}")
    
#     scope = [
#         "https://spreadsheets.google.com/feeds",
#         "https://www.googleapis.com/auth/drive"
#     ]
#     creds = ServiceAccountCredentials.from_json_keyfile_name(
#         "secrets/project-assignment-bot.json", scope
#     )
#     client = gspread.authorize(creds)

#     # List all accessible spreadsheets
#     print("✅ Authenticated. Available sheets:")
#     for s in client.openall():
#         print(" -", s.title)

#     sheet = client.open(sheet_name)
#     print("📄 Successfully opened:", sheet.title)

#     # List all worksheet titles
#     print("📋 Worksheets:")
#     for ws in sheet.worksheets():
#         print("   •", ws.title)

#     return sheet.sheet1  # Try to get the first worksheet

# def log_assignment(category, title, student_id):
#     try:
#         print("Connecting to sheet...")
#         sheet = get_google_sheet()
#         print("Connected.")
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         sheet.append_row([category, title, student_id, timestamp])
#         print("Row appended.")
#     except Exception as e:
#         print("❌ ERROR logging assignment:", e)
        

def get_google_sheet(sheet_name="PHY132_Unit_3_project"):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "secrets/project-assignment-bot.json", scope
    )
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name)
    return sheet.worksheet("ProjectAssignments")  # Or .sheet1 if using first tab

def log_assignment(category, title, student_id):
    try:
        st.toast(f"📡 Logging project adoption...")  # Show brief popup in corner
        sheet = get_google_sheet()
        st.toast("✅ Connected to sheet.")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sheet.append_row([category, title, student_id, timestamp])
        st.success("✅ Assignment logged to Google Sheet.")
    except Exception as e:
        st.error(f"❌ Failed to log assignment: {e}")