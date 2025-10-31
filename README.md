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

The following environment variables are used by this project for local development.

| Variable | Required (yes/no) | Description |
|----------|-------------------|-------------|
| `UPRN`* | Yes | UPRN (or Unique Property Reference Number) is a unique numeric identifier tied to _your_ home address. Bin collection days varies across Glasgow, your UPRN will ensure you get notifications with the correct bin collection dates. |
| `MONGO_URI` | No | Connection string to enable client to connect to database. |

*[FindMyAddress](https://www.findmyaddress.co.uk/search) can be used to find out your UPRN.

## Local development

It is highly encouraged to run this application using Docker for local development since:

- Docker containers act as a virtual environment, removing the need to manually create the virtual environment (`venv`).
- Default, non-sensitive environment variables are set in the base [Docker Compose configuration](/compose.yaml), removing the need to store and maintain as many values in the `.env` file. 

Build the container:

```
docker compose build
```

Start the container:

```
docker compose up
```
