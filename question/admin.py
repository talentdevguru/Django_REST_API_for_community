from django.contrib import admin

# Register your models here.
from .models import Garden
from .models import Vegetable
admin.site.register(Garden)
admin.site.register(Vegetable)
