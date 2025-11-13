import os
from dotenv import load_dotenv
import smtplib 
from email.mime.text import MIMEText
import format_bin_colours from utils.format_bin_colours

def send_email_alert(collection_date, bin_colours):
  load_dotenv()

  colours = format_bin_colours(bin_colours)

  body = (
    f'The {colours} bin will be collected tomorrow ({collection_date}).'
  )

  sender = os.getenv('SENDER_EMAIL_ADDRESS')
  recipient = os.getenv('RECIPIENT_EMAIL_ADDRESS')

  msg = MIMEText(body)
  msg['Subject'] = 'BIN COLLECTION DUE TOMORROW!'
  msg['From'] = sender
  msg['To'] = recipient

  password = os.getenv('GMAIL_APP_PASSWORD')
  server = os.getenv('SMTP_SERVER')
  port = os.getenv('SMTP_PORT')

  with smtplib.SMTP(server, port) as smtp_server:
    smtp_server.starttls() 
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipient, msg.as_string())

  print('✅ Email alert successfully sent')

__all__ = ['send_emai_alert']
