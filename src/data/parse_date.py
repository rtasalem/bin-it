from datetime import datetime
import re

def parse_date(raw_date: str):
  if not raw_date:
    return None
  
  clean_date = re.sub(r'^today\s+is\s+', '', raw_date.strip(), flags=re.IGNORECASE)

  try:  
    parsed_date = datetime.strptime(clean_date, '%A, %d %B %Y')

    return parsed_date.strftime('%d-%m-%Y')
  except ValueError:
    return None

__all__ = ['parse_date']
