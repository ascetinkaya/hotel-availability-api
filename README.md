# Hotel Availability API

A RESTful B2B hotel distribution API built with FastAPI and SQLAlchemy.

## Features

- Search hotel availability by destination, dates and occupancy
- Real-time allotment tracking — inventory decreases on booking, releases on cancellation
- Overbooking protection — returns 409 when no availability exists
- Full booking lifecycle — create, retrieve and cancel reservations
- Auto-generated Swagger documentation at `/docs`

## Tech Stack

- Python / FastAPI
- SQLAlchemy ORM
- SQLite
- Pydantic

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /hotels | List hotels with filters |
| GET | /hotels/{id} | Hotel detail |
| POST | /hotels | Create hotel |
| GET | /availability | Search availability |
| GET | /availability/{hotel_id}/rooms | Room breakdown |
| POST | /bookings | Create booking |
| GET | /bookings | List all bookings |
| GET | /bookings/{booking_ref} | Get booking |
| DELETE | /bookings/{booking_ref} | Cancel booking |
| GET | /health | Health check |

## Running Locally

```bash
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn sqlalchemy pydantic
python seed_data.py
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs` to explore the API.