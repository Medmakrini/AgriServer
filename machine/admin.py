from django.contrib import admin

from machine.models import Machine

# Register your models here.

class MachineAdmin(admin.ModelAdmin):
    list_display=('name','id','farm')


admin.site.register(Machine,MachineAdmin)