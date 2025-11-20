from datetime import datetime
from mongo.queries.delete_all import delete_all_documents
from handle_scraped_data import handle_scraped_data
from utils.tomorrow import tomorrows_date

def refresh_database():
  tomorrow = tomorrows_date()

  delete_all_documents(tomorrow)
  handle_scraped_data()

  now = datetime.now()
  current_month = now.strftime('%B')
  current_year = now.year

  print(f'📅 Database has been refreshed and updated for {current_month} {current_year}')

__all__ = ['refresh_database']
