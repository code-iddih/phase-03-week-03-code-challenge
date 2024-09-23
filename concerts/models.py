import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    ForeignKey,
    create_engine,
    Column,
    Integer,
    String,
    Table,
    Date
)

from sqlalchemy.orm import (
    relationship,
    sessionmaker
)

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_str = 'sqlite:///' + os.path.join(BASE_DIR , 'concert.db')

engine = create_engine('sqlite:///concert.db')

Base = declarative_base()

# Band Model
class Band(Base):
    __tablename__ = 'bands'
    id = Column(Integer() , primary_key = True)
    name = Column(String(255) , nullable = False)
    hometown = Column(String(255) , nullable = False)
    # Defining the relationship
    concerts = relationship(
        'Concert', 
        back_populates = 'band'
    )

    # Object Relationship Methods

    def get_concerts(self):
        return self.concerts

    def venues(self):
        return [concert.venue for concert in self.concerts]
    
    # Aggregate and Relationship Methods

    def play_in_venue(self, venue, date):
        concert_name = f"{self.name} Festival"
        new_concert = Concert(name=concert_name, date=date, band=self, venue=venue)
        return new_concert
    
    def all_introductions(self):
        introductions =[]
        for concert in self.get_concerts():
            introductions.append(concert.introduction())
        return introductions
    
    @classmethod
    def most_performances(cls, session):
        count = {}
        bands = session.query(cls).all()
        for band in bands:
            count[band] = len(band.get_concerts())
        most_performed_band = max(count, key=count.get)
        return most_performed_band
        
# Venue Model
class Venue(Base):
    __tablename__ = 'venues'
    id = Column(Integer() , primary_key = True)
    title = Column(String(255) , nullable = False)
    city = Column(String(255) , nullable = False)
    # Defining the relationship
    concerts = relationship(
        'Concert',
        back_populates = 'venue'
    )

    # Object Relationship Methods

    def get_concerts(self):
        return self.concerts

    def bands(self):
        return [concert.band for concert in self.concerts]
    
    # Aggregate and Relationship Methods

    def concert_on(self, date):
        for concert in self.concerts:
            if concert.date == date:
                return concert
        return None  # if there is no concert on that specific date

# Concert Model
class Concert(Base):
    __tablename__ = 'concerts'
    id = Column(Integer() , primary_key = True)
    name = Column(String(255) , nullable = False)
    date = Column(String(50) , nullable = False)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))
    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')

    # Object Relationship Methods

    def get_band(self):
        return self.band

    def get_venue(self):
        return self.venue
    
    # Aggregate and Relationship Methods

    def hometown_show(self):
        return self.venue.city == self.band.hometown
    
    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
    