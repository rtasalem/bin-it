import time
import os
from dotenv import load_dotenv
from mongo.indexes.bin_collections import set_up_bin_collections_index
from data.save_scraped_data import save_scraped_data

def main():
  load_dotenv()

  print('🗑️ Starting scraper...')

  set_up_bin_collections_index()
  save_scraped_data()

if __name__ == '__main__':
  main()
