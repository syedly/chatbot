from django.contrib import admin
from app.models import CustomUser, Preferences
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Preferences)