from schedule.scheduler import scheduler
from mongo.refresh_database import refresh_database

def execute_monthly_database_refresh():
  scheduler.add_job(
    refresh_database,
    trigger='cron',
    day=1,
    hour=0,
    minute=0,
    second=0
  )
