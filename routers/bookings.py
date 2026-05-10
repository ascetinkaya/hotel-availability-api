from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import and_
from database import get_db
from models import Booking, RoomType
from schemas import BookingCreate, BookingResponse
from typing import List
import uuid

router = APIRouter()

def generate_booking_ref() -> str:
    return "BK-" + str(uuid.uuid4())[:8].upper()

def get_booked_count(db: Session, room_type_id: int, check_in, check_out) -> int:
    return db.query(Booking).filter(
        and_(
            Booking.room_type_id == room_type_id,
            Booking.is_cancelled == False,
            Booking.check_in < check_out,
            Booking.check_out > check_in
        )
    ).count()

@router.post("/", response_model=BookingResponse)
def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    if booking.check_out <= booking.check_in:
        raise HTTPException(status_code=400, detail="check_out must be after check_in")

    room = db.query(RoomType).filter(RoomType.id == booking.room_type_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Room type not found")

    if booking.pax > room.max_occupancy:
        raise HTTPException(status_code=400, detail=f"Room max occupancy is {room.max_occupancy}")

    booked = get_booked_count(db, room.id, booking.check_in, booking.check_out)
    available = room.total_inventory - booked
    if available <= 0:
        raise HTTPException(status_code=409, detail="No availability for selected dates")

    db_booking = Booking(
        booking_ref=generate_booking_ref(),
        room_type_id=booking.room_type_id,
        guest_name=booking.guest_name,
        check_in=booking.check_in,
        check_out=booking.check_out,
        pax=booking.pax
    )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

@router.get("/", response_model=List[BookingResponse])
def list_bookings(db: Session = Depends(get_db)):
    return db.query(Booking).all()

@router.get("/{booking_ref}", response_model=BookingResponse)
def get_booking(booking_ref: str, db: Session = Depends(get_db)):
    booking = db.query(Booking).filter(Booking.booking_ref == booking_ref).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@router.delete("/{booking_ref}", response_model=BookingResponse)
def cancel_booking(booking_ref: str, db: Session = Depends(get_db)):
    booking = db.query(Booking).filter(Booking.booking_ref == booking_ref).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    if booking.is_cancelled:
        raise HTTPException(status_code=400, detail="Booking is already cancelled")

    booking.is_cancelled = True
    db.commit()
    db.refresh(booking)
    return booking

    booking.is_cancelled = True
    db.commit()
    db.refresh(db_booking)
    return booking