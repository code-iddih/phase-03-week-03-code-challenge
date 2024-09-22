#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import ipdb
from models import Band, Venue, Concert

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///concert.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    ipdb.set_trace()  

    # Test retrieving the first Band
    first_band = session.query(Band).first()
    if first_band:
        print("First Band:")
        print(" Name:", first_band.name)
        print(" Hometown:", first_band.hometown)

        # Band get_concerts()
        # Returns a collection of all the concerts that the Band has played
        print(" Concerts for First Band:", [concert.name for concert in first_band.get_concerts()])

        # Band venues()
        # Returns a collection of all the venues that the Band has performed at
        print(" Venues for First Band:", [venue.title for venue in first_band.venues()])

        # Band play_in_venue(venue, date)
        # Creates a new concert for the band in that venue on that date
        if session.query(Venue).count() > 0:  # Ensuring there are venues available
            venue = session.query(Venue).first()  # Getting the first venue
            new_concert = first_band.play_in_venue(venue, "2024-10-11")
            session.add(new_concert)
            session.commit()
            print(" A new Concert has been Created:")
            print(" Name:", new_concert.name)
            print(" Date:", new_concert.date)

        # Band all_introductions()
        example_introduction = print(" Introductions for First Band:", first_band.all_introductions())

    # Test retrieving the first Venue
    first_venue = session.query(Venue).first()
    if first_venue:
        print("\nFirst Venue:")
        print(" Title:", first_venue.title)
        print(" City:", first_venue.city)

        # Venue get_concerts()
        # Returns a collection of all the concerts for the Venue
        print(" Concerts for First Venue:", [concert.name for concert in first_venue.get_concerts()])

        # Venue bands()
        # Returns a collection of all the bands who performed at the Venue
        print(" Bands for First Venue:", [band.name for band in first_venue.bands()])

    # Test retrieving the first Concert
    first_concert = session.query(Concert).first()
    if first_concert:
        print("\nFirst Concert:")
        print(" Name:", first_concert.name)
        print(" Date:", first_concert.date)

        # Concert get_band()
        # Returns the Band instance for this Concert
        print(" Band for First Concert:", first_concert.get_band().name)

        # Concert get_venue()
        # Returns the Venue instance for this Concert
        print(" Venue for First Concert:", first_concert.get_venue().title)

        # Concert hometown_show()
        # Returns true if the concert is in the band's hometown, false if it is not
        print(first_concert.hometown_show())

        # Concert introduction()
        # Returns a string with the band's introduction for this concert
        print(first_concert.introduction())
    
        

