from mongo.indexes.bin_collections import set_up_bin_collections_index
from data.save_scraped_data import save_scraped_data
from send_email_reminder import send_email_reminder

import os
from dotenv import load_dotenv

def main():
  load_dotenv()

  print('🗑️ Starting scraper...')

  set_up_bin_collections_index()
  save_scraped_data()

  sender = os.getenv('SENDER_EMAIL_ADDRESS')
  recipient = os.getenv('RECIPIENT_EMAIL_ADDRESS')

  send_email_reminder('test', 'hello world', sender, recipient)

if __name__ == '__main__':
  main()
