from django.db import models

from accounts.models import Student, User

# Create your models here.
class Attendance(models.Model):
  date = models.DateField()
  student_id = models.ForeignKey(User, on_delete=models.CASCADE)
  status = models.CharField(max_length=2, choices= [('AB', 'Absent'), ('P', 'Present')], default='AB')

  class Meta:
    unique_together = ["date", "student_id"]

  def __str__(self) -> str:
      return f'Attendance on {self.date}'

class Marks(models.Model):

  class Meta:
    unique_together = ['exam_name', 'max_marks', 'student_id', 'subject_name']

  EXAM_CHOICES = [
    ('Q', 'Quarterly Examination'),
    ('H', 'Half Yearly Examination'),
    ('A', 'Annual Examination')
  ]

  SUBJECT_CHOICES = [
    ('FL', 'First Language'),
    ('SL', 'Second Language'),
    ('E', 'English'),
    ('M', 'Mathematics'),
    ('P', 'Physics'),
    ('B', 'Biology'),
    ('S', 'Social'),
  ]

  exam_name = models.CharField(max_length= 1, choices=EXAM_CHOICES)
  max_marks = models.PositiveSmallIntegerField()
  student_id = models.ForeignKey(User, on_delete=models.CASCADE)
  total_marks = models.SmallIntegerField()
  subject_name = models.CharField(max_length=2, choices=SUBJECT_CHOICES)
