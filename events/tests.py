from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from django.test import Client
from django.core.urlresolvers import reverse

from events.models import Location

class EventTest(TestCase):

    def create_location(self, city = 'Columbus', state = 'Ohio'):
        user = User.objects.create(username='janmilosh')
        
        return Location.objects.create (city = city,
                                        state = state,
                                        user = user,
                                        lat = '39.9611755',
                                        lon = '-82.9987942',
                                        timestamp = timezone.now())                                  

    def test_location_creation(self):
        loc = self.create_location()
        unicode_string = '%s, %s' % (loc.city, loc.state)
        self.assertTrue(isinstance(loc, Location))
        self.assertEqual(loc.__unicode__(), unicode_string)

    def test_events_login_page_view(self):
        url = reverse('lastfm.views.login')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_user_can_register_account_and_login(self):
        c = Client()
        username = 'janmilosh'
        email = 'test@test.com'
        password = 'test'
        registration_resp = c.post('/register/', {'username': username, 
                                     'email': email,
                                     'password1': password,
                                     'password2': password})
        self.assertEqual(registration_resp.status_code, 302)
        
        registration_success_url = reverse('lastfm.views.register_success')
        registration_redirect = c.get(registration_success_url)
        self.assertEqual(registration_redirect.status_code, 200)
        self.assertIn('You have registered successfully.', registration_redirect.content)

        login_resp = c.post('/login/', {'username': username,
                                        'password': password})
        self.assertEqual(login_resp.status_code, 200)