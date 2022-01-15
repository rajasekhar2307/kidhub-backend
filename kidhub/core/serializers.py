from rest_framework import serializers
from .models import Attendance, Marks

class AttendanceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Attendance
    fields = ['date', 'student_id', 'status']


class MarksSerializer(serializers.ModelSerializer):
  class Meta:
    model = Marks
    fields = ['total_marks', 'max_marks', 'subject_name', 'student_id', 'exam_name']
class GetAttendanceSerializer(serializers.Serializer):
  present = serializers.IntegerField
  absent = serializers.IntegerField
