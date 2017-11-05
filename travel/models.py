from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # user = models.OneToOneField(User, blank=True, default=None)
    username = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=(('M', 'M'), ('F', 'F'), ('N', 'N')), default=None)
    birth_day = models.DateField(default=date.today, blank=True)
    country = models.CharField(max_length=50, blank=True)


class Location(models.Model):
    id = models.AutoField
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    name = models.CharField(primary_key=True, max_length=50)
    description = models.TextField(max_length=250)


class Visit(models.Model):
    CHOICES = [(i, i) for i in range(11)]
    # user_id = models.OneToOneField(UserProfile, null=True, blank=True)
    location_id = models.ForeignKey(Location, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    ratio = models.IntegerField(choices=CHOICES)
