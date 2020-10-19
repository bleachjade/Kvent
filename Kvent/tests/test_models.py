from django.test import TestCase
from Kvent.models import Info
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