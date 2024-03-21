from django.contrib import admin
from .models import User, APIKey

admin.site.register(User)
admin.site.register(APIKey)

# Register your models here.
