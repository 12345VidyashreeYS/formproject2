from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    place=models.CharField(max_length=40)
    email=models.EmailField()
    dob=models.DateField()