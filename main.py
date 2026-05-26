from fastapi import FastAPI
from database import engine, Base
from routers import hotels, availability, bookings

Base.metadata.create_all(bind=engine)

import seed_data

app = FastAPI(
    title="AllotmentAPI Project",
    description="A B2B hotel distribution API for searching availability and managing bookings",
    version="1.0"
)

app.include_router(hotels.router, prefix="/hotels", tags=["Hotels"], redirect_slashes=False)
app.include_router(availability.router, prefix="/availability", tags=["Availability"], redirect_slashes=False)
app.include_router(bookings.router, prefix="/bookings", tags=["Bookings"], redirect_slashes=False)

@app.get("/health")
def health_check():
    return {"status": "ok", "version": "1.0"}