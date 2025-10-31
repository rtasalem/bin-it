from mongo.database import database
from scraper import scraper

def save_scraped_data():
  collection = database['bin_collections']
  scraped_data = scraper()

  if scraped_data:
    collection.insert_many(scraped_data)
    print(f'💾 {len(scraped_data)} documents have been saved into bin_collections')
  else:
    print('No data available')

__all__ = ['save_scraped_data']
