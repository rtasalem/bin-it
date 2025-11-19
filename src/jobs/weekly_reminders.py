from jobs.scheduler import scheduler
from alerts.check_and_alert import check_and_alert


def send_weekly_bin_collection_reminder():
  scheduler.add_job(
    check_and_alert,
    trigger='cron',
    day_of_week='mon-fri',
    hour=12,
    minute=0
  )

__all__ = ['send_weekly_bin_collection_reminder']
