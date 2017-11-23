from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save




class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    username = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=(('M', 'M'), ('F', 'F'), ('N', 'N')), default='N')
    birth_day = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user



class Location(models.Model):

    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name


class Visit(models.Model):
    CHOICES = [(i, i) for i in range(11)]
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE,)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    ratio = models.IntegerField(choices=CHOICES)

    def __str__(self):
        return 'visit id: ' + str(self.id)

