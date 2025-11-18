FROM python:3.9-slim

WORKDIR /bin-it

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["watchmedo", "auto-restart", "--patterns=*.py", "--ignore-patterns=*.txt;*.env;*.json;*.log;*.db;*.pyc;__pycache__/*", "--recursive", "--", "python", "src/main.py"]
