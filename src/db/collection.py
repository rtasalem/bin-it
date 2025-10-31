from database import database

collection = database.create_collection('bin_collection_dates')

__all__ = ['collection']
