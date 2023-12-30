'''from django.db import models

# Create your models here.
class Activity(models.Model):  
    activityname = models.CharField(max_lengt=100)
    activityinfo = models.CharField(max_length=500)
    activityspot = models.CharField(max_length=255)
    activitylink = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.activityspot} {self.activityname}"  '''