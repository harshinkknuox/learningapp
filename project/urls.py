from django.urls import path
from .api import ProjectsPagesViewSet

urlpatterns = [
    path('projects/', ProjectsPagesViewSet.as_view({'get': 'list'}), name='projects-list'),
     path('projects/<slug:slug>/detail/', ProjectsPagesViewSet.as_view({'get': 'retrieve'}), name='projects-detail'),
]