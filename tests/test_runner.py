import unittest
from runner import Session, User

from datetime import date, timedelta


class TestSession(unittest.TestCase):
    
    def test_createSessionWithDistanceAndTime(self):
        self.session = Session(10, 3600)

        self.assertEqual(10, self.session.get_distance())
        self.assertEqual(timedelta(seconds=3600), self.session.get_duration())

    def test_createSessionWithNoDateSetsTodaysDate(self):
        self.session = Session(10, 3600)

        self.assertEqual(date.today(), self.session.get_date())

    def test_createSessionWithExplicitDate(self):
        self.session = Session(10, 3600, "2024-01-24")

        self.assertEqual(date(2024, 1, 24), self.session.get_date())

    def test_computePace(self):
        self.session = Session(10, 3600)
        actual = self.session.compute_pace()
        self.assertEqual(timedelta(minutes=6), actual)

        self.session = Session(10, 3500)
        actual = self.session.compute_pace()
        self.assertEqual(timedelta(minutes=5, seconds=50), actual)

    def test_computeSpeed(self):
        self.session = Session(10, 3600)
        actual = self.session.compute_speed()
        self.assertAlmostEqual(10.0, actual, delta=0.1)

        self.session = Session(10, 3500)
        actual = self.session.compute_speed()
        self.assertAlmostEqual(10.28, actual, delta=0.1)

class Testuser(unittest.TestCase):
    
    def test_addSessionToUser_AssertUserHasOneSession(self):
        self.user = User()
        session = Session(10, 3600)
        self.user.add_session(session)

        actual = len(self.user.get_sessions())

        self.assertEqual(1, actual)

    def test_addThreeSessionsToUser_AssertuserHasThreeSessions(self):
        self.user = User()
        self.user.add_session(Session(10, 3600))
        self.user.add_session(Session(5, 1900))
        self.user.add_session(Session(12, 3600))

        actual = len(self.user.get_sessions())

        self.assertEqual(3, actual)

    def test_computeAverageDistance(self):
        self.user = User()

        self.user.add_session(Session(10, 3600))
        self.user.add_session(Session(5, 1900))
        self.user.add_session(Session(12, 3600))

        actual = self.user.compute_avg_distance()

        self.assertEqual(9, actual)
