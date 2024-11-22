from django.urls import path
from .api import BlogPagesViewSet


urlpatterns = [
    path('blogs/', BlogPagesViewSet.as_view({'get': 'list'}), name='projects-list'),
    path('blogs/<slug:slug>/detail/', BlogPagesViewSet.as_view({'get': 'retrieve'}), name='projects-detail'),
]