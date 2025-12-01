import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mongo.database import database

def backfill_missing_collection_dates(collection_dates, bin_colours):
  collection = database['bin_collections']

  query = {
    'data.date': collection_date
  }

  missing_data = {
    '$set': {
      'data.bin_colours': bin_colours
    }
  }

  result = collection.update_one(query, missing_data)

  print(f'Record for {collection_date} has been updated to include {bin_colours}')

if __name__ == '__main__':
  import sys
  import json

  collection_date = sys.argv[1]
  bin_colours = json.loads(sys.argv[2])

  backfill_missing_collection_dates(collection_date, bin_colours)
