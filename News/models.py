from django.db import models

class Resource(models.Model):
    name=models.CharField(max_length=30)
    link=models.URLField()
    def __str__(self):
        return self.name,self.link
class Category(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class News(models.Model):
    title=models.CharField(max_length=200,blank=False)
    link=models.URLField(blank=False)
    read=models.BooleanField(auto_created=False,default=False)
    post_date=models.DateTimeField(blank=False)
    category=models.ManyToManyField(Category)

    def __str__(self):
        return self.title