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

| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| GET | /hotels | List hotels with filters | Public |
| GET | /hotels/{id} | Hotel detail | Public |
| GET | /availability | Search availability | Public |
| GET | /availability/{hotel_id}/rooms | Room breakdown | Public |
| POST | /bookings | Create booking | Public |
| GET | /bookings | List all bookings | Public(Authentication is planned.) |
| GET | /bookings/{booking_ref} | Get booking | Public |
| DELETE | /bookings/{booking_ref} | Cancel booking | Public |
| GET | /health | Health check | Public |

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