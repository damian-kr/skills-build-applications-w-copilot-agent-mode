from django.db import models
from django.contrib.auth.models import AbstractUser


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='members')


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=50)
    duration = models.PositiveIntegerField()  # minuty
    calories = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=20)
    suggested_for = models.ManyToManyField(User, blank=True, related_name='suggested_workouts')


class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
    points = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
