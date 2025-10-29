FROM python:3.9-slim
WORKDIR /bin-it
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "src/scraper.py"]
