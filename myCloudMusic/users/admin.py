import imp
from django.contrib import admin
from users.models import Message, Profile


admin.site.register(Message)
admin.site.register(Profile)
