from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from wagtail.models import Locale
from django.utils.translation import get_language_from_request
from django.core.paginator import Paginator

from .models import CoursePage
from .serializers import CoursePageSerializer
from learningapp.constants import PAGINATION_PERPAGE


class CoursePagesViewSet(viewsets.ModelViewSet):
    
    def get_serializer_class(self):
        group_serializer ={
            'list':CoursePageSerializer
        }

        serializer_class = group_serializer.get(self.action,None)

        if serializer_class is None:
            raise ValueError(f"No serializer found for action: {self.action}")
        return serializer_class
    
    def get_queryset(self):
        queryset = CoursePage.objects.live().exact_type(CoursePage)
        return queryset
    
    def list(self,request,*args, **kwargs):
        response = {}
        try:
            records = self.get_queryset()
            serializer = self.get_serializer(records, many=True, context={'request':request})
            response['result'] = 'success'
            response['records'] = serializer.data
        except Exception as e:
            response['result'] = 'failure'
            response['message'] = str(e)
        return Response(response, status=status.HTTP_200_OK)