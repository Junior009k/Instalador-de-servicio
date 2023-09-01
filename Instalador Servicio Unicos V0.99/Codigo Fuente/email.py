import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import re 
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# ...

def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

def send_message(service, user_id, message):
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute()
        print('Message sent successfully. Message ID: {}'.format(message['id']))
        return message
    except HttpError as error:
        print('An error occurred: {}'.format(error))

# Definir el alcance y el archivo de credenciales descargado
#SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
CREDENTIALS_FILE = 'datos.json'

def get_gmail_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)

def list_messages(service, user_id='me', label_ids=[]):
    
    response = service.users().messages().list(userId=user_id, labelIds=label_ids).execute()
    messages = response['messages']
    for message in messages:
        
        msg = service.users().messages().get(userId=user_id, id=message['id']).execute()
        if(re.findall("WeTransfer",msg['snippet'])):
            print(msg['snippet'])

if __name__ == '__main__':
    service = get_gmail_service()
    #list_messages(service)
    sender = 'junior.sidesys@gmail.com'
    to = 'junior.aquino@sidesys.com'
    subject = 'Desde python'
    message_text = 'Hola, esto es un mensaje de prueba.'

    message = create_message(sender, to, subject, message_text)
    send_message(service, 'me',message)