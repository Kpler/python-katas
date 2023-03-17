from unittest.mock import patch

from src.trip_service.trip_service import Trip, TripService, User


def test_empty_trip_service() -> None:
    user = User()
    service = TripService()
    with patch("src.trip_service.trip_service._get_logged_user", return_value=True):
        trips = service.get_trips_by_user(user)
        assert trips == []


@patch("src.trip_service.trip_service._get_logged_user")
@patch("src.trip_service.trip_service._find_trips_by_user")
def test_single_trip_service(mocker_find_trips_by_user, mocked_get_logged_user) -> None:
    logged_user = User()
    mocked_get_logged_user.return_value = logged_user

    query_user = User()
    query_user.add_friend(logged_user)

    trip = Trip()
    mocker_find_trips_by_user.return_value = [trip]

    service = TripService()
    trips = service.get_trips_by_user(query_user)
    assert trips == [trip]
