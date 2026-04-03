# Repair Tracker API

A basic backend API for tracking repair jobs, built with Python, FastAPI, and SQLite.

## Features

* Create repair records
* List all repairs
* Get a repair by ID
* Update a repair
* Delete a repair

## Tech Stack

* Python
* FastAPI
* SQLite
* Pydantic

## Project Structure

* `main.py` — main FastAPI application
* `repairs.db` — SQLite database file

## API Endpoints

### Health Check

* `GET /`
* Returns a simple message to confirm the API is running

### Get All Repairs

* `GET /repairs`
* Returns all repair records

### Get One Repair

* `GET /repairs/{repair_id}`
* Returns a single repair by ID

### Create Repair

* `POST /repairs`
* Example request body:

```json
{
  "device": "Ericsson Radio",
  "status": "pending"
}
```

### Update Repair

* `PUT /repairs/{repair_id}`
* Example request body:

```json
{
  "device": "Ericsson Radio",
  "status": "completed"
}
```

### Delete Repair

* `DELETE /repairs/{repair_id}`

## How to Run

1. Install dependencies:

```bash
pip install fastapi uvicorn
```

2. Start the server:

```bash
uvicorn main:app --reload
```

3. Open in your browser:

* API: `http://127.0.0.1:8000`
* Interactive docs: `http://127.0.0.1:8000/docs`

## Notes

This is a basic CRUD API project created for practice and portfolio development. It uses SQLite for simple local data storage.

## Future Improvements

* Restrict allowed status values
* Split code into multiple files
* Add better validation
* Add tests
* Deploy the API

