from schedule.scheduler import scheduler
from data.refresh_data import refresh_data

def execute_monthly_database_refresh():
  scheduler.add_job(
    refresh_data,
    trigger='cron',
    day=1,
    hour=0,
    minute=0,
    second=0
  )
