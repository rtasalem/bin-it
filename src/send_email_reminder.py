import os
from dotenv import load_dotenv
import smtplib 
from email.mime.text import MIMEText

def send_email_reminder(subject, body, sender, recipient, password=None):
  load_dotenv()

  if password is None:
    password = os.getenv('GMAIL_APP_PASSWORD')

  msg = MIMEText(body)
  msg['Subject'] = subject
  msg['From'] = sender
  msg['To'] = recipient

  server = os.getenv('SMTP_SERVER')
  port = os.getenv('SMTP_PORT')

  with smtplib.SMTP(server, port) as smtp_server:
    smtp_server.starttls() 
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipient, msg.as_string())

  print('✉️ Email alert has been sent')

__all__ = ['send_email_reminder']
