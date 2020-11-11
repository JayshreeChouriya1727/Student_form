from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=120)
    courses = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    desc = models .TextField(max_length=128)

