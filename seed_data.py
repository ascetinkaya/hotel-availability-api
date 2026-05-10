from database import SessionLocal, engine, Base
from models import Hotel, RoomType

Base.metadata.create_all(bind=engine)

db = SessionLocal()

hotel1 = Hotel(
    name="Grand Istanbul Hotel",
    city="Istanbul",
    country="Turkey",
    star_rating=5,
    address="Sultanahmet, Istanbul"
)

hotel2 = Hotel(
    name="Ankara Business Hotel",
    city="Ankara",
    country="Turkey",
    star_rating=4,
    address="Kızılay, Ankara"
)

db.add_all([hotel1, hotel2])
db.commit()
db.refresh(hotel1)
db.refresh(hotel2)

rooms = [
    RoomType(hotel_id=hotel1.id, name="Standard Room", max_occupancy=2, price_per_night=150.0, total_inventory=10),
    RoomType(hotel_id=hotel1.id, name="Deluxe Room", max_occupancy=2, price_per_night=220.0, total_inventory=5),
    RoomType(hotel_id=hotel1.id, name="Suite", max_occupancy=4, price_per_night=450.0, total_inventory=3),
    RoomType(hotel_id=hotel2.id, name="Standard Room", max_occupancy=2, price_per_night=90.0, total_inventory=15),
    RoomType(hotel_id=hotel2.id, name="Executive Room", max_occupancy=2, price_per_night=140.0, total_inventory=8),
]

db.add_all(rooms)
db.commit()
db.close()

print("Seed data added successfully!")