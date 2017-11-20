from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile, Location, Visit
from .serializers import UserSerializer, LocationSerializer, VisitSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer
from .models import UserProfile


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


class AuthRegister(APIView):
    """
    Register a new user.
    """
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)