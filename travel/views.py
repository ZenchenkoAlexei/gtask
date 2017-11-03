from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User, Location, Visit
from .serializers import UserSerializer, LocationSerializer, VisitSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = IsAuthenticated
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LocationViewSet(viewsets.ModelViewSet):
    permission_classes = IsAuthenticated
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class VisitViewSet(viewsets.ModelViewSet):
    permission_classes = IsAuthenticated
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
