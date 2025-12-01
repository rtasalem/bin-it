# development
FROM python:3.9-slim AS development

WORKDIR /bin-it

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["watchmedo", "auto-restart", "--patterns=*.py", "--ignore-patterns=*.txt;*.env;*.json;*.log;*.db;*.pyc;__pycache__/*;*/__pycache__/*", "--recursive", "--debug", "--debug-force-polling", "--", "python", "src/main.py"]

# production
FROM python:3.9-slim AS production

WORKDIR /bin-it

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "src/main.py"]
