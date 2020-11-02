"""Seed file to make sample data for users db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
pet1 = Pet(name='Mittens', species='Cat', photo_url="https://i.pinimg.com/736x/33/32/6d/33326dcddbf15c56d631e374b62338dc.jpg", age=3,
        notes="Mittens is a strong independent cat, but will cave and cuddle with you every now and then")
pet2 = Pet(name='Luna', species='Dog', photo_url="https://www.animalkingdomaz.com/wp-content/uploads/Siberian-Husky.jpg", age=5,
        notes="Luna the lovable lunatic")
pet3 = Pet(name='Goldy', species='Dog', photo_url="https://cdn.akc.org/content/hero/golden_retriever_august_hero.jpg", age=2,
        notes="Goldy the golden retriever")
pet4 = Pet(name='Goldy2', species='Dog', photo_url="https://cdn.akc.org/content/hero/golden_retriever_august_hero.jpg", age=2,
        notes="Goldy2 the golden retrievers twin")
pet5 = Pet(name='Porky', species='Porcupine', photo_url="https://p1.pxfuel.com/preview/9/10/499/hedgehog-baby-cute-animal.jpg", age=2,
        notes="Porky the porcupine", available=False)

# Add new objects to session, so they'll persist
db.session.add(pet1)
db.session.add(pet2)
db.session.add(pet3)
db.session.add(pet4)
db.session.add(pet5)

db.session.commit()
