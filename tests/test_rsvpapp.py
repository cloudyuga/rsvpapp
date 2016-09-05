import mongomock
import requests
import rsvptest
import unittest


class RSVPAppTest(unittest.TestCase):
    def setUp(self):
        self.app = rsvptest.app.test_client()
        rsvptest.client = mongomock.MongoClient()
        rsvptest.db = rsvptest.client.mock_db_function

    def test_black_box_application_response(self):
        post_address = 'http://localhost:5000/new'
        user_data = {'name': 'test_name', 'email': 'test_email@test_domain.com'}
        r = requests.post(post_address, user_data)
        self.assertEqual(r.status_code, 200)

    def test_flask_app_response(self):
        user_data = {'name': 'test_name', 'email': 'test_email@test_domain.com'}
        status_code = self.app.post('/new', data=user_data, follow_redirects=True).status_code
        self.assertEqual(200, status_code)
