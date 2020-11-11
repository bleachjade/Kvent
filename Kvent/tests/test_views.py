from django.test import TestCase
from Kvent.views import detail
from Kvent.models import Event
from django.urls import reverse


def create_event():
    return Event.objects.create(event_name="Event Test", 
                    location="KU",
                    short_description="The short test for this event.",
                    long_description="Test for the long description for the event.",
                    arrange_time="2020-12-20 18:00:00",
                    number_people=20,
                    full=False)

class EventDetailViewTest(TestCase):
    def test_name(self):
        event = create_event()
        url = reverse('event-detail', args=(event.id,))
        response = self.client.get(url)
        self.assertContains(response, event.event_name)
    
    def test_location(self):
        event = create_event()
        url = reverse('event-detail', args=(event.id,))
        response = self.client.get(url)
        self.assertContains(response, event.location)
    
    def test_long_description(self):
        event = create_event()
        url = reverse('event-detail', args=(event.id,))
        response = self.client.get(url)
        self.assertContains(response, event.long_description)
    
    # def test_arrange_time(self):
    #     event = create_event()
    #     url = reverse('event-detail', args=(event.id,))
    #     response = self.client.get(url)
    #     self.assertContains(response, "Dec. 12, 2020, 6 p.m.")

    def test_number_people(self):
        event = create_event()
        url = reverse('event-detail', args=(event.id,))
        response = self.client.get(url)
        self.assertContains(response, event.number_people)