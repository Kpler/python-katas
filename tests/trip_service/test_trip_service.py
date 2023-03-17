from unittest.mock import patch

from src.trip_service.trip_service import Trip, TripService, User


def test_xyz() -> None:
    user = User()
    service = TripService()
    with patch(
        "src.trip_service.trip_service._get_logged_user", return_value=True
    ):
        trips = service.get_trips_by_user(user)
        assert trips == []
