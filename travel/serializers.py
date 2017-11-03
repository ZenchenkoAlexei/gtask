from rest_framework import serializers

from .models import UserProfile, Location, Visit


class UserSerializer(serializers.ModelSerializer):
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
        fields = ('user_id', 'location_id', 'date', 'ratio')
