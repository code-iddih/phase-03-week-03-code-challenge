import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Band, Venue, Concert
from datetime import date

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_str = 'sqlite:///' + os.path.join(BASE_DIR, 'concert.db')

engine = create_engine(connection_str)

Base.metadata.bind = engine

Session = sessionmaker(bind=engine)
session = Session()

# creating instances of classes to test code

# Creating band instances
band1 = Band(name="Acapella", hometown="Nairobi")
band2 = Band(name="Sauti Sol", hometown="Nakuru")
band3 = Band(name="Mbogi Genje", hometown="Eldoret")

# Creating venue instances
venue1 = Venue(title="Kasarani Square", city="Nairobi")
venue2 = Venue(title="Nyayo Stadium", city="Nakuru")
venue3 = Venue(title="Jacaranda Stadium", city="Los Angeles")

# Creating concert instances linking bands and venues
concert1 = Concert(name="Acapella Live", date="2024-10-01", band=band1, venue=venue1)
concert2 = Concert(name="Sauti Sol Festival", date="2024-10-15", band=band2, venue=venue2)
concert3 = Concert(name="Mbogi Genje Experience", date="2024-10-20", band=band3, venue=venue3)

# Adding all instances to the session
session.add_all([band1, band2, band3, venue1, venue2, venue3, concert1, concert2, concert3])

# Commiting the session
session.commit()
session.close()

print("Seeding Successful...")