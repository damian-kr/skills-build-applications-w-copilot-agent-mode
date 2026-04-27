from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Usuń istniejące dane
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Tworzenie drużyn
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Tworzenie użytkowników
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', team=marvel)
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='pass', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='pass', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='pass', team=dc)

        # Tworzenie aktywności
        Activity.objects.create(user=ironman, type='run', duration=30, calories=300)
        Activity.objects.create(user=batman, type='cycle', duration=45, calories=400)

        # Tworzenie treningów
        Workout.objects.create(name='Full Body', description='Całościowy trening', difficulty='medium')
        Workout.objects.create(name='Cardio', description='Trening cardio', difficulty='easy')

        # Tworzenie leaderboard
        Leaderboard.objects.create(user=ironman, points=100)
        Leaderboard.objects.create(user=batman, points=120)

        self.stdout.write(self.style.SUCCESS('Baza danych octofit_db została wypełniona przykładowymi danymi.'))
