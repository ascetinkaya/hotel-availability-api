from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Hotel
from schemas import HotelCreate, HotelResponse
from typing import List, Optional

router = APIRouter()

@router.get("", response_model=List[HotelResponse]), summary="List Hotels"
def list_hotels(
    city: Optional[str] = None,
    country: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Hotel)
    if city:
        query = query.filter(Hotel.city.ilike(f"%{city}%"))
    if country:
        query = query.filter(Hotel.country.ilike(f"%{country}%"))
    return query.all()

@router.get("/{hotel_id}", response_model=HotelResponse), summary="Get Hotel by ID"
def get_hotel(hotel_id: int, db: Session = Depends(get_db)):
    hotel = db.query(Hotel).filter(Hotel.id == hotel_id).first()
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return hotel