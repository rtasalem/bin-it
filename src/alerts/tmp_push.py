import requests

def test_send_push_notification():
  topic = 'rana'

  message = 'hello world'

  response = requests.post(
    f'https://ntfy.sh/{topic}',
    data=message.encode(encoding='utf-8')
  )

  print('Push notification has been sent')

__all__ = ['test_send_push_notification']
