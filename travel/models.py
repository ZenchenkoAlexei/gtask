from django.conf import settings
from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    username = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=(('M', 'M'), ('F', 'F'), ('N', 'N')), default='N')
    birth_day = models.DateField(default=date.today, blank=True)
    country = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.username


class Location(models.Model):

    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=50, primary_key=False)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name


class Visit(models.Model):
    CHOICES = [(i, i) for i in range(11)]
    # location = models.ForeignKey(Location, blank=False, default='1')
    # user = models.ManyToManyField(User, default=User.is_active)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE,)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE, default='')
    date = models.DateTimeField(default=timezone.now)
    ratio = models.IntegerField(choices=CHOICES)


    def __str__(self):
        return 'visit id: ' + str(self.id)
