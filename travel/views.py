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
from django.db.models import Avg
from .serializers import UserSerializer
from .models import UserProfile
from django.http import JsonResponse

from django.http import HttpResponse
import json

from django.views.decorators.http import require_http_methods


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

#@require_http_methods(["GET", "POST", "HEAD", "OPTIONS", "DETAILS"])
class LocationViewSet(viewsets.ModelViewSet):
   # permission_classes = (IsAuthenticated,)
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class VisitViewSet(viewsets.ModelViewSet):
   # permission_classes = (IsAuthenticated,)
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

def detail(request, question_id):
    count_n = Visit.objects.filter(user_id_id= question_id).count()
    avg_n = Visit.objects.filter(user_id_id= question_id).aggregate(Avg('ratio'))
    list_n = Visit.objects.filter(user_id_id=question_id).values_list('location_id_id', flat=True).distinct()
    return JsonResponse({"count" : count_n, 'avg': list(avg_n.values())[0], 'locations' : list(list_n)})


