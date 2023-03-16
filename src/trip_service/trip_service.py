from src.trip_service.exceptions import DependantClassCallDuringUnitTestException, UserNotLoggedInException


class TripService:
    def get_trips_by_user(self, user):
        logged_user = _get_logged_user()
        is_friend = False
        trip_list = []
        if logged_user:
            for friend in user.get_friends():
                if friend is logged_user:
                    is_friend = True
                    break
            if is_friend:
                trip_list = _find_trips_by_user(user)
            return trip_list
        else:
            raise UserNotLoggedInException()


# Classes
class Trip:
    pass


class User:
    def __init__(self):
        self.trips = []
        self.friends = []

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
