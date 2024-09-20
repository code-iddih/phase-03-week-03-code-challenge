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