import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import pandas as pd

load_dotenv()

gcc_url = os.getenv("GCC_URL")
page = requests.get(gcc_url)
soup = BeautifulSoup(page.text, "html.parser")

print(soup.title.text)
