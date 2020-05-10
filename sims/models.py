from django.db import models


# Create your models here.
class Student(models.Model):
    student_no = models.CharField(max_length=32, unique=True)
    student_name = models.CharField(max_length=32)
