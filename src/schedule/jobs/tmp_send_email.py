from schedule.scheduler import scheduler
from alerts.tmp_email import tmp_send_email_alert

def tmp_send_outlook_email():
  scheduler.add_job(
    tmp_send_email_alert,
    trigger='cron',
    minute=17
  )
