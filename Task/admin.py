from django.contrib import admin
from models import Task
from News.models import News

class TaskAdmin(admin.ModelAdmin):
    list_display=('get_news_title','get_translator_name','time_translator','expiration_date','read')

    def get_translator_name(self,obj):
        return obj.translator_id.user_id.name + ' ' + obj.translator_id.user_id.family

    def get_news_title(self,obj):
        return obj.news_id.title

    get_news_title.short_description = 'Title'
    get_news_title.admin_order_field = 'news_id__title'
    get_translator_name.short_description = 'Translator'
    get_translator_name.admin_order_field = 'translator_id__user_id__name'

admin.site.register(Task, TaskAdmin)
