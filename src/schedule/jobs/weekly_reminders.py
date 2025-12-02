from schedule.scheduler import scheduler
from alerts.handle_alerts import handle_bin_collection_alerts

def send_weekly_bin_collection_reminder():
  scheduler.add_job(
    handle_bin_collection_alerts,
    trigger='cron',
    hour=12,
    minute=0
  )
