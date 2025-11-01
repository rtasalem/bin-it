import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from data.parse_date import parse_date

def scraper():
  load_dotenv()

  uprn = os.getenv('UPRN')
  gcc_url = f'https://onlineservices.glasgow.gov.uk/forms/refuseandrecyclingcalendar/CollectionsCalendar.aspx?UPRN={uprn}'

  page = requests.get(gcc_url)
  soup = BeautifulSoup(page.text, 'html.parser')

  all_collection_dates = soup.find_all('td', class_='CalendarDayStyle')

  data = []

  for collection_date in all_collection_dates:
    raw_date = collection_date.get('title')
    parsed_date = parse_date(raw_date)

    imgs = collection_date.find_all('img')
    bin_colours = [img.get('title').partition(' ')[0] for img in imgs] if imgs else 'None'

    item = {
      'data': {
        'date': parsed_date,
        'bin_colours': bin_colours
      }
    }

    data.append(item)

  return data
