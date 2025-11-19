import os
from dotenv import loadenv
import requests
import format_bin_colours from utils.format_bin_colours

def send_push_notification_alert(collection_date, bin_colours):
  load_dotenv()

  colours = format_bin_colours(bin_colours)

  topic = os.getenv('NTFY_ALERTS_TOPIC')

  message = (
    f'The {colours} bin will be collected tomorrow ({collection_date}).'
  )

  response = requests.post(
    f'https://ntfy.sh/{topic}',
    data=message.encode(encoding='utf-8'),
    headers={
      Title: 'BIN COLLECTION DUE TOMORROW!',
      tags: 'put_litter_in_its_place'
    }
  )

  print('📱 Push notification alert successfully sent')

__all__ = ['send_push_notification_alert']
