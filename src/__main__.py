from scraper import scraper

def main():
  print('🗑️ Starting scraper...')

  data = scraper()

  print('Finished scraping.')

  for item in data:
    print(item)

if __name__ == '__main__':
  main()
