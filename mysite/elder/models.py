from django.db import models

# Create your models here.
class Elder(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    def __str__(self):
        return self.name

class Family(models.Model):
    name = models.CharField(max_length=30)
    line = models.CharField(max_length=30)
    elder = models.ForeignKey(Elder)
    def __str__(self):
        return self.name

class Gesture(models.Model):
    name = models.CharField(max_length=30, blank=True)
    video = models.FileField(upload_to='upload/')
    elder = models.ForeignKey(Elder)
    
    
