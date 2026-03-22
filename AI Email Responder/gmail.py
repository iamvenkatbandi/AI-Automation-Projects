import os.path
import base64
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def get_gmail_service():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

def get_unread_messages(service):
    results = service.users().messages().list(userId='me', labelIds=['UNREAD'], maxResults=5).execute()
    messages = results.get('messages', [])
    return messages


def read_message(service, msg_id):
    message = service.users().messages().get(userId='me', id=msg_id).execute()
    payload = message['payload']
    headers = payload['headers']

    subject = ""
    sender = ""

    for header in headers:
        if header['name'] == 'Subject':
            subject = header['value']
        if header['name'] == 'From':
            sender = header['value']

    body = ""

    if 'parts' in payload:
        parts = payload['parts']
        for part in parts:
            if part['mimeType'] == 'text/plain':
                data = part['body']['data']
                body = base64.urlsafe_b64decode(data).decode('utf-8')
    else:
        body = base64.urlsafe_b64decode(payload['body']['data']).decode('utf-8')

    return subject, sender, body

def send_reply(service, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['subject'] = "Re: " + subject

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()

    message = {'raw': raw}

    service.users().messages().send(userId='me', body=message).execute()

def mark_as_read(service, msg_id):
    service.users().messages().modify(
        userId='me',
        id=msg_id,
        body={'removeLabelIds': ['UNREAD']}
    ).execute()
