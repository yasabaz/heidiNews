from django.contrib import admin
from models import *
class userAdmin(admin.ModelAdmin):
    list_display=('name','family_name','username','date_register')
class TranslatorAdmin(admin.ModelAdmin):
    list_display=('user_id','skill')
admin.site.register(user,userAdmin)
admin.site.register(Translator,TranslatorAdmin)
 