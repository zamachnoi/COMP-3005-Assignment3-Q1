# COMP 3005 Assignment 3 Q1 - Nickolas Zamachnoi

## Pre-requisites

### Postgres Installation:

Make sure that you have a postgres server setup locally, in a docker container, or on a remote server.

**Docker Instructions:**

Download and install Docker from [Docker.com](https://docker.com)

Once installed, run this command in your preferred terminal:

```bash
docker run \
  --name pgsql-dev \
  -e POSTGRES_PASSWORD=test \
  -p 5432:5432 postgres
```

This is our Postgres DB!

### Python Installation

Make sure Python version >=3.7 is installed on your device. Check your version by running `python --version` in your terminal.

### psycopg2 Installation

This program uses psycopg2 to use SQL in our python program. Install it with:

```bash
pip install psycopg2
```

## Setup Instructions

### Step 1: Set Password Environment Variable

Set the `PGPASSWORD` environment variable to your database's password if it is not already set.

For Unix/Linux/macOS:

```bash
export PGPASSWORD='test'
```

For Windows:

```
set PGPASSWORD=test
```

### Step 2: Initialize Your Database

Setup your database with the setup.sql script, replace host, port, username, and database with your database's corresponding information.

```
psql -h localhost -p 5432 -U postgres -d postgres -f setup.sql
```

This connects to `localhost` at port `5432` in the `postgres` logical database, with user `postgres` and runs `setup.sql`

### Step 3: Run `crud.py`

Here we run the crud.py program that uses psycopg2 to connect to the database and do the CRUD operations specified in the Assignment 3 - Q1 Specification

It will ask you for input to connect to your database, such as the host, port, password, database name, and database password.

Enter that information when prompted.

```bash
python crud.py
```
