import os
from dotenv import load_dotenv
from pymongo import MongoClient

uri = os.getenv('MONGO_URI')
client = MongoClient(uri)
database = client['bin_it']
collection = database.create_collection('bin_collection_dates')
