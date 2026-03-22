import gspread
from oauth2client.service_account import ServiceAccountCredentials

def connect_sheet():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "credentials.json", scope
    )
    
    client = gspread.authorize(creds)
    
    sheet = client.open_by_url(
        "https://docs.google.com/spreadsheets/d/1rMoWvWmkmzEuYTtUw2AP1U9OeHbra63Rty0yFuTozTY/edit?usp=sharing"
        ).sheet1
    return sheet
    print("Connected successfully!")
