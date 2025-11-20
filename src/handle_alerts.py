from mongo.queries.check_bin_collections import check_bin_collections
from alerts.email import send_email_alert
from utils.tomorrow import tomorrows_date

def handle_bin_collection_alerts():
  tomorrow = tomorrows_date()
  result = check_bin_collections(tomorrow)

  if result:
    date, bin_colours = result
    send_email_alert(date, bin_colours)
  else:
    print('🗑️ No bin collections due tomorrow')

__all__ = ['handle_bin_collection_alerts']
