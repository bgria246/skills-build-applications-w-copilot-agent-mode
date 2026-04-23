from django.test import TestCase
from .models import Team, User, Workout, Activity, Leaderboard

class ModelSmokeTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='TestTeam')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='pw', team=self.team)
        self.workout = Workout.objects.create(name='TestWorkout', description='desc')
        self.activity = Activity.objects.create(user=self.user, workout=self.workout, duration=10, calories=100)
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=42)

    def test_team(self):
        self.assertEqual(str(self.team), 'TestTeam')

    def test_user(self):
        self.assertEqual(self.user.email, 'test@example.com')

    def test_workout(self):
        self.assertEqual(str(self.workout), 'TestWorkout')

    def test_activity(self):
        self.assertEqual(self.activity.calories, 100)

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.score, 42)
