from django.test import TestCase
from Kvent.models import Event

class EventTest(TestCase):
    """ Test the Event django models """
    def test_event_details(self):
        """ Test event details """
        event = Event(event_name="Art with Motions", 
                    location="Kasetsart University",
                    short_description="Art with Motions is the best event in town.",
                    long_description="Art with Motions is the best event in town and the only event that we have available for the next day.",
                    number_people=200,
                    full=False)
        self.assertEqual(event.get_event_name(), "Art with Motions")
        self.assertEqual(event.get_location(), "Kasetsart University")
        self.assertEqual(event.get_short_description(), "Art with Motions is the best event in town." )
        self.assertEqual(event.get_long_description(), "Art with Motions is the best event in town and the only event that we have available for the next day.")
        self.assertEqual(event.get_number_people(), 200)
        self.assertFalse(event.get_full(), False)
        self.assertTrue(isinstance(event, Event))