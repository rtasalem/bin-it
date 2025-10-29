import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()

uprn = os.getenv('UPRN')
gcc_url = f'https://onlineservices.glasgow.gov.uk/forms/refuseandrecyclingcalendar/CollectionsCalendar.aspx?UPRN={uprn}'
page = requests.get(gcc_url)
soup = BeautifulSoup(page.text, 'html.parser')

all_collection_dates = soup.find_all('td', class_='CalendarDayStyle')

data = []

for collection_date in all_collection_dates:
  item = {}

  item['Date'] = collection_date.get('title')
  imgs = collection_date.find_all('img')
  item['Bin colour'] = [img.get('title').partition(' ')[0] for img in imgs] if imgs else 'No bins due for collection'

  data.append(item)

print(data)

