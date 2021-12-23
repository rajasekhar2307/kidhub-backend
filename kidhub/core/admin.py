from django.contrib import admin

from core.models import Attendance, Marks

# Register your models here.
admin.site.register(Marks)

admin.site.register(Attendance)