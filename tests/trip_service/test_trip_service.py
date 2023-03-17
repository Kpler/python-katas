import pytest
from src.trip_service.exceptions import DependantClassCallDuringUnitTestException, UserNotLoggedInException
from unittest.mock import MagicMock
from src.trip_service.trip_service import User

from src.trip_service.trip_service import TripService

def test_raising_exception_when_user_is_not_logged():
    ts = TripService()
    not_logged_user = User()

    with pytest.raises(DependantClassCallDuringUnitTestException):
        ts.get_trips_by_user(not_logged_user)
    

