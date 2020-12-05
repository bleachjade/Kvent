from django.test import TestCase
from Kvent.views import detail
from Kvent.models import Event, User
from django.urls import reverse


def create_event(event_name, location, short_description, long_description, arrange_time, number_people, full):
    return Event.objects.create(event_name=event_name, 
                    location=location,
                    short_description=short_description,
                    long_description=long_description,
                    arrange_time=arrange_time,
                    number_people=number_people,
                    full=full)


class EventDetailViewTest(TestCase):
    def test_name(self):
        event = create_event(event_name="Event Test", 
                    location="KU",
                    short_description="The short test for this event.",
                    long_description="Test for the long description for the event.",
                    arrange_time="2020-12-20 18:00:00",
                    number_people=20,
                    full=False)
        response = self.client.get(reverse('event-detail', args=(event.id,)))
        self.assertContains(response, event.event_name)
    
    def test_location(self):
        event = create_event(event_name="Event Test", 
                    location="KU",
                    short_description="The short test for this event.",
                    long_description="Test for the long description for the event.",
                    arrange_time="2020-12-20 18:00:00",
                    number_people=20,
                    full=False)
        response = self.client.get(reverse('event-detail', args=(event.id,)))
        self.assertContains(response, event.location)
    
    def test_long_description(self):
        event = create_event(event_name="Event Test", 
                    location="KU",
                    short_description="The short test for this event.",
                    long_description="Test for the long description for the event.",
                    arrange_time="2020-12-20 18:00:00",
                    number_people=20,
                    full=False)
        response = self.client.get(reverse('event-detail', args=(event.id,)))
        self.assertContains(response, event.long_description)

    def test_number_people(self):
        event = create_event(event_name="Event Test", 
                    location="KU",
                    short_description="The short test for this event.",
                    long_description="Test for the long description for the event.",
                    arrange_time="2020-12-20 18:00:00",
                    number_people=20,
                    full=False)
        response = self.client.get(reverse('event-detail', args=(event.id,)))
        self.assertContains(response, event.number_people)

class IndexViewTest(TestCase):
    def test_no_event(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Events")
        self.assertQuerysetEqual(response.context['all_event'], [])
    
    def test_have_one_event(self):
        create_event(event_name="Event Test", 
                    location="KU",
                    short_description="The short test for this event.",
                    long_description="Test for the long description for the event.",
                    arrange_time="2020-12-20 18:00:00",
                    number_people=20,
                    full=False)
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(response.context['all_event'], ['<Event: Event Test>'])

    def test_have_two_events(self):
        create_event(event_name="Event Test", 
                    location="KU",
                    short_description="The short test for this event.",
                    long_description="Test for the long description for the event.",
                    arrange_time="2020-12-20 18:00:00",
                    number_people=20,
                    full=False)
        create_event(event_name="Event Test2", 
                    location="KU",
                    short_description="The short test for this event.",
                    long_description="Test for the long description for the event.",
                    arrange_time="2020-12-20 19:00:00",
                    number_people=20,
                    full=False)
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(response.context['all_event'], ['<Event: Event Test>', '<Event: Event Test2>'])
