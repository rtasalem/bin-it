from db.database import database
from db.create_index import create_index

def set_up_gcc_bin_collections_index():
  collection = database['gcc_bin_collections']

  create_index(
    collection,
    [('data.bin_colours', 1)],
    'bin_colours_index'
  )

__all__ = ['gcc_bin_collections']
