from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from accounts.models import User
from accounts.models import Student, Teacher


# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
  add_fieldsets = (
    (None, {
      'classes' : ('wide',),
      'fields' : ('username', 'password1', 'password2', 'email', 'first_name', 'last_name'),
    }),
  )

admin.site.register(Student)

admin.site.register(Teacher)