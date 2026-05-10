from pydantic import BaseModel
from datetime import date
from typing import Optional

class HotelBase(BaseModel):
    name: str
    city: str
    country: str
    star_rating: Optional[int] = None
    address: Optional[str] = None

class HotelCreate(HotelBase):
    pass

class HotelResponse(HotelBase):
    id: int
    class Config:
        from_attributes = True

class RoomTypeBase(BaseModel):
    name: str
    max_occupancy: int
    price_per_night: float
    total_inventory: int

class RoomTypeCreate(RoomTypeBase):
    hotel_id: int

class RoomTypeResponse(RoomTypeBase):
    id: int
    hotel_id: int
    class Config:
        from_attributes = True

class AvailabilityResponse(BaseModel):
    room_type_id: int
    room_name: str
    price_per_night: float
    available_rooms: int
    total_nights: int
    total_price: float

class BookingCreate(BaseModel):
    room_type_id: int
    guest_name: str
    check_in: date
    check_out: date
    pax: int

class BookingResponse(BaseModel):
    id: int
    booking_ref: str
    guest_name: str
    check_in: date
    check_out: date
    pax: int
    is_cancelled: bool
    room_type: RoomTypeResponse
    class Config:
        from_attributes = True