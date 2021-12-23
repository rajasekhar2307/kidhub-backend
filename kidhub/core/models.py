from django.db import models

from accounts.models import Student, User

# Create your models here.
class Attendance(models.Model):
  date = models.DateField()
  student_id = models.ForeignKey(User, on_delete=models.CASCADE)
  status = models.CharField(max_length=2, choices= [('AB', 'Absent'), ('P', 'Present')], default='AB')

  def __str__(self) -> str:
      return f'Attendance on {self.date}'

class Marks(models.Model):
  max_marks = models.PositiveSmallIntegerField()
  student_id = models.ForeignKey(User, on_delete=models.CASCADE)
  total_marks = models.SmallIntegerField()
  subject_name = models.CharField(max_length=255)




