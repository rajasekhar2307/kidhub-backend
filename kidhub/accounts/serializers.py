from rest_framework import serializers
from .models import Student, Teacher
from djoser.serializers import UserSerializer as BaseUserSerializer

class UserSerializer(BaseUserSerializer):
  class Meta(BaseUserSerializer.Meta):
    fields = ['id', 'username', 'email', 'first_name', 'last_name']


class StudentSerializer(serializers.ModelSerializer):
  admission_number = serializers.IntegerField(read_only = True)
  class Meta:
    model = Student
    fields = ['admission_number', 'father_name', 'mother_name', 'address', 'phone', 'birth_date', 'class_year', 'div']

class TeacherSerializer(serializers.ModelSerializer):
  class Meta:
    model = Teacher
    fields = ['phone', 'birth_date']
