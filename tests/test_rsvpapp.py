from rsvpapp import rsvp
import pytest
@pytest.fixture
def self():
    return rsvp.app.test_client()
    

def test_urls(self):
    return 

