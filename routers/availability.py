from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import and_
from database import get_db
from models import RoomType, Booking
from schemas import AvailabilityResponse
from typing import List
from datetime import date

router = APIRouter(redirect_slashes=False)

def get_booked_count(db: Session, room_type_id: int, check_in: date, check_out: date) -> int:
    return db.query(Booking).filter(
        and_(
            Booking.room_type_id == room_type_id,
            Booking.is_cancelled == False,
            Booking.check_in < check_out,
            Booking.check_out > check_in
        )
    ).count()

@router.get("/", response_model=List[AvailabilityResponse])
def search_availability(
    hotel_id: int,
    check_in: date,
    check_out: date,
    pax: int = 1,
    db: Session = Depends(get_db)
):
    if check_out <= check_in:
        raise HTTPException(status_code=400, detail="check_out must be after check_in")

    total_nights = (check_out - check_in).days

    room_types = db.query(RoomType).filter(
        and_(
            RoomType.hotel_id == hotel_id,
            RoomType.max_occupancy >= pax
        )
    ).all()

    if not room_types:
        raise HTTPException(status_code=404, detail="No rooms found for this hotel")

    results = []
    for room in room_types:
        booked = get_booked_count(db, room.id, check_in, check_out)
        available = room.total_inventory - booked
        if available > 0:
            results.append(AvailabilityResponse(
                room_type_id=room.id,
                room_name=room.name,
                price_per_night=room.price_per_night,
                available_rooms=available,
                total_nights=total_nights,
                total_price=round(room.price_per_night * total_nights, 2)
            ))

    return results

@router.get("/{hotel_id}/rooms", response_model=List[AvailabilityResponse])
def get_hotel_rooms(
    hotel_id: int,
    check_in: date,
    check_out: date,
    db: Session = Depends(get_db)
):
    if check_out <= check_in:
        raise HTTPException(status_code=400, detail="check_out must be after check_in")

    total_nights = (check_out - check_in).days
    room_types = db.query(RoomType).filter(RoomType.hotel_id == hotel_id).all()

    if not room_types:
        raise HTTPException(status_code=404, detail="No rooms found for this hotel")

    results = []
    for room in room_types:
        booked = get_booked_count(db, room.id, check_in, check_out)
        available = room.total_inventory - booked
        results.append(AvailabilityResponse(
            room_type_id=room.id,
            room_name=room.name,
            price_per_night=room.price_per_night,
            available_rooms=available,
            total_nights=total_nights,
            total_price=round(room.price_per_night * total_nights, 2)
        ))

    return results