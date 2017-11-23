from rest_framework import viewsets, generics
from .models import Location, Visit
from .serializers import LocationSerializer, VisitSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.db.models import Avg
from .serializers import UserSerializer
from .models import UserProfile
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate
import datetime
import json
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import UserForm, UserProfileForm
from rest_framework.permissions import IsAuthenticated


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class LocationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class VisitViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer


class AuthRegister(APIView):
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


@csrf_exempt
def mark_visited(request, location_id):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    ratio_input = body['ratio']
    curent_id = request.user.id
    v1 = Visit(date=datetime.datetime.now(), ratio=ratio_input, user_id_id=curent_id, location_id_id=location_id)
    v1.save()
    return HttpResponse("Added." + str(datetime.datetime.now()))


@csrf_exempt
def create_user(request):

    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            return HttpResponse("Error!")
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return HttpResponse("Success!")


@csrf_exempt
def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            return HttpResponse("Wrong Creds")
    else:
        pass
