from django.db import models
from News.models import News
from Translator.models import Translator
from django.core.exceptions import ValidationError
import os

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx', ]
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')

def path():
    return os.path

class Task(models.Model):
    translator_id=models.ForeignKey(Translator)
    news_id=models.OneToOneField(News)
    time_translator=models.DateTimeField(auto_now_add=True)
    upload=models.FileField(upload_to='article/%Y/%m/%d/',blank=False,default=path, validators=[validate_file_extension])#to do 
    expiration_date=models.DateTimeField(blank=False)
    
    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)

