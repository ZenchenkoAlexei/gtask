from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=50)
    email = models.EmailField
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=(('M', 'M'), ('F', 'F')), default=None)
    birth_day = models.DateField
    country = models.CharField(max_length=50)


class Location(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)


class Visit(models.Model):
    CHOICES = [(i, i) for i in range(11)]
    id = models.AutoField(primary_key=True, unique=True)
    user_id = models.OneToOneField(User)
    location_id = models.OneToOneField(Location)
    date = models.DateField
    ratio = models.IntegerField(choices=CHOICES)
