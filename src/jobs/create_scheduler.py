from apscheduler.schedulers.background import BackgroundScheduler

def create_scheduler():
  scheduler = BackgroundScheduler()
  
  return scheduler

__all__ = ['create_scheduler']
