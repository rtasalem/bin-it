FROM python:3.9-slim

WORKDIR /bin-it

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["watchmedo", "shell-command", "--patterns=*.py", "--ignore-patterns=*.txt;*.env;*.json;*.log;*.db;*.pyc;__pycache__/*;*/__pycache__/*", "--recursive",  "--wait", "--command=python src/main.py"]

