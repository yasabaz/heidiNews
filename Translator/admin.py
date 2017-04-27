from django.contrib import admin
from models import *
from django.contrib.auth.models import User
'''
class userAdmin(admin.ModelAdmin):
    list_display=('name','family','username','date_register')
'''

class TranslatorAdmin(admin.ModelAdmin):
    list_display=('user','skill')



#admin.site.register(user,userAdmin)
admin.site.register(Translator,TranslatorAdmin)
 
