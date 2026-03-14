
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Safely delete all objects
        for model in [Activity, Leaderboard, Workout, User, Team]:
            objs = model.objects.all()
            for obj in objs:
                if getattr(obj, 'id', None):
                    obj.delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', team=marvel)
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', team=dc)

        # Create activities
        Activity.objects.create(user=ironman, type='run', duration=30)
        Activity.objects.create(user=batman, type='cycle', duration=45)

        # Create workouts
        Workout.objects.create(user=ironman, description='Chest day')
        Workout.objects.create(user=superman, description='Leg day')

        # Create leaderboard
        Leaderboard.objects.create(user=ironman, points=100)
        Leaderboard.objects.create(user=batman, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
