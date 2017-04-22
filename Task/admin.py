from django.contrib import admin
from models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display=('translator_id','news_id','time_translator','expiration_date')

admin.site.register(Task,TaskAdmin)