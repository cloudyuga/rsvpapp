from rsvpapp import rsvptest
import pytest
@pytest.fixture
def self():
    return rsvptest.app.test_client()
    

def test_urls(self):
    return 

