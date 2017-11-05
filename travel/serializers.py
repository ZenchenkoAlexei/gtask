from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import UserProfile, Location, Visit


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'first_name', 'last_name', 'email', 'gender', 'birth_day', 'country')


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('country', 'city', 'name', 'description')


class VisitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visit
        fields = ('location_id', 'date', 'ratio')   # 'user_id',
