from rest_framework import serializers
from .models import Student, Teacher
from djoser.serializers import UserSerializer as BaseUserSerializer
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

class UserSerializer(BaseUserSerializer):
  class Meta(BaseUserSerializer.Meta):
    fields = ['id', 'username', 'email', 'first_name', 'last_name', 'user_type']

class StudentSerializer(serializers.ModelSerializer):
  admission_number = serializers.IntegerField()
  class Meta:
    model = Student
    fields = ['admission_number', 'father_name', 'mother_name', 'address', 'phone', 'birth_date', 'class_year', 'div', 'user']

class TeacherSerializer(serializers.ModelSerializer):
  class Meta:
    model = Teacher
    fields = ['phone', 'birth_date']


class UserCreateSerializer(BaseUserCreateSerializer):
  class Meta(BaseUserCreateSerializer.Meta):
    fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']