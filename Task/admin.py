from django.contrib import admin
from models import Task
from News.models import News

class TaskAdmin(admin.ModelAdmin):
    list_display=('get_news_title','translator_id','news_id','time_translator','expiration_date')

    def get_news_title(self,obj):
        return obj.news_id.title

admin.site.register(Task, TaskAdmin)
