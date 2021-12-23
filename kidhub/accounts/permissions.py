from rest_framework import permissions

class IsTeacher(permissions.BasePermission):
  def has_permission(self, request, view):
      if(request.user and request.user.user_type == 'T'):
        return True
      return False