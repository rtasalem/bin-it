import time
import os
from dotenv import load_dotenv
from mongo.indexes.bin_collections import set_up_bin_collections_index
from data.save_scraped_data import save_scraped_data

from alerts.tmp_push import test_send_push_notification

def main():
  load_dotenv()

  print('🗑️ Starting scraper...')

  set_up_bin_collections_index()
  save_scraped_data()

  test_send_push_notification()

if __name__ == '__main__':
  main()
