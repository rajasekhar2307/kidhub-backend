from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import StudentViewSet, TeacherViewSet, UserViewSet

router = SimpleRouter()

router.register('students', StudentViewSet)
router.register('teachers', TeacherViewSet)
router.register('users', UserViewSet)


urlpatterns = router.urls