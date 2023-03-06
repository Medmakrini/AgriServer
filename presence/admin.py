from django.contrib import admin

from presence.models import PresenceDate


# Register your models here.

class Presenceadmin(admin.ModelAdmin):
    list_display=('worker','date','hoursofWork')


admin.site.register(PresenceDate,Presenceadmin)