from django.db.models.base import Model
from rest_framework.viewsets import ModelViewSet

from accounts.permissions import IsTeacher
from .models import Student, Teacher, User
from .serializers import StudentSerializer, TeacherSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated


# Create your views here.
class StudentViewSet(ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  permission_classes = [DjangoModelPermissions]

  # def get_permissions(self):
  #     if self.request.method == 'PUT':
  #       return [IsTeacher()]

  @action(detail=False, methods=['GET', 'PUT'])
  def me(self, request):
    (student, created) = Student.objects.get_or_create(user_id=request.user.id)
    if request.method == 'GET':
      serializer = StudentSerializer(student)
      return Response(serializer.data)
    elif request.method == 'PUT':
      serializer = StudentSerializer(student, data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)

class TeacherViewSet(ModelViewSet):
  queryset = Teacher.objects.all()
  serializer_class = TeacherSerializer
  permission_classes = [IsAuthenticated]

  @action(detail=False, methods=['PUT', 'GET'])
  def me(self, request):
    (teacher, created) = Teacher.objects.get_or_create(user_id=request.user.id)

    if request.method == 'GET':
      serializer = TeacherSerializer(teacher)
      return Response(serializer.data)
    elif request.method == 'PUT':
      serializer = TeacherSerializer(teacher, data=request.data)
      serializer.is_valid(raise_exception= True)
      serializer.save()
      return Response(serializer.data)

class UserViewSet(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsAuthenticated]

  @action(detail=False, methods=['GET', 'PUT'])
  def me(self, request):
    (user, created) = User.objects.get_or_create(id = request.user.id)
    

    if(request.method == 'GET'):
      serializer = UserSerializer(user)
      return Response(serializer.data)
    elif request.method == 'PUT':
      serializer = UserSerializer(user, data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)
