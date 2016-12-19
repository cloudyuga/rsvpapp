from rsvpapp import rsvp
import unittest
import mongomock
import pytest

class RSVPApp(unittest.TestCase):
    def setUp(self):
        self.app = rsvp.app.test_client()
        rsvp.client = mongomock.MongoClient()
        rsvp.db = rsvp.client.mock_db_function

    def test_Rsvp(self):
        user_data = {'name': 'test_name', 'email': 'test_email@test_domain.com'}
        status_code = self.app.post('/new', data=user_data, follow_redirects=True).status_code
        self.assertEqual(200, status_code)

@pytest.fixture
def self():
    return rsvp.app.test_client()


def test_urls(self):
    return
