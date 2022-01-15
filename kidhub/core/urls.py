from django.urls import include, path
from . import views

urlpatterns = [
  path('getdetails/', views.get_data, name='get-details'),
  path('getmarks/', views.get_marks, name='get-details'),
  path('getattendance/', views.get_attendance, name='get-details'),
  path('getdetails/stuu/', views.get_studentu, name='get-details'),
  path('uptdetails/stup/', views.update_studentp, name='get-details'),
  path('getdetails/stup/', views.get_studentp, name='get-details'),
  path('uptdetails/stuu/', views.update_studentu, name='get-details'),
  path('postattendance/', views.post_attendance , name='post-attendance'),
  path('postmarks/', views.post_marks , name='post-marks'),
]