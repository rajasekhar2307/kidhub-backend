from django.db.models.fields.related import ManyToManyField
from django.shortcuts import render
from django.views.decorators import csrf
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from accounts.models import Student
from accounts.serializers import StudentSerializer
from accounts.models import User
from rest_framework import serializers
from rest_framework.views import APIView
from django.contrib.auth.decorators import user_passes_test

from core.serializers import GetAttendanceSerializer
from .models import Attendance, Marks

from core.serializers import AttendanceSerializer, MarksSerializer
from accounts.serializers import UserSerializer
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from accounts.permissions import IsStudent,IsTeacher


@api_view(['PUT'])
@csrf_exempt
@permission_classes([IsTeacher])
def update_studentp(request):
  if(request.method == 'PUT'):
    student = Student.objects.get(admission_number = request.data['admission_number'])
    print(student)
    serializer = StudentSerializer(student, data= request.data)
    serializer.is_valid(raise_exception= True)
    serializer.save()
    return Response(serializer.data)
  return Response("Not a valid method")

@api_view(['PUT'])
@csrf_exempt
@permission_classes([IsTeacher])
def update_studentu(request):
  if(request.method == 'PUT'):
    user = User.objects.get(id = request.data['id'])
    print(user)
    serializer = UserSerializer(user, data= request.data)
    serializer.is_valid(raise_exception= True)
    serializer.save()
    return Response(serializer.data)
  return Response("Not a valid method")


@api_view(['GET', 'POST'])
@csrf_exempt
@permission_classes([IsTeacher])
def get_studentp(request):
  if(request.method == 'POST'):
    admission_number = request.data['admission_number']
    queryset = Student.objects.filter(admission_number=admission_number)
    print(queryset)
    serializer = StudentSerializer
    if(len(queryset) == 0):
      return Response("Student not found")
    data = serializer(queryset[0])
    print(data.data)
    return Response(data.data)
    # return Response('ok')
  return Response("HEllo world")

@api_view(['GET', 'POST'])
@csrf_exempt
@permission_classes([IsTeacher])
def get_studentu(request):
  if(request.method == 'POST'):
    print(request.data)
    userid = request.data['userid']
    queryset = User.objects.all().filter(id = userid)
    serializer = UserSerializer
    data = serializer(queryset[0])
    return Response(data.data)
  return Response("HEllo world")


@api_view(['POST', 'GET'])
@csrf_exempt
@permission_classes([IsTeacher])
def get_data(request):
  if(request.method == 'POST'):
    class_year = request.data['classStudying']
    section = request.data['section']
    students = Student.objects.select_related('user').all().filter(class_year = class_year, div = section)
    serializer = StudentSerializer
    data = serializer(students, many=True)
    return Response(data.data)
  return Response("HEllo world")

@api_view(['POST'])
@csrf_exempt
@permission_classes([IsTeacher])
def post_attendance(request):
  if(request.method == 'POST'):
    print(request.data)
    for attendance in request.data:
      try:
        serializer = AttendanceSerializer(data = attendance)
        serializer.is_valid(raise_exception= True)
        serializer.save()
      except:
        return Response('Duplication')
    return Response('saved!')

@api_view(['POST'])
@csrf_exempt
@permission_classes([IsTeacher])
def post_marks(request):
  if(request.method == 'POST'):
    print(request.data['marks'])
    for mark in request.data['marks']:
      print(mark)
      try:
        serializer = MarksSerializer(data = mark)
        serializer.is_valid(raise_exception=True)
        serializer.save()
      except:
        return Response('Duplication')
    return Response('saved!')

@api_view(['GET', 'POST'])
@csrf_exempt
def get_attendance(request):
  if(request.method == 'POST'):
    print(request.data)
    admission_number = request.data['admission_number']
    student = Student.objects.all().filter(admission_number = admission_number)
    attendance = Attendance.objects.all().filter(student_id = student[0].user.id)
    present,absent = 0,0 
    for i in attendance:
      if(i.status == 'P'):
        present+=1
      elif(i.status == 'A'):
        absent+=1
    return Response({"present":present,"absent":absent})
  
@api_view(['GET', 'POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_marks(request):
  if(request.method == 'POST'):
    SUBJECTS = {
      'FL': 'First Language',
    'SL': 'Second Language',
    'E': 'English',
    'M': 'Mathematics',
    'P': 'Physics',
    'B': 'Biology',
    'S': 'Social',
    }
    subject = request.data['subject']
    exam_type = request.data['exam_type']
    admission_number = request.data['admission_number']
    student = Student.objects.all().filter(admission_number = admission_number)
    if(subject == 'AL'):
      marks = Marks.objects.all().filter(exam_name = exam_type, student_id = student[0].user.id)
      marks_list = []
      for i in marks:
        d = {
          "admission_number": admission_number,
          "subject": SUBJECTS.get(i.subject_name),
          "total_marks": i.total_marks,
          "max_marks": i.max_marks
        }
        marks_list.append(d)
      return Response(marks_list)

    marks = Marks.objects.all().filter(exam_name = exam_type, student_id = student[0].user.id, subject_name = subject)
    print(marks[0].total_marks, marks[0].max_marks)
    return Response({"admission_number":admission_number, "subject":subject, "total_marks": marks[0].total_marks, "max_marks":marks[0].max_marks})
  return Response("OK")
  
