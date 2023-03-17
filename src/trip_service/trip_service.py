import dataclasses

from src.trip_service.exceptions import (
    DependantClassCallDuringUnitTestException,
    UserNotLoggedInException,
)


class TripService:
    @staticmethod
    def get_trips_by_user(user):
        logged_user = _get_logged_user()
        if not logged_user:
            raise UserNotLoggedInException()

        is_friend = False
        trip_list = []

        for friend in user.friends:
            if friend is logged_user:
                is_friend = True
                break
        if is_friend:
            trip_list = _find_trips_by_user(user)
        return trip_list


# Classes
class Trip:
    pass


@dataclasses.dataclass(kw_only=True)
class User:
    friends: list = dataclasses.field(default_factory=list)
    trips: list = dataclasses.field(default_factory=list)

    def add_friend(self, user):
        self.friends.append(user)

    def add_trip(self, trip):
        self.trips.append(trip)


# Functions
def _get_logged_user():
    raise DependantClassCallDuringUnitTestException(
        "_get_logged_user() should not be called in an unit test"
    )


def _find_trips_by_user(user):
    raise DependantClassCallDuringUnitTestException(
        "_find_trips_by_user() should not be called in an unit test"
    )


if __name__ == "__main__":
    pass
