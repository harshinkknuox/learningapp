from wagtail.admin.viewsets.pages import PageListingViewSet
from wagtail.admin.views.pages.create import CreateView
from wagtail.admin.views.pages.edit import EditView
from django.urls import path
from wagtail import hooks
from wagtail.admin.ui.tables import Column

from .models import ProjectsPage  

class ProjectsPageCreateView(CreateView):
    model = ProjectsPage
class ProjectsPageEditView(EditView):
    model = ProjectsPage

class ProjectsPageViewSet(PageListingViewSet):
    model = ProjectsPage
    icon = 'tag'  
    menu_label = 'Projects'
    menu_order = 204  
    add_to_settings_menu = False
    exclude_from_explorer = False
    add_to_admin_menu = True
    list_display = ('project_name')  
    search_fields = ('project_name')  
    columns = PageListingViewSet.columns + [
        Column("locale", label="Locale", sort_key="locale"), 
    ]

    create_view_class = ProjectsPageCreateView
    edit_view_class = ProjectsPageEditView

    def get_urlpatterns(self):
        urlpatterns = super().get_urlpatterns()
        return urlpatterns + [
            path('create/', self.create_view_class.as_view(), name='create'),  
            path('<int:page_id>/edit/', self.edit_view_class.as_view(), name='edit'),  
        ]

@hooks.register('register_admin_viewset')
def register_product_category_viewset():
    return ProjectsPageViewSet('project_page')
