from django.urls import path
from .api import CoursePagesViewSet

urlpatterns = [
    path('courses/', CoursePagesViewSet.as_view({'get':'list'}), name='course-list'),
]