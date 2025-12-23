from django.core.management.base import BaseCommand
from octofit_tracker import models
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        # Robust deletion: filter only objects with a valid id
        for model in [models.Team, models.Activity, models.Leaderboard, models.Workout, models.User]:
            objs = model.objects.all()
            objs_with_id = [obj for obj in objs if getattr(obj, 'id', None)]
            if objs_with_id:
                model.objects.filter(id__in=[obj.id for obj in objs_with_id]).delete()

        # Create Teams
        marvel = models.Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = models.Team.objects.create(name='DC', description='DC superheroes')

        # Create Users (Superheroes)
        users = [
            {'email': 'tony@stark.com', 'name': 'IronMan', 'team': marvel.name},
            {'email': 'steve@rogers.com', 'name': 'CaptainAmerica', 'team': marvel.name},
            {'email': 'bruce@wayne.com', 'name': 'Batman', 'team': dc.name},
            {'email': 'clark@kent.com', 'name': 'Superman', 'team': dc.name},
        ]
        user_objs = []
        for u in users:
            user = models.User.objects.create(email=u['email'], name=u['name'], team=u['team'])
            user_objs.append(user)

        # Create Activities
        from datetime import date
        activities = [
            {'user': user_objs[0], 'type': 'Run', 'duration': 30, 'date': date.today()},
            {'user': user_objs[1], 'type': 'Swim', 'duration': 45, 'date': date.today()},
            {'user': user_objs[2], 'type': 'Bike', 'duration': 60, 'date': date.today()},
            {'user': user_objs[3], 'type': 'Yoga', 'duration': 20, 'date': date.today()},
        ]
        for a in activities:
            models.Activity.objects.create(**a)

        # Create Workouts
        workouts = [
            {'name': 'Hero HIIT', 'description': 'High intensity for heroes', 'suggested_for': 'All'},
            {'name': 'Power Yoga', 'description': 'Yoga for super strength', 'suggested_for': 'All'},
        ]
        for w in workouts:
            models.Workout.objects.create(**w)

        # Create Leaderboard
        for user in user_objs:
            models.Leaderboard.objects.create(user=user, score=100)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
