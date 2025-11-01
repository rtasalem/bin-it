from db.database import database

def check_database(target_date: str):
  collection = db['bin_collections']

  result = collection.find_one({ 'data.date': target_date })
  return result['data'] if result else None

