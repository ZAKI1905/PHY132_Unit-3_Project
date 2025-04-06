import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import streamlit as st

def get_google_sheet(sheet_name="PHY132_Unit_3_project"):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    # Load credentials from Streamlit secrets
    creds_dict = st.secrets["gcp_service_account"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    return client.open(sheet_name)

def get_project_status_sheet():
    # Assumes your status sheet is named "ProjectStatus"
    sheet = get_google_sheet()
    return sheet.worksheet("ProjectStatus")

def get_project_statuses():
    """
    Returns a dictionary keyed by (Category, Title)
    with values as the row data from the ProjectStatus sheet.
    Assumes the sheet has headers: "Category", "Title", "Status", "Student ID", "Timestamp"
    """
    ws = get_project_status_sheet()
    records = ws.get_all_records()
    statuses = {}
    for row in records:
        key = (row["Category"], row["Title"])
        statuses[key] = row
    return statuses

def update_project_status(category, title, student_id, new_status="taken"):
    """
    Updates the ProjectStatus sheet for the given project.
    If the project does not exist, it appends a new row.
    Otherwise, it updates the "Status", "Student ID", and "Timestamp" columns.
    """
    ws = get_project_status_sheet()
    records = ws.get_all_records()
    row_index = None
    # Note: Google Sheets rows are 1-indexed, and row 1 is usually the header.
    for idx, row in enumerate(records, start=2):
        if row["Category"] == category and row["Title"] == title:
            row_index = idx
            break
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if row_index is None:
        # Append new row if not found
        ws.append_row([category, title, new_status, student_id, timestamp])
    else:
        # Update the appropriate cells; assuming columns:
        # A: Category, B: Title, C: Status, D: Student ID, E: Timestamp
        ws.update_cell(row_index, 3, new_status)
        ws.update_cell(row_index, 4, student_id)
        ws.update_cell(row_index, 5, timestamp)

def log_assignment(category, title, student_id, action="adopted"):
    try:
        st.toast(f"📡 Logging project {action}...")
        sheet = get_google_sheet()
        st.toast("✅ Connected to sheet.")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Append a row that includes the action.
        sheet.append_row([category, title, student_id, action, timestamp])
        st.success("✅ Project event logged to Google Sheet.")
    except Exception as e:
        st.error(f"❌ Failed to log project event: {e}")