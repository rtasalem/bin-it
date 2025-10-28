import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import pandas as pd

load_dotenv()

gcc_url = os.getenv("GCC_URL")
page = requests.get(gcc_url)
soup = BeautifulSoup(page.text, "html.parser")

all_collection_dates = soup.find_all("td", class_="CalendarDayStyle")

for collection_date in all_collection_dates:
  item = {}

  # collection_date is a <td>; read its title attribute directly
  item["Date"] = collection_date.get("title")
  img = collection_date.find("img")
  item["Bin colour"] = img.get("title") if img else None

  print(item["Bin colour"])
