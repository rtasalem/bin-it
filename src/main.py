import time
import os
from dotenv import load_dotenv
from mongo.indexes.bin_collections import set_up_bin_collections_index
from alerts.check_and_alert import check_and_alert
from mongo.update_database import update_database

def main():
  load_dotenv()

  set_up_bin_collections_index()
  update_database()
  check_and_alert()

  while True:
    time.sleep(1)

if __name__ == '__main__':
  main()
