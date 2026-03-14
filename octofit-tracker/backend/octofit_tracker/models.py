from django.db import models
from djongo.models import ObjectIdField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = ObjectIdField(primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True)

class Team(models.Model):
    id = ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)

class Activity(models.Model):
    id = ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()

class Workout(models.Model):
    id = ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)

class Leaderboard(models.Model):
    id = ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    points = models.IntegerField()
