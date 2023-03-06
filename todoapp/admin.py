from django.contrib import admin


from todoapp.models import TodoList

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display=('user','name', 'date')


admin.site.register(TodoList,TodoAdmin)