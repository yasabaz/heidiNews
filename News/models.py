from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name
class News(models.Model):
    title=models.CharField(max_length=200,blank=False)
    link=models.URLField(blank=False)
    post_date=models.DateTimeField(blank=False)
    category=models.ForeignKey(Category)