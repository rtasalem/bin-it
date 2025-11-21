import time
import os
from dotenv import load_dotenv
from mongo.indexes.bin_collections import setup_bin_collections_index
from handle_scraped_data import handle_scraped_data
from schedule.jobs.monthly_database_refresh import execute_monthly_database_refresh
from schedule.jobs.weekly_reminders import send_weekly_bin_collection_reminder

from schedule.jobs.tmp_send_email import tmp_send_outlook_email

def main():
  load_dotenv()

  setup_bin_collections_index()
  handle_scraped_data()
  execute_monthly_database_refresh()
  send_weekly_bin_collection_reminder()

  tmp_send_outlook_email()

  while True:
    time.sleep(1)

if __name__ == '__main__':
  main()
