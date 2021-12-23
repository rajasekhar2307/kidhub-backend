from rest_framework import serializers
from .models import Attendance, Marks

class AttendanceSerializer(serializers.Serializer):
  class Meta:
    model = Attendance
    fields = ['date', 'student_id', 'status']

class Marks(serializers.Serializer):
  class Meta:
    model = Marks
    fields = ['total_marks', 'max_marks', 'subject_name', 'student_id']