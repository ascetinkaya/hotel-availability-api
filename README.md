# AllotmentAPI Project

A RESTful B2B hotel distribution API built with FastAPI and SQLAlchemy.
This project does not aim any commercial profit, but personal development in API domain; how APIs work behind the scene in travel ecosystem. New versions are planned to be built as a milestone in my API understanding. 

## Features

- Search hotel availability by defining hotel id, check-in/check-out dates and pax.
- Real-time allotment tracking — inventory decreases on booking, releases on cancellation.
- Overbooking protection — returns 409 when no availability exists.
- Full booking lifecycle — create, retrieve and cancel reservations.

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
| POST | /hotels | Create hotel | AUTH |
| GET | /availability | Search availability |
| GET | /availability/{hotel_id}/rooms | Room breakdown |
| POST | /bookings | Create booking |
| GET | /bookings | List all bookings | AUTH |
| GET | /bookings/{booking_ref} | Get booking |
| DELETE | /bookings/{booking_ref} | Cancel booking |
| GET | /health | Health check |

> AUTH: Authentication required — not yet implemented, planned for v1.1

## Roadmap

### v1.1
- API key authentication for protected endpoints
- Partner identity — bookings tied to the partner who created them
- Partners can only list their own bookings
- Admin role with full access

## Running Locally

```bash
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn sqlalchemy pydantic
python seed_data.py
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs` to explore the API.