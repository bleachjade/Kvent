from django.test import TestCase
from Kvent.views import detail
from Kvent.models import Event, User
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

    def test_number_people(self):
        event = create_event()
        url = reverse('event-detail', args=(event.id,))
        response = self.client.get(url)
        self.assertContains(response, event.number_people)

class IndexViewTest(TestCase):
    def test_no_event(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Events")
        self.assertQuerysetEqual(response.context['all_event'], [])
    
    def test_have_one_event(self):
        event = create_event()
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(response.context['all_event'], ['<Event: Event Test>'])

    def test_location_of_event(self):
        event = create_event()
        event2 = Event.objects.create(event_name="Event Test2", 
                    location="KU",
                    short_description="The short test for this event.",
                    long_description="Test for the long description for the event.",
                    arrange_time="2020-12-20 18:00:00",
                    number_people=20,
                    full=False)
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(response.context['all_event'], ['<Event: Event Test2>', '<Event: Event Test>'])
