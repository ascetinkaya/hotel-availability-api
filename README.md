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
| GET | /hotels | List hotels | Public |
| GET | /hotels/{id} | Hotel detail | Public |
| GET | /availability | Search Hotel Availability | Public |
| POST | /bookings | Create booking | Public |
| GET | /bookings | List all bookings | Public(Authentication is planned.) |
| GET | /bookings/{booking_ref} | Get booking | Public |
| DELETE | /bookings/{booking_ref} | Cancel booking | Public |
| GET | /health | Health check | Public |

## Roadmap

### v1.1
- API key authentication for protected endpoints
- User identity — bookings tied to the user who created them
- Users can only list their own bookings
- Admin role with full access
- Admin endpoints to manage hotels and room inventory without database reset (PATCH /hotels/{id}, PATCH /rooms/{room_id})

### v1.2
- Pagination on list endpoints
- Multi-property availability search by city (no hotel_id required) - consider POST-based search endpoint for complex filter support
- Rate plans and cancellation policies
- Multi-room booking (book multiple rooms in one request)

### v1.3
- Per person pricing (price varies by occupancy)
- RateID implementation — rate integrity between search and booking steps
- Migrate to PostgreSQL for persistent storage (currently SQLite resets on redeployment)

### v1.4
- Date-based rate calendar (different prices per date range)

### v2.0
- Migrate to push-based supplier model
- Hotels and room data managed by an external supplier(a new dedicated API)
- Supplier API pushes inventory and rate updates via dedicated endpoints
- AllotmentAPI becomes a pure distribution layer

## Live API

Base URL: `https://allotment-api-production.up.railway.app`

## Documentation

- Interactive docs (Swagger UI): `https://allotment-api-production.up.railway.app/docs`
- Postman documentation: `https://documenter.getpostman.com/view/52203054/2sBXwmQsxZ`