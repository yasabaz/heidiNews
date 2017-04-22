from django.db import models

class user(models.Model):
    name=models.CharField(max_length=30,blank=False)
    family_name=models.CharField(max_length=30,blank=False)
    username=models.CharField(max_length=20,blank=False)
    password=models.CharField(max_length=20,blank=False)
    date_register=models.DateTimeField(auto_now_add=True)

class Translator(models.Model):
    user_id=models.OneToOneField(user)
    skill=models.CharField(max_length=20)