from wagtail.admin.viewsets.pages import PageListingViewSet
from wagtail.admin.views.pages.create import CreateView
from wagtail.admin.views.pages.edit import EditView
from django.urls import path
from wagtail import hooks
from wagtail.admin.ui.tables import Column

from .models import CoursePage


class CoursePageCreateview(CreateView):
    model = CoursePage
class CoursePageEditView(EditView):
    model = CoursePage

class CoursePageViewSet(PageListingViewSet):
    model = CoursePage
    icon = "grip"
    menu_label = 'Courses'
    menu_order = 205
    exclude_from_explorer = False
    add_to_admin_menu = True
    list_display = ('course_name')  
    search_fields = ('course_name')  
    columns = PageListingViewSet.columns + [
        Column("locale", label="Locale", sort_key="locale"), 
    ]

    create_view_class = CoursePageCreateview
    edit_view_class = CoursePageEditView
    
    def get_urlpatterns(self):
        urlpatterns = super().get_urlpatterns()
        return urlpatterns + [
            path('create/', self.create_view_class.as_view(), name='create'),  
            path('<int:page_id>/edit/', self.edit_view_class.as_view(), name='edit'),  
        ]


@hooks.register('register_admin_viewset')
def register_course_page_viewset():
    return CoursePageViewSet('course_page')