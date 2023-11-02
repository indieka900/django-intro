from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    image = models.ImageField(upload_to='students', default='profile.png')
    
    def __str__(self):
        return self.name
    
    
class Sliders(models.Model):
    text1 = models.CharField(max_length=100)
    text2 = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sliders', default='profile.png')
    
    def __str__(self):
        return self.text1

# Create your models here.
