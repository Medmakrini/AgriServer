from django.contrib import admin

from worker.models import Worker


# Register your models here.

class Workeradmin(admin.ModelAdmin):
    list_display=('farm','id','startWork','firstName','workField')


admin.site.register(Worker,Workeradmin)