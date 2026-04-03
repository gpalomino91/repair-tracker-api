# Repair Tracker API

A basic backend API for tracking repair jobs, built with Python, FastAPI, and SQLite.

## Features

- Create repair records
- List all repairs
- Get a repair by ID
- Update a repair
- Delete a repair

## Tech Stack

- Python
- FastAPI
- SQLite
- Pydantic

## Project Structure

- `main.py` — main FastAPI application
- `repairs.db` — SQLite database file

## API Endpoints

### Health Check
- `GET /`
- Returns a simple message to confirm the API is running

### Get All Repairs
- `GET /repairs`
- Returns all repair records

### Get One Repair
- `GET /repairs/{repair_id}`
- Returns a single repair by ID

### Create Repair
- `POST /repairs`
- Example request body:

```json
{
  "device": "Ericsson Radio",
  "status": "pending"
}
