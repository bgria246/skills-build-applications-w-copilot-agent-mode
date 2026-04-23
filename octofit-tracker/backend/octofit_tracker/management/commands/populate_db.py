from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Törlés
        get_user_model().objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Csapatok
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Felhasználók
        User = get_user_model()
        tony = User.objects.create_user(username='ironman', email='tony@marvel.com', password='password', team=marvel)
        steve = User.objects.create_user(username='captain', email='steve@marvel.com', password='password', team=marvel)
        bruce = User.objects.create_user(username='batman', email='bruce@dc.com', password='password', team=dc)
        clark = User.objects.create_user(username='superman', email='clark@dc.com', password='password', team=dc)

        # Edzések
        w1 = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        w2 = Workout.objects.create(name='Running', description='Run 5km')

        # Aktivitások
        Activity.objects.create(user=tony, workout=w1, duration=10, calories=50)
        Activity.objects.create(user=steve, workout=w2, duration=30, calories=200)
        Activity.objects.create(user=bruce, workout=w1, duration=15, calories=60)
        Activity.objects.create(user=clark, workout=w2, duration=25, calories=180)

        # Leaderboard
        Leaderboard.objects.create(user=tony, score=100)
        Leaderboard.objects.create(user=steve, score=90)
        Leaderboard.objects.create(user=bruce, score=95)
        Leaderboard.objects.create(user=clark, score=98)

        self.stdout.write(self.style.SUCCESS('Test adatok feltöltve!'))
