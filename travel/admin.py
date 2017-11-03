from django.contrib import admin
from .models import UserProfile, Location, Visit

admin.site.register(UserProfile)
admin.site.register(Location)
admin.site.register(Visit)
