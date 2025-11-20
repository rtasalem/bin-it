from mongo.database import database
from mongo.create_index import create_index

def setup_bin_collections_index():
  collection = database['bin_collections']

  create_index(
    collection,
    [('data.bin_colours', 1)],
    'bin_colours_index'
  )

  create_index(
    collection,
    [('data.date', 1)],
    'date_index'
  )

__all__ = ['setup_bin_collections_index']
