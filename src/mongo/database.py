from mongo.client import client

database = client['bin_it']

__all__ = ['database']
