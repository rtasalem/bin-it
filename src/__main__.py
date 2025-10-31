from scraper import scraper

def main():
  print('🗑️ Starting scraper...')

  data = scraper()

  for item in data:
    print(item)

if __name__ == '__main__':
  main()
