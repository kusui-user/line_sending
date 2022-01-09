# from __future__ import print_function
#
# import os.path
#
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from email.mime.text import MIMEText
# import base64
# from googleapiclient.errors import HttpError
#
# # If modifying these scopes, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/gmail.send']
#
# def create_message(sender, to, subject, message_text):
#     message = MIMEText(message_text)
#     message['to'] = to
#     message['from'] = sender
#     message['subject'] = subject
#     return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}
#
#
# def send_message(service, user_id, message):
#     try:
#         message = (service.users().messages().send(userId=user_id, body=message).execute())
#         print('Message Id: %s' % message['id'])
#         return message
#     except errors.HttpError as e:
#         print('An error occurred: %s' % e)
#
# def main():
#     creds = None
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'gmail_cred.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())
#
#         service = build('gmail', 'v1', credentials=creds)
#
#         sender = 'kusui.takashi@gmail.com'
#         to = 'riryubyo738@merry.pink'
#         subject ='テストメール'
#         message_text ='これはGmail apiによるテストメールです'
#
#         message = create_message(sender, to, subject, message_text)
#         send_message(service, 'me', message)
#
#
#
# if __name__ == '__main__':
#     main()

# consumer_key = 'U3ICUFbpYKsd4NVm7DDU85P2Z'
# consumer_secret = 'tvRzhaF8Vil73RXobsiwrxrRyF2xrzeSlpRFfoRqo2PL8G5f14'
# access_token = '1479589834587254784-VIT6kfOOMK5K2F0RbLn88eo96XChw9'
# access_token_secret ='yaHsFHZeiyiFtIbxfDr6TUYbulnhLS9uxuf0GiuMZxwNh'
#
# import tweepy
#
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)
#
#
# me = api.me()
# print(me.create_at)

LINE_TOKEN = '6LADcBsu8D9FeIGPIIdeOHUGTqxTOSAmKgH82lJs7AG'

import requests

def notify_message(message):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {LINE_TOKEN}'}
    data = {'message': message}
    requests.post(url,
                  headers=headers,
                  data=data
                  )

notify_message('おはようございますtoday')

print('good')

