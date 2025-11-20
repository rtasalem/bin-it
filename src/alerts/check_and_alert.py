from mongo.queries.check_bin_collections import check_bin_collections
from alerts.email import send_email_alert
from utils.tomorrows_date import tomorrows_date

def check_and_alert():
  tomorrow = tomorrows_date()
  result = check_bin_collections(tomorrow)

  if result:
    date, bin_colours = result
    send_email_alert(date, bin_colours)
  else:
    print('No bin collections due tomorrow')

__all__ = ['check_and_alert']
