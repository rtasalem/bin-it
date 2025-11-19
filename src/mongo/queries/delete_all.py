from mongo.database import database

def delete_all_documents(tomorrows_date):
  if tomorrows_date.day == 1:
    collection = database['bin_collections']
    doc = collection.delete_many({})

__all__ = ['delete_all']
