import os
from dotenv import load_dotenv
from datetime import datetime
import smtplib 
from email.mime.text import MIMEText
from utils.format_bin_colours import format_bin_colours
from utils.render_emojis import render_bin_colour_emojis

def send_email_alert(collection_date, bin_colours):
  load_dotenv()

  emojis = render_bin_colour_emojis(bin_colours)
  colours = format_bin_colours(bin_colours)

  collection_date_str = datetime.strptime(collection_date, "%Y-%m-%d").strftime("%d-%m-%Y")

  body = (
    f'{emojis} The {colours} bin will be collected tomorrow ({collection_date_str}).'
  )

  sender = os.getenv('SENDER')
  recipient = os.getenv('RECIPIENT')

  msg = MIMEText(body)
  msg['Subject'] = '⚠️ Bin collection due tomorrow'
  msg['From'] = sender
  msg['To'] = recipient

  password = os.getenv('APP_PASSWORD')
  server = os.getenv('SMTP_SERVER')
  port = os.getenv('SMTP_PORT')

  with smtplib.SMTP(server, port) as smtp_server:
    smtp_server.starttls() 
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipient, msg.as_string())

  print('✉️ Email alert successfully sent')
