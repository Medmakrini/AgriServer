from django.contrib import admin

from location.models import Location

# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    list_display=('latitude','longitude','farm')


admin.site.register(Location,LocationAdmin)