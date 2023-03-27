import unittest
from datetime import datetime
import requests


class ArtEvent:
    def __init__(self, name, destination, date, time, entry_fee):
        self.name = name
        self.destination = destination
        self.date = date
        self.time = time
        self.entry_fee = entry_fee
        
class ArtVenue:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.events = []
        
    def add_event(self, event):
        self.events.append(event)


class TestArtVenue(unittest.TestCase):
    def setUp(self):
        self.venue = ArtVenue("New Cultural Destination", "Delhi")
        self.gallery_event = ArtEvent("Gallery Exhibition", "New Delhi", "2023-04-15" , "10:00", "Free")
        self.theatrical_event = ArtEvent("Epic Theatrical", "Mumbai", "2023-05-20", "19:00", "Rs. 500")
        self.dance_event = ArtEvent("Contemporary Dance Performance", "Bangalore", "2023-06-30", "18:30", "Rs. 300")
        self.music_event = ArtEvent("Classical Music Concert", "Chennai", "2023-07-10", "19:30", "Rs. 1000")
        self.spoken_word_event = ArtEvent("Spoken Word Poetry Night", "Kolkata", "2023-08-05", "20:00", "Rs. 200")

    def test_add_event(self):
        venue = ArtVenue("New Cultural Destination", "Delhi")
        event = ArtEvent("Gallery Exhibition", "New Delhi", "2023-04-15", "10:00", "Free")
        venue.add_event(event)
        self.assertIn(event, venue.events)

    def test_event_details(self):
        self.venue.add_event(self.dance_event)
        event = self.venue.events[0]
        self.assertEqual(event.name, "Contemporary Dance Performance")
        self.assertEqual(event.destination, "Bangalore")
        self.assertEqual(event.date, "2023-06-30", "18:30")
        self.assertEqual(event.entry_fee, "Rs. 300")
        
if __name__ == '__main__':
    # Create the ArtVenue
    venue = ArtVenue("ArtHub", "Delhi")
    
    # Create some ArtEvent objects
    gallery_event = ArtEvent("Gallery Exhibition", "New Delhi", "2023-04-15", "10:00", "Free")
    theatrical_event = ArtEvent("Epic Theatrical", "Mumbai", "2023-05-20", "19:00", "Rs. 500")
    dance_event = ArtEvent("Contemporary Dance Performance", "Bangalore", "2023-06-30", "18:30", "Rs. 300")
    music_event = ArtEvent("Classical Music Concert", "Chennai", "2023-07-10", "19:30", "Rs. 1000")
    spoken_word_event = ArtEvent("Spoken Word Poetry Night", "Kolkata", "2023-08-05", "20:00", "Rs. 200")
    
    # Add the events to the venue
    venue.add_event(gallery_event)
    venue.add_event(theatrical_event)
    venue.add_event(dance_event)
    venue.add_event(music_event)
    venue.add_event(spoken_word_event)
    
    # Print out the details of the events at the venue
    print(f"Events at {venue.name}, {venue.city}:")
    for event in venue.events:
        print(f"\nName: {event.name}")
        print(f"Destination: {event.destination}")
        print(f"Date: {event.date}")
        print(f"Time: {event.time}")
        print(f"Entry Fee: {event.entry_fee}")

        object_id = '436535'

        # Make an API request to the Met Museum API to get the artwork information
        response = requests.get(f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}')

        # Check if the request was successful
        if response.status_code == 200:
            # Get the artwork information from the API response
            artwork_data = response.json()
            # Print the artwork information 
            print(f"Artwork Title: {artwork_data['title']}")
            print(f"Artist: {artwork_data['artistDisplayName']}")
            print(f"Department: {artwork_data['department']}")
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.reason}")

    unittest.main()

