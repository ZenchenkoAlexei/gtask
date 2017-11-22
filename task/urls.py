"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from travel.views import UserViewSet, LocationViewSet, VisitViewSet, AuthRegister, detail_user, detail_location, mark_visited
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.contrib.auth import views as auth_views
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'visits', VisitViewSet)

urlpatterns = [
    url(r'^users/(?P<user_id>[0-9]+)/ratio$', detail_user, name='detail_user'),
    url(r'^locations/(?P<location_id>[0-9]+)/ratio$', detail_location, name='detail_location'),
    url(r'^locations/(?P<location_id>[0-9]+)/visit$', mark_visited, name='mark_visited'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^sign_in_jwt/', obtain_jwt_token),
    url(r'^token-refresh/', refresh_jwt_token),
    url(r'^token-verify/', verify_jwt_token),
    url(r'^register/$', AuthRegister.as_view()),
    url(r'^sign_in/', include('rest_framework.urls', namespace='rest_framework')),
 #   url(r'^sing_in2/$', include('django.contrib.auth.views')),
    url(r'^', include(router.urls))
]
