from apscheduler.schedulers.background import BackgroundScheduler

def create_scheduler():
  scheduler = BackgroundScheduler()

__all__ = ['create_scheduler']
