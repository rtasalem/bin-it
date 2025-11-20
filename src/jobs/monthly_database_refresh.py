from jobs.scheduler import scheduler
from mongo.update_database import update_database

def execute_monthly_database_refresh():
  scheduler.add_job(
    update_database,
    trigger='cron',
    day=1,
    hour=0,
    minute=0,
    second=0
  )

__all__ = ['execute_monthly_database_update']
