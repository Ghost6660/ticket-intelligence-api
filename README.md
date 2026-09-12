<<<<<<< HEAD
# Ticket Intelligence API

A beginner FastAPI project for creating and retrieving support tickets. The project currently stores tickets in memory and demonstrates validation, HTTP status codes, automated testing, and API documentation.

## Requirements

* Python 3
* Git
* WSL2 with Ubuntu, or another Linux environment

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Run the application

```bash
uvicorn main:app --reload
```

The application will be available at:

* API: `http://localhost:8000`
* Interactive documentation: `http://localhost:8000/docs`
* Health check: `http://localhost:8000/health`

## API endpoints

| Method | Endpoint               | Description                      |
| ------ | ---------------------- | -------------------------------- |
| `GET`  | `/health`              | Check whether the API is running |
| `POST` | `/tickets`             | Create a ticket                  |
| `GET`  | `/tickets`             | Retrieve all tickets             |
| `GET`  | `/tickets/{ticket_id}` | Retrieve one ticket              |

## Create a ticket

```bash
curl -i \
  -X POST \
  http://localhost:8000/tickets \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Cannot access account",
    "description": "The password reset link has expired",
    "priority": "high"
  }'
```

Valid priority values are:

* `low`
* `medium`
* `high`

## Retrieve tickets

Retrieve all tickets:

```bash
curl -i http://localhost:8000/tickets
```

Retrieve ticket number 1:

```bash
curl -i http://localhost:8000/tickets/1
```

## Run the tests

```bash
pytest -v
```

## Check code quality

```bash
ruff format --check .
ruff check .
```

To format the project automatically:

```bash
ruff format .
```

## Current limitations

* Tickets are stored in a Python list.
* Restarting the application deletes all existing tickets.
* There is no database or authentication yet.
* Ticket IDs are generated using the current list length.

Persistent database storage will be added later in the project.
=======
# ticket-intelligence-api
>>>>>>> eeb31c028c0be8b752633587aa90f7d3e7ffcd51
