from django.contrib import admin

from startthedark.events.models import Event, Attendance

admin.site.register(Event)
admin.site.register(Attendance)
