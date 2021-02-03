from django.contrib import admin
from .models import *

# Register your models here.

class taskadmin(admin.ModelAdmin):
    list_display = ['title','complete','created']

admin.site.register(Task, taskadmin)
