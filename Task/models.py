from django.db import models
from News.models import News
from Translator.models import Translator

import os
def path():
    return os.path

class Task(models.Model):
    translator_id=models.ForeignKey(Translator)
    news_id=models.OneToOneField(News)
    time_translator=models.DateTimeField(auto_now_add=True)
    upload=models.FileField(upload_to='article/%Y/%m/%d/',blank=False,default=path)#to do 
    expiration_date=models.DateTimeField(blank=False)
