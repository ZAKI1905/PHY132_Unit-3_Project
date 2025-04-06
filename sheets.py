import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def get_google_sheet(sheet_name="ProjectAssignments"):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "secrets/project-assignment-bot.json", scope
    )
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1  # First tab
    return sheet

def log_assignment(category, title, student_id):
    sheet = get_google_sheet()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([category, title, student_id, timestamp])
    