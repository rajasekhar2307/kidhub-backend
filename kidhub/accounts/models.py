from django.db import models
from django.contrib.auth.models import AbstractUser

USER_CHOICES = [
  ('A', 'Admin'),
  ('T', 'Teacher'),
  ('S', 'Student')
]

# Create your models here.
class User(AbstractUser):
  email = models.EmailField(unique= True)
  user_type = models.CharField(max_length=1, choices=USER_CHOICES)

class Teacher(models.Model):
  phone = models.CharField(max_length=255)
  birth_date = models.DateField(null=True)

  user = models.OneToOneField(User, on_delete= models.CASCADE)


class Student(models.Model):

  CLASS_CHOICES = [
    ('NUR', 'Kinder Garten'),
    ('LKG', 'Lower Kinder Garten'),
    ('UKG', 'Upper Kinder Garten'),
    ('I', 'First'),
    ('II', 'Second'),
    ('III', 'Third'),
    ('IV', 'Fourth'),
    ('V', 'Fifth'),
    ('VI', 'Sixth'),
    ('VII', 'Seventh'),
    ('VIII', 'Eighth'),
    ('IX', 'Ninth'),
    ('X', 'Tenth'),
  ]

  DIV_CHOICES = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D')
  ]

  admission_number = models.BigIntegerField(unique=True)
  father_name = models.CharField(max_length=255)
  mother_name = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  phone = models.CharField(max_length=255)
  birth_date = models.DateField(null=True)
  class_year = models.CharField( max_length=4, choices= CLASS_CHOICES)
  div = models.CharField(max_length=1, choices=DIV_CHOICES)

  user = models.OneToOneField(User, on_delete= models.CASCADE)
