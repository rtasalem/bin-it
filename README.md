# Bin It! 🚮

Python application that scrapes the [Glasgow City Council (GCC) Refuse and Recycling Calendar](https://www.glasgow.gov.uk/article/1524/Bin-Collection-Days) and sends out email alerts the day before a bin collection is due, including which bins are being collected:  

💙 Blue - Paper, card, cardboard  
🤎 Brown - Food and garden waste  
💚 Green - General non-recyclable household waste  
🩶 Grey* - Plastics, metals, film  
💜 Purple - Glass  

For the most up to date information on what waste should go into which bin, refer to the GCC article: [_What goes in your bin?_](https://www.glasgow.gov.uk/article/13729/What-goes-in-your-bin)

Below is an example of the email sent by the application.

![example email](email.jpg)

*The grey bin is relatively new and therefore GCC have yet to update the online calendar to include grey bin collection dates. It is possible to [backfill these missing records](#backfill-missing-records). Alternatively, you can refer to a hard copy of your local bin collection calendar (typically sent via post at the start of the year).

## Prerequisites

Docker  
Docker Compose  
Python

## Environment variables

The following environment variables are used by this project for local development. Variables not required are provided a default value in the Docker Compose configuration. Variables that are required must be defined in the `.env` file.

| Variable | Required | Description |
|----------|----------|-------------|
| `UPRN`* | Yes | UPRN (or Unique Property Reference Number) is a unique numeric identifier tied to _your_ home address. Bin collection days varies across Glasgow, your UPRN will ensure you get notifications with the correct bin collection dates. |
| `MONGO_URI` | No | Connection string to enable client to connect to database. |
| `ME_CONFIG_MONGODB_URL` | No | Same as `MONGO_URI`, connects to MongoDB instance to allow for database interactions through GUI accessible via the browser. |
| `ME_CONFIG_BASICAUTH_USERNAME` | Yes | Mongo Express username for authentication at the application level. |
| `ME_CONFIG_BASICAUTH_PASSWORD` | Yes | Mongo Express Password for authentication at the application level. |
| `SMTP_SERVER`** | No | Server definition based on email address being used for `sender`. |
| `SMTP_PORT` | No | Port to bind for `SMTP_SERVER`. |
| `APP_PASSWORD` | Yes| App password to authenticate `sender` email sent as automated reminders from this application. |
| `SENDER` | Yes | Email address of the sender. |
| `RECIPIENT` | Yes | Email address of the recipient. |

*[FindMyAddress](https://www.findmyaddress.co.uk/search) can be used to find out your UPRN.  

**For your own personal use, you should change this if you intend to use the app with a different email provider e.g. Outlook.  

## Application overview

```mermaid
sequenceDiagram
  participant GCC as Glasgow City Council
  participant APP as Bin It!
  participant MONGODB as MongoDB
  participant USER as User

  loop Every 1st of the month at midnight
    APP->>GCC: Scrape (with UPRN)
    APP->>MONGODB: Delete data for previous month and store newly scraped data
  end

  loop Every Tuesday & Wednesday at middday
    APP->>MONGODB: Check if bin collections are due tomorrow
    MONGODB-->>APP: Retrieve bin colours for tomorrow's collections
    APP->>USER: Format and send user email reminder
  end
```

## Local development

It is highly encouraged to run this application using Docker for local development since:

- Docker containers act as a virtual environment, removing the need to manually create the virtual environment (`venv`).
- Default, non-sensitive environment variables are set in the base [Docker Compose configuration](/compose.yaml), removing the need to store and maintain as many values in the `.env` file. 

Build the container:

```bash
docker compose build
```

Start the container:

```bash
docker compose up
```

## Production (TBC)

To run the production container, first build the container:

```bash
docker compose build
```

Start the container:

```bash
docker compose -f compose.yaml up
```

## Backfill missing records

To backfill or even update the existing database records, a script it available for selecting which collection date needs updating.  

First, open a shell inside the `bin-it` container:

```bash
docker exec -it bin-it /bin/bash
```

Run the [`backfill.sh`](./backfill.sh) script:

```bash
./backfill.sh
```

Follow the prompts to update as many records as needed.

## MongoDB

### Indexes

To ensure efficient query performance, the following indexes are created on database startup:

- `bin_colours_index`: intended for more general querying to check future dates of specific bin colours.

> **As a** user  
> **I want** to occasionally query the database by `bin_colours`  
> **So that** I have the option to check future collection dates based on specific `bin_colours`.

- `date_index`: intended for use by the application itself when running cron jobs to check and send alerts when a bin collection is due.

> **As the** application  
> **I want** to routinely query the database by `date`  
> **So that** I can alert users when a bin collection is due the next day.

### Database usage

For local development, [MongoDB Compass](https://www.mongodb.com/products/tools/compass) is an official GUI for interacting with MongoDB instances.

Alternatively for local development and in production, a GUI is provided for the application: [`mongo-express`](https://hub.docker.com/_/mongo-express).
