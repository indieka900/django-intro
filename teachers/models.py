from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    image = models.ImageField(upload_to='students', default='profile.png')

# Create your models here.
