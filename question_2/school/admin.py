from django.contrib import admin
from .models import Contact
from .models import Profile

# Register your models here.
# Registring Profile and Contact Models
admin.site.register(Profile)
admin.site.register(Contact)