from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile, Location, Visit
from .serializers import UserSerializer, LocationSerializer, VisitSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = IsAuthenticated
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class LocationViewSet(viewsets.ModelViewSet):
    # permission_classes = IsAuthenticated
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class VisitViewSet(viewsets.ModelViewSet):
    # permission_classes = IsAuthenticated
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
