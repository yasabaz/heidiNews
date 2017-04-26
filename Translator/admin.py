from django.contrib import admin
from models import *

class userAdmin(admin.ModelAdmin):
    list_display=('name','family','username','date_register')


class TranslatorAdmin(admin.ModelAdmin):
    list_display=('get_user_name_family','skill')

    def get_user_name_family(self,obj):
        return obj.user_id.name + ' ' + obj.user_id.family

    get_user_name_family.short_description = 'Name'
    get_user_name_family.admin_order_field = 'user_id__name'


admin.site.register(user,userAdmin)
admin.site.register(Translator,TranslatorAdmin)
 
