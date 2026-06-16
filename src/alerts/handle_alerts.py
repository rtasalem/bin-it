import os
from mongo.queries.check_bin_collections import check_bin_collections
from alerts.email import send_email_alert
from alerts.push_notification import send_push_notification
from utils.tomorrow import tomorrows_date

def handle_bin_collection_alerts():
  tomorrow = tomorrows_date()
  result = check_bin_collections(tomorrow)

  convertedDate = tomorrow.strftime('%d-%m-%Y')

  if result:
    date, bin_colours = result

    if os.getenv('ENABLE_EMAIL_ALERTS', '').lower() == 'true':
      send_email_alert(date, bin_colours)

    if os.getenv('ENABLE_PUSH_NOTIFICATIONS', '').lower() == 'true':
      send_push_notification(date, bin_colours)
  else:
    print(f'🗑️ No bin collections due tomorrow ({convertedDate})')
