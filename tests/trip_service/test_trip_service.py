
import pytest
from src.trip_service.exceptions import UserNotLoggedInException
from trip_service import TripService

@pytest.fixture
def user():
    pass

def test_user_should_not_be_empty():
    trip_service = TripService()
    trip_service.get_trips_by_user()
    pytest.assertRaises(UserNotLoggedInException)