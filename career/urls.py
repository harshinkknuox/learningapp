from django.urls import path
from .api import CareerPagesViewSet


urlpatterns = [
    path('careers/', CareerPagesViewSet.as_view({'get': 'list'}), name='career-list'),
    
]