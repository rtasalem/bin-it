import os
from dotenv import load_dotenv
from datetime import datetime
import smtplib 
from email.mime.text import MIMEText

def tmp_send_email_alert():
  load_dotenv()

  body = (
    'hello world'
  )

  sender = os.getenv('SENDER_EMAIL_ADDRESS')
  recipient = os.getenv('RECIPIENT_EMAIL_ADDRESS')

  msg = MIMEText(body)
  msg['Subject'] = 'TEST'
  msg['From'] = sender
  msg['To'] = recipient

  password = os.getenv('GMAIL_APP_PASSWORD')
  server = os.getenv('SMTP_SERVER')
  port = os.getenv('SMTP_PORT')

  with smtplib.SMTP(server, port) as smtp_server:
    smtp_server.starttls() 
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipient, msg.as_string())

  print('✉️ Email alert successfully sent')
