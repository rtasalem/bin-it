from db.indexes.bin_collections import set_up_bin_collections_index
from save_scraped_data import save_scraped_data

def main():
  print('🗑️ Starting scraper...')
  set_up_bin_collections_index()
  save_scraped_data()

if __name__ == '__main__':
  main()
