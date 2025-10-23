import requests
import bs4
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

gcc_url = os.getenv("GCC_URL")

response = requests.get(gcc_url)

soup = bs4.BeautifulSoup(response.text, 'html.parser')

type(response)
type(soup)

print(soup)
