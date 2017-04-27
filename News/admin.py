from django.contrib import admin
from models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','link','post_date','get_display_category')
    def get_display_category(self,obj):
        return ' , '.join([category.name for category in obj.category.all()])
    get_display_category.short_description="category"
    get_display_category.allow_tags=True

admin.site.register(News,NewsAdmin)
admin.site.register(Category)
admin.site.register(Resource)