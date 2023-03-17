import pytest

from unittest.mock import MagicMock

from src.trip_service.trip_service import TripService

def test_get_trip_by_user_raising():
    ts = TripService();

    with pytest.raises(DependantClassCallDuringUnitTestException):
        ts.get_trips_by_user()
    

