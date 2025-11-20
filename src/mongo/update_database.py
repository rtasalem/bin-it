from mongo.queries.delete_all import delete_all_documents
from data.save_scraped_data import save_scraped_data
from utils.tomorrows_date import tomorrows_date

def update_database():
  tomorrow = tomorrows_date()

  delete_all_documents(tomorrow)
  save_scraped_data()

  print('✨ Database has been updated')

__all__ = ['update_database']
