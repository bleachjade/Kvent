from django.test import TestCase
from Kvent.models import Info, Event
from django.contrib.auth.models import User

class InfoTest(TestCase):
    """Test the Info django models and its get functions."""
    def test_user_info(self):
        """Test user information attributes."""
        user1 = User(first_name="Nattapol", last_name="Boonyapornpong")
        info1 = Info(user=user1, phone_num="0981322686", email="nattapol.boo@ku.th", address="NOT SET")
        self.assertEqual(info1.get_name(), "Nattapol Boonyapornpong")
        self.assertEqual(info1.get_number(), "0981322686")
        self.assertEqual(info1.get_email(), "nattapol.boo@ku.th")
        self.assertEqual(info1.get_address(), "NOT SET")
        self.assertTrue(isinstance(user1, User))
        self.assertTrue(isinstance(info1, Info))

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