import dataclasses
from typing import Optional

from src.trip_service.exceptions import (
    DependantClassCallDuringUnitTestException,
    UserNotLoggedInException,
)


# Classes
class Trip:
    pass


@dataclasses.dataclass(kw_only=True)
class User:
    friends: list = dataclasses.field(default_factory=list)
    trips: list = dataclasses.field(default_factory=list)

    def add_friend(self, user: "User"):
        self.friends.append(user)

    def add_trip(self, trip: Trip):
        self.trips.append(trip)

    def has_friends(self, friend: "User") -> bool:
        return friend in self.friends


class TripService:
    @staticmethod
    def get_trips_by_user(user: User) -> list[Trip]:
        logged_user = _get_logged_user()
        if not logged_user:
            raise UserNotLoggedInException()

        has_access_to_user_trips = user.has_friends(logged_user)

        if has_access_to_user_trips:
            return _find_trips_by_user(user)
        else:
            return []


# Functions
def _get_logged_user() -> Optional[User]:
    raise DependantClassCallDuringUnitTestException(
        "_get_logged_user() should not be called in an unit test"
    )


def _find_trips_by_user(user: User) -> list[Trip]:
    raise DependantClassCallDuringUnitTestException(
        "_find_trips_by_user() should not be called in an unit test"
    )


if __name__ == "__main__":
    pass
