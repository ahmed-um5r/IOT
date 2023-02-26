from django.db import models 
import datetime 


class Country(models.Model):
    name = models.CharField(max_length=255)      
    number_of_club = models.IntegerField()
    
class Post2(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.TimeField()


 