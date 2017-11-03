from django.contrib import admin
from .models import User, Location, Visit

admin.site.register(User)
admin.site.register(Location)
admin.site.register(Visit)
