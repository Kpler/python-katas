import pytest
from src.trip_service.exceptions import UserNotLoggedInException
from src.trip_service.trip_service import TripService, User


@pytest.fixture
def user():
    pass


def test_userservice_should_raise_exception_when_user_is_none(mocker):
    mock = mocker.patch("src.trip_service.trip_service._get_logged_user")
    user = None
    mock.return_value = user
    trip_service = TripService()
    with pytest.raises(UserNotLoggedInException):
        trip_service.get_trips_by_user(user)


def test_trip_service_should_return_empty_list_when_user_has_no_friends(mocker):
	user = User()

	mock = mocker.patch("src.trip_service.trip_service._get_logged_user")
	mock.return_value = user

	trip_service = TripService()
	trips = trip_service.get_trips_by_user(user)

	assert len(trips) == 0
