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

from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt

import datetime

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

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def detail_user(request, user_id):
    count_n = Visit.objects.filter(user_id_id=user_id).count()
    avg_n = Visit.objects.filter(user_id_id=user_id).aggregate(Avg('ratio'))
    list_n = Visit.objects.filter(user_id_id=user_id).values_list('location_id_id', flat=True).distinct()
    return JsonResponse({"count": count_n, 'avg': list(avg_n.values())[0], 'locations': list(list_n)})


def detail_location(request, location_id):
    count_n = Visit.objects.filter(location_id_id=location_id).count()
    avg_n = Visit.objects.filter(location_id_id=location_id).aggregate(Avg('ratio'))
    list_n = Visit.objects.filter(location_id_id=location_id).values_list('user_id_id', flat=True).distinct()
    return JsonResponse({"count": count_n, 'avg': list(avg_n.values())[0], 'users': list(list_n)})

#@csrf_protect
#@ensure_csrf_cookie
@csrf_exempt
def mark_visited(request, location_id):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    ratio_input = body['ratio']
    curent_id = request.user.id
    # if request.META.get('CONTENT_TYPE', '').lower() == 'application/json' and len(request.body) > 0:
    #     try:
    #         body_data = json.loads(request.body)
    #     except Exception as e:
    #         return HttpResponseBadRequest(json.dumps({'error': 'Invalid request: {0}'.format(str(e))}),
    #                                       content_type="application/json")
    v1 = Visit(date=datetime.datetime.now(), ratio=ratio_input, user_id_id=curent_id, location_id_id=location_id)
    v1.save()
    return HttpResponse("Added. Go fuck yourself." + str(datetime.datetime.now()))


