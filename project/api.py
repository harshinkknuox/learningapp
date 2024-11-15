from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from wagtail.models import Locale
from django.utils.translation import get_language_from_request
from django.core.paginator import Paginator

from .models import ProjectsPage
from django.db.models import Q
from .serializers import ProjectsPageSerializer,ProjectsDetailSerializer
from learningapp.constants import PAGINATION_PERPAGE



class ProjectsPagesViewSet(viewsets.ModelViewSet):
    # serializer_class = ProjectsPageSerializer

    #seralizer class for actions
    def get_serializer_class(self):
        # Dictionary to map actions to their respective serializers
        group_serializer = {
            'list': ProjectsPageSerializer,
            'retrieve': ProjectsDetailSerializer,
        }
        
        # Get the appropriate serializer based on the action
        serializer_class = group_serializer.get(self.action, None)
        
        if serializer_class is None:
            raise ValueError(f"No serializer found for action: {self.action}")
        return serializer_class
        
    def get_queryset(self):
        # Retrieve the language from the request
        lang = get_language_from_request(self.request)
        # Get the locale object or raise a 404 error if not found
        locale = get_object_or_404(Locale, language_code=lang)
        
        # Return the filtered queryset
        return ProjectsPage.objects.live().exact_type(ProjectsPage).filter(locale=locale)


    #lists all market updates with pagination and filtering by category
    def list(self, request, *args, **kwargs):
        response = {}
        try:
            limit = int(request.GET.get('limit', PAGINATION_PERPAGE))  # Ensure limit is an integer
            page = int(request.GET.get('page', 1))  # Ensure page is an integer
            search_term = request.GET.get('search_term', None)
            project_name = request.GET.get('project_name', None) # To get project name
            communities = request.GET.get('communities', None) # To get communities name
            querysets = self.get_queryset()
              
            if project_name:
                querysets = querysets.filter(project_name__icontains=project_name)
            if communities:
                querysets = querysets.filter(communities__icontains=communities)
            if search_term:
                querysets = querysets.filter(Q(project_name__icontains=search_term) | Q(project_description__icontains=search_term))

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
    
    def retrieve(self, request, *args, **kwargs):
        response = {}
        try:
        
            # Extract slug from URL parameters
            slug = kwargs.get('slug')
            
            # Get language from the request and fetch corresponding Locale object
            lang = get_language_from_request(request)
            locale = get_object_or_404(Locale, language_code=lang)
            
            # Create a queryset for ProjectPAge filtered by locale and live pages
            queryset = ProjectsPage.objects.live().filter(locale=locale)
            
            # Fetch the specific ProjectPAge using slug, raising a 404 if not found
            projects_page = get_object_or_404(queryset, slug=slug)
            
            # Serialize the retrieved ProjectPAge
            serializer = self.get_serializer(projects_page)
            print("==--queryset-serializer--==",serializer.data)
            # Prepare the response data
            response['result'] = 'success'
            response['records'] = serializer.data
        except Exception as e:
            response['result'] = 'failure'
            response['message'] = str(e)
        # Return the response with a 200 OK status
        return Response(response, status=status.HTTP_200_OK)