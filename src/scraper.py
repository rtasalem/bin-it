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

data = []

for collection_date in all_collection_dates:
  item = {}

  item["Date"] = collection_date.get("title")
  imgs = collection_date.find_all("img")
  item["Bin colour"] = [img.get("title") for img in imgs] if imgs else "No bins due for collection"

  data.append(item)

  print(item["Bin colour"])
  print("-----")
  print(item["Date"])
  print("-----")

print(data)

