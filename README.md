# Bin It! 🗑️
Scrape the [Glasgow City Council Refuse and Recycling Calendar](https://www.glasgow.gov.uk/article/1524/Bin-Collection-Days) and send out notification reminders the day before a bin collection is due that includes which bins are being collected:  

💙 Blue - Paper, card, cardboard  
🤎 Brown - Food and garden waste  
💚 Green - General non-recyclable household waste  
🩶 Grey - Plastics, metals, film  
💜 Purple - Glass  

For the most up to date information on what waste should go into which bin, refer to the Glasgow City Council article: [_What goes in your bin?_](https://www.glasgow.gov.uk/article/13729/What-goes-in-your-bin)

## Prerequisites

Docker  
Docker Compose  
Python

## Environment variables

The following environment variables are used by this project for local development _within a Docker container_.

| Variable | Required (yes/no) | Description |
|----------|-------------------|-------------|
| `UPRN` | Yes | UPRN* (or Unique Property Reference Number) is a unique numeric identifier tied to _your_ home address. Bin collection days varies across Glasgow, your UPRN will ensure you get notifications with the correct bin collection dates. |
| `MONGO_URI` | No | Connection string to enable client to connect to database. |

*[FindMyAddress](https://www.findmyaddress.co.uk/search) can be used to find out your UPRN.

## Local development

### Create virtual environment

This application can be ran locally on the host machine. First a virtual environment must be created:

```
python -m venv venv # for some the correct command may be python3
```

Once created, activate the virtual environment:

```
source venv/bin/activate
```

### Install dependencies

All required dependencies are listed in and available at [`requirements.txt`](/requirements.txt). Dependencies must be installed prior to running the app:

```
pip install -r requirements.txt # for some the correct command may be pip3
```

### Starting the application

Start the application:

```
python src/__main__.py
```

## Docker

It is encouraged to run this application using Docker for local development since:

- Docker containers act as a virtual environment, removing the need to manually create the environment as demonstrated above.
- Default, non-sensitive environment variables are set in the base [Docker Compose configuration](/compose.yaml), removing the need to store and maintain as many values in a `.env` file. 

Build the container:

```
docker compose build
```

Start the container:

```
docker compose up
```
