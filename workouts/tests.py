from django.test import TestCase
from .models import LiftingWorkout, CardioWorkout
from django.contrib.auth import get_user_model
import datetime
import requests


class WorkoutTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testing",
            first_name="Test",
            last_name="User",
            age=20,
            weight=150,
            fitness_level=2,
            gender=1,
        )

        cls.lifting = LiftingWorkout.objects.create(
            name=cls.user,
            date=datetime.date.today(),
            exercise="Bench Press",
            weight=140,
            reps=10,
            sets=3,
            notes="ow",
        )

        cls.cardio = CardioWorkout.objects.create(
            name=cls.user,
            date=datetime.date.today(),
            exercise="Uphill Jog",
            start_time=datetime.time(11, 1, 15),
            end_time=datetime.time(11, 52, 50),
            distance=2.4,
            notes="ow",
        )

    def test_lift_model(self):
        self.assertEqual(self.lifting.name.username, "testing")
        self.assertEqual(self.lifting.date, datetime.date.today())
        self.assertEqual(self.lifting.exercise, "Bench Press")
        self.assertEqual(self.lifting.weight, 140)
        self.assertEqual(self.lifting.reps, 10)
        self.assertEqual(self.lifting.sets, 3)
        self.assertEqual(self.lifting.notes, "ow")

    def test_cardio_model(self):
        self.assertEqual(self.cardio.name.username, "testing")
        self.assertEqual(self.cardio.date, datetime.date.today())
        self.assertEqual(self.cardio.exercise, "Uphill Jog")
        self.assertEqual(self.cardio.start_time, datetime.time(11, 1, 15))
        self.assertEqual(self.cardio.end_time, datetime.time(11, 52, 50))
        self.assertEqual(self.cardio.distance, 2.4)
        self.assertEqual(self.cardio.notes, "ow")

class APITest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.query = {"limit":"10","offset":"0"}
        cls.headers = {
	        "x-rapidapi-key": "02545e6abemsh0d4efd23e797fdfp174875jsn9e006e53804a",
	        "x-rapidapi-host": "exercisedb.p.rapidapi.com"
        }
    
    def test_connection(self):
        url = "https://exercisedb.p.rapidapi.com/status"

        response = requests.get(url, headers=self.headers)

        self.assertEqual(response.json(), {'status': 'online'})
