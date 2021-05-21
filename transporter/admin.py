from django.contrib import admin

# Register your models here.

from .models import Bus, Passengers, Bus_stops, Routes, Tickets, Schedules

admin.site.register(Bus)
admin.site.register(Passengers)
admin.site.register(Bus_stops)
admin.site.register(Routes)
admin.site.register(Tickets)
admin.site.register(Schedules)

