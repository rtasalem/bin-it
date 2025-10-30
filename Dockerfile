FROM python:3.9-slim

WORKDIR /bin-it

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "src/__main__.py"]
