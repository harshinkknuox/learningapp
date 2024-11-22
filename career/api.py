from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from wagtail.models import Locale
from django.utils.translation import get_language_from_request
from django.core.paginator import Paginator

from .models import CareerPage
from django.db.models import Q
from .serializers import CareerPageSerializer
from learningapp.constants import PAGINATION_PERPAGE


class CareerPagesViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        # Dictionary to map actions to their respective serializers
        group_serializer = {
            'list': CareerPageSerializer,
            
        }
        
        # Get the appropriate serializer based on the action
        serializer_class = group_serializer.get(self.action, None)
        
        if serializer_class is None:
            raise ValueError(f"No serializer found for action: {self.action}")
        return serializer_class
    
    def get_queryset(self):
        # Return the filtered queryset
        queryset = CareerPage.objects.live()
        return queryset

    def list(self, request, *args, **kwargs):
        response = {}
        try:
            limit = int(request.GET.get('limit', PAGINATION_PERPAGE))  # Ensure limit is an integer
            page = int(request.GET.get('page', 1))  # Ensure page is an integer
            
            querysets = self.get_queryset()

            paginator = Paginator(querysets, limit)
            records = paginator.get_page(page)
            
            # Determine pagination status
            has_next = records.has_next()
            has_previous = records.has_previous()      
            
            # Serialize the paginated records
            serializer = self.get_serializer(records, many=True, context={'request': request})
            
            # Prepare the response data
            response['result'] = 'success'
            response['records'] = serializer.data
            response['page_count'] = paginator.count
            response['has_next'] = has_next
            response['has_previous'] = has_previous
            response['pages'] = paginator.num_pages          
        except Exception as e:
            response['result'] = 'failure'
            response['message'] = str(e)    
        # Return the response with a 200 OK status
        return Response(response, status=status.HTTP_200_OK)
    
    