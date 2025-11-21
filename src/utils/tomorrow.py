from datetime import date, timedelta

def tomorrows_date():
  return date.today() + timedelta(days=1)
