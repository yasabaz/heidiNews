from django.db import models
from django.contrib.auth.models import User

class Translator(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    skill=models.CharField(max_length=25)

    def __str__(self):
        return self.user.username
