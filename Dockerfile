# development
FROM python:3.9-slim AS development

WORKDIR /bin-it

RUN apt-get update && apt-get install -y jq && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["watchmedo", "auto-restart", "--patterns=*.py", "--ignore-patterns=*.txt;*.env;*.json;*.log;*.db;*.pyc;__pycache__/*;*/__pycache__/*", "--recursive", "--debug", "--debug-force-polling", "--", "python", "src/main.py"]

# test
FROM development AS test

COPY requirements-test.txt .
RUN pip install --no-cache-dir -r requirements-test.txt

CMD ["pytest", "-v"]

# production
FROM python:3.9-slim AS production

WORKDIR /bin-it

RUN apt-get update && apt-get install -y jq && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "src/main.py"]
