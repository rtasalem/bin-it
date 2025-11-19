from mongo.database import database

def check_bin_collections(tomorrows_date):
  collection = database['bin_collections']
  tomorrow_str = tomorrows_date.strftime("%Y-%m-%d")

  doc = collection.find_one(
    {
    'data.date': tomorrow_str,
    'data.bin_colours': {'$exists': True, '$not': {'$size': 0}}
    },
    {
      '_id': 0,
      'data.date': 1,
      'data.bin_colours': 1 
    }
  )

  if not doc:
    return None

  date = doc['data']['date']
  bin_colours = doc['data']['bin_colours']

  return date, bin_colours
