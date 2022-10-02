import imp
from django.contrib import admin
from users.models import Message, UserProfile


admin.site.register(Message)
admin.site.register(UserProfile)
