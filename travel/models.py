from django.db import models
from datetime import date
from django.utils import timezone
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model


class User(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(blank=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=(('M', 'M'), ('F', 'F'), ('N', 'N')), default=None)
    birth_day = models.DateField(default=date.today, blank=True)
    country = models.CharField(max_length=50, blank=True)


class Location(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=50, primary_key=True)
    description = models.TextField(max_length=250)


class Visit(models.Model):
    CHOICES = [(i, i) for i in range(11)]
    id = models.AutoField(primary_key=True, unique=True)
    user_id = models.ForeignKey(User)
    location_id = models.ForeignKey(Location)
    date = models.DateTimeField(default=timezone.now)
    ratio = models.IntegerField(choices=CHOICES)
