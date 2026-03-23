import gspread
from oauth2client.service_account import ServiceAccountCredentials

def connect_to_sheets():
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "credentials.json", scope)

    client = gspread.authorize(creds)
    return client.open("Resume Screening").sheet1

def upload_data(data):
    sheet = connect_to_sheets()

    for item in data:
        sheet.append_row([
            item["file"],
            item["data"],
            item["score"]
        ])
