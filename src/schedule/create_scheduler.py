from apscheduler.schedulers.background import BlockingScheduler

def create_scheduler():
  return BlockingScheduler()
