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


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

import datetime

from django.http import HttpResponse
import json

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm, UserProfileForm
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



# @login_required
# @transaction.atomic

@csrf_exempt
def create_user11(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)#, instance=request.user)
        user_profile_form = UserProfileForm(request.POST)#, instance=request.user.profile)
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            return HttpResponse("Added. Go fuck yourself.")
        else:
            return HttpResponse("NO! Go fuck yourself.")
    else:
        #user_form = UserForm(instance=request.user)
        #profile_form = UserProfileForm(instance=request.user.profile)
        return HttpResponse("Fail. FAIL! Go fuck yourself.")
#    return HttpResponse("Fail. Go fuck yourself.")

@csrf_exempt
def create_user11(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User created successfully!")
        return HttpResponse("Invalid")
    else:
        return HttpResponse("Not Post!")
@csrf_exempt
def create_user(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
           # if 'coutry' in request.body:
           #     profile.country = request.body['country']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            return HttpResponse("Error!")

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return HttpResponse("No luck!")