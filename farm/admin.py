from django.contrib import admin

from  farm.models import Farm

# Register your models here.

class FarmAdmin(admin.ModelAdmin):
    list_display=('name','id','owner','work')


admin.site.register(Farm,FarmAdmin)