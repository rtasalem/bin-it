from schedule.scheduler import scheduler
from handle_alerts import handle_bin_collection_alerts

def send_weekly_bin_collection_reminder():
  scheduler.add_job(
    handle_bin_collection_alerts,
    trigger='cron',
    day_of_week='mon-fri',
    hour=12,
    minute=0
  )

__all__ = ['send_weekly_bin_collection_reminder']
