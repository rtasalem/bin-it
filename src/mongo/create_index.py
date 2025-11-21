from mongo.database import database

def create_index(collection, params, index_name, unique=False):
  collection.create_index(
    params,
    unique=unique,
    name=index_name
  )

  print(f'🍃 MongoDB index has been created: {index_name}')
