import os
import requests
from dotenv import load_dotenv
from datetime import datetime
from utils.format_bin_colours import format_bin_colours
from utils.render_emojis import render_bin_colour_emojis

def send_push_notification(collection_date, bin_colours):
  load_dotenv()

  emojis = render_bin_colour_emojis(bin_colours)
  colours = format_bin_colours(bin_colours)

  collection_date_str = datetime.strptime(collection_date, "%Y-%m-%d").strftime("%d-%m-%Y")

  message = f'{emojis} The {colours} bin will be collected tomorrow ({collection_date_str}).'

  topic_url = os.getenv('NTFY_TOPIC_URL')
  base_url = topic_url.rsplit('/', 1)[0]
  topic = topic_url.rsplit('/', 1)[1]

  response = requests.post(
    base_url,
    json={
      'topic': topic,
      'message': message,
      'title': '⚠️ Bin collection due tomorrow 🚮',
      'priority': 3,
    },
    verify=False
  )

  response.raise_for_status()

  print('🔔 Push notification successfully sent')
