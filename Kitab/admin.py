from django.contrib import admin

from Kitab.models import Booking, kitab

# Register your models here.
admin.site.register(kitab)
admin.site.register(Booking)