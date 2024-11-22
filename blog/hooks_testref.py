# Import necessary modules from Wagtail and Django
from wagtail.admin.viewsets.pages import PageListingViewSet
from wagtail.admin.views.pages.create import CreateView
from wagtail.admin.views.pages.edit import EditView
from django.urls import path
from wagtail import hooks
from wagtail.admin.viewsets.base import ViewSetGroup
from django.utils.translation import gettext_lazy as _
from wagtail.admin.ui.tables import Column
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.snippets.models import register_snippet

# Importing models used in different ViewSets
from .models import BlogPage
from market_updates.models import MarketUpdatePage, MarketCategory
from technical_analysis.models import TechnicalAnalysisPage, AnalysisCategory
from webinar.models import WebinarPage
from workshop.models import WorkshopPage
from economic_reports.models import EconomicReportPage, ReportCategory
from press_release.models import PressReleasePage
from activities.models import ActivityPage
from awards.models import AwardPage

# Custom Create and Edit Views for BlogPage
class BlogPageCreateView(CreateView):
    pass

class BlogPageEditView(EditView):
    pass

# ViewSet for managing Blog Pages in the Wagtail admin interface
class BlogPageViewSet(PageListingViewSet):
    model = BlogPage  # Model associated with this ViewSet
    icon = 'globe'  # Icon for the menu
    menu_label = 'Blog Pages'  # Label in the admin menu
    menu_order = 10  # Order in the admin menu
    add_to_settings_menu = False  # Do not add to settings menu
    exclude_from_explorer = False  # Include in the explorer
    list_display = ('title', 'status_string')  # Fields to display in the list
    search_fields = ('title',)  # Fields for the search functionality
    name = 'blogs_pages'  # Unique name for the ViewSet
    columns = PageListingViewSet.columns + [
        Column("locale", label="Locale", sort_key="locale"),  # Custom column for locale
    ]

    create_view_class = BlogPageCreateView  # Custom create view
    edit_view_class = BlogPageEditView  # Custom edit view

    # Method to define additional URL patterns for creating and editing pages
    def get_urlpatterns(self):
        urlpatterns = super().get_urlpatterns()  # Get the default patterns
        return urlpatterns + [
            path('create/', self.create_view_class, name='create-blog'),  # URL for creating a blog page
            path('<int:page_id>/edit/', self.edit_view_class, name='edit-blog'),  # URL for editing a blog page
        ]

# Custom Create and Edit Views for MarketUpdatePageCreateView
class MarketUpdatePageCreateView(CreateView):
    pass

class MarketUpdatePageEditView(EditView):
    pass

class MarketUpdatePageViewSet(PageListingViewSet):
    model = MarketUpdatePage # Model associated with this ViewSet
    icon = 'globe' # Icon for the menu
    menu_label = 'Market Updates' # Label in the admin menu
    menu_order = 20 # Order in the admin menu
    add_to_settings_menu = False # Do not add to settings menu
    exclude_from_explorer = False # Include in the explorer
    list_display = ('title', 'status_string')  # Fields to display in the list
    search_fields = ('title',) # Fields for the search functionality
    name = 'update_pages'  # Unique name for the ViewSet
    columns = PageListingViewSet.columns + [
        Column("locale", label="Locale", sort_key="locale"), # Custom column for locale
    ]

    create_view_class = MarketUpdatePageCreateView # Custom create view
    edit_view_class = MarketUpdatePageEditView # Custom edit view

    # Method to define additional URL patterns for creating and editing pages
    def get_urlpatterns(self):
        urlpatterns = super().get_urlpatterns() # Get the default patterns
        return urlpatterns + [
            path('create/', self.create_view_class, name='create-update'), # URL for creating a market page
            path('<int:page_id>/edit/', self.edit_view_class, name='edit-update'),  # URL for editing a market page
        ]

# Custom Create and Edit Views for MarketUpdatePageCreateView
class TechnicalAnalysisPageCreateView(CreateView):
    pass

class TechnicalAnalysisPageEditView(EditView):
    pass

class TechnicalAnalysisPageViewSet(PageListingViewSet):
    model = TechnicalAnalysisPage # Model associated with this ViewSet
    icon = 'globe' # Icon for the menu
    menu_label = 'Technical Analysis' # Label in the admin menu
    menu_order = 30 # Order in the admin menu
    add_to_settings_menu = False # Do not add to settings menu
    exclude_from_explorer = False # Include in the explorer
    list_display = ('title', 'status_string')  # Fields to display in the list
    search_fields = ('title',) # Fields for the search functionality
    name = 'analysis_pages'  # Unique name for the ViewSet
    columns = PageListingViewSet.columns + [
        Column("locale", label="Locale", sort_key="locale"), # Custom column for locale
    ]

    create_view_class = TechnicalAnalysisPageCreateView # Custom create view
    edit_view_class = TechnicalAnalysisPageEditView # Custom edit view

    # Method to define additional URL patterns for creating and editing pages
    def get_urlpatterns(self):
        urlpatterns = super().get_urlpatterns() # Get the default patterns
        return urlpatterns + [
            path('create/', self.create_view_class, name='create-analysis'), # URL for creating a analysis page
            path('<int:page_id>/edit/', self.edit_view_class, name='edit-analysis'), # URL for editing
        ]

# Custom Create and Edit Views for MarketUpdatePageCreateView
class EconomicReportsPageCreateView(CreateView):
    pass

class EconomicReportsEditView(EditView):
    pass

class EconomicReportsViewSet(PageListingViewSet):
    model = EconomicReportPage # Model associated with this ViewSet
    icon = 'globe' # Icon for the menu
    menu_label = 'Economic Reports' # Label in the admin menu
    menu_order = 40 # Order in the admin menu
    add_to_settings_menu = False # Do not add to settings menu
    exclude_from_explorer = False # Include in the explorer
    list_display = ('title', 'status_string')  # Fields to display in the list
    search_fields = ('title',) # Fields for the search functionality
    name = 'economic_pages'  # Unique name for the ViewSet
    columns = PageListingViewSet.columns + [
        Column("locale", label="Locale", sort_key="locale"), # Custom column for locale
    ]

    create_view_class = EconomicReportsPageCreateView # Custom create view
    edit_view_class = EconomicReportsEditView # custom edit view

    # Method to define additional URL patterns for creating and editing pages
    def get_urlpatterns(self):
        urlpatterns = super().get_urlpatterns() # Get the default patterns
        return urlpatterns + [
            path('create/', self.create_view_class, name='create-update'), # URL for creating a economic page
            path('<int:page_id>/edit/', self.edit_view_class, name='edit-update'), # URL for editing a economic page
        ]

 # Custom Create and Edit Views for MarketUpdatePageCreateView   
class WebinarPageCreateView(CreateView):
    pass

class WebinarPageEditView(EditView):
    pass

class WebinarPageViewSet(PageListingViewSet):
    model = WebinarPage # Model associated with this ViewSet
    icon = 'globe' # Icon for the menu
    menu_label = 'Webinars' # Label in the admin menu
    menu_order = 50 # Order in the admin menu
    add_to_settings_menu = False # Do not add to settings menu
    exclude_from_explorer = False # Include in the explorer
    list_display = ('title', 'status_string')  # Fields to display in the list
    search_fields = ('title',) # Fields for the search functionality
    name = 'webinar_pages'  # Unique name for the ViewSet
    columns = PageListingViewSet.columns + [
        Column("locale", label="Locale", sort_key="locale"), # Custom column for locale
    ]

    create_view_class = WebinarPageCreateView # custom create view class
    edit_view_class = WebinarPageEditView # custom edit view class

    # Method to define additional URL patterns for creating and editing pages
    def get_urlpatterns(self):
        urlpatterns = super().get_urlpatterns() # Get the default patterns
        return urlpatterns + [
            path('create/', self.create_view_class, name='create-update'),  # URL for creating a webinar page
            path('<int:page_id>/edit/', self.edit_view_class, name='edit-update'), # URL for editing
        ]

# Custom Create and Edit Views for MarketUpdatePageCreateView
class WorkshopPageCreateView(CreateView):
    pass

class WorkshopPageEditView(EditView):
    pass

class WorkshopPageViewSet(PageListingViewSet):
    model = WorkshopPage # Model associated with this ViewSet
    icon = 'globe' # Icon for the menu
    menu_label = 'Workshops' # Label in the admin menu
    menu_order = 51 # Order in the admin menu
    add_to_settings_menu = False # Do not add to settings menu
    exclude_from_explorer = False # Include in the explorer
    list_display = ('title', 'status_string')  # Fields to display in the list
    search_fields = ('title',) # Fields for the search functionality
    name = 'workshop_pages'  # Unique name for the ViewSet
    columns = PageListingViewSet.columns + [
        Column("locale", label="Locale", sort_key="locale"), # Custom column for locale
    ]

    create_view_class = WorkshopPageCreateView # custom create view class
    edit_view_class = WorkshopPageEditView # custom edit view class

    # Method to define additional URL patterns for creating and editing pages
    def get_urlpatterns(self):
        urlpatterns = super().get_urlpatterns() # Get the default patterns
        return urlpatterns + [
            path('create/', self.create_view_class, name='create-update'), # URL for creating a workshop page
            path('<int:page_id>/edit/', self.edit_view_class, name='edit-update'), # URL for editing a  workshop page
        ]

# Custom Create and Edit Views for MarketUpdatePageCreateView
class PressReleasePageCreateView(CreateView):
    pass

class PressReleasePageEditView(EditView):
    pass

class PressReleasePageViewSet(PageListingViewSet):
    model = PressReleasePage # Model associated with this ViewSet
    icon = 'globe' # Icon for the menu
    menu_label = 'Press Releases' # Label in the admin menu
    menu_order = 52 # Order in the admin menu
    add_to_settings_menu = False # Do not add to settings menu
    exclude_from_explorer = False # Include in the explorer
    list_display = ('title', 'status_string')  # Fields to display in the list
    search_fields = ('title',) # Fields for the search functionality
    name = 'press_release_pages'  # Unique name for the ViewSet
    columns = PageListingViewSet.columns + [
        Column("locale", label="Locale", sort_key="locale"), # Custom column for locale
    ]

    create_view_class = PressReleasePageCreateView # custom create view class
    edit_view_class = PressReleasePageEditView # custom edit view class

    # Method to define additional URL patterns for creating and editing pages
    def get_urlpatterns(self):
        urlpatterns = super().get_urlpatterns() # Get the default patterns
        return urlpatterns + [
            path('create/', self.create_view_class, name='create-update'), # URL for creating a release page
            path('<int:page_id>/edit/', self.edit_view_class, name='edit-update'), # URL for editing a release page
        ]

# Custom Create and Edit Views for MarketUpdatePageCreateView
class ActivityPageCreateView(CreateView):
    pass

class ActivityPageEditView(EditView):
    pass

class ActivityPageViewSet(PageListingViewSet):
    model = ActivityPage # Model associated with this ViewSet
    icon = 'globe' # Icon for the menu
    menu_label = 'Activities' # Label in the admin menu
    menu_order = 53 # Order in the admin menu
    add_to_settings_menu = False # Do not add to settings menu
    exclude_from_explorer = False # Include in the explorer
    list_display = ('title', 'status_string')  # Fields to display in the list
    search_fields = ('title',) # Fields for the search functionality
    name = 'activity_pages'  # Unique name for the ViewSet
    columns = PageListingViewSet.columns + [
        Column("locale", label="Locale", sort_key="locale"), # Custom column for locale
    ]

    create_view_class = ActivityPageCreateView # custom create view class
    edit_view_class = ActivityPageEditView # custom edit view class

    # Method to define additional URL patterns for creating and editing pages
    def get_urlpatterns(self):
        urlpatterns = super().get_urlpatterns() # Get the default patterns
        return urlpatterns + [
            path('create/', self.create_view_class, name='create-update'), # URL for creating a activity page
            path('<int:page_id>/edit/', self.edit_view_class, name='edit-update'),  # URL for editing a activity page
        ]

# Custom Create and Edit Views for MarketUpdatePageCreateView
class AwardPageCreateView(CreateView):
    pass

class AwardPageEditView(EditView):
    pass

class AwardPageViewSet(PageListingViewSet):
    model = AwardPage # Model associated with this ViewSet
    icon = 'globe' # Icon for the menu
    menu_label = 'Awards' # Label in the admin menu
    menu_order = 54 # Order in the admin menu
    add_to_settings_menu = False # Do not add to settings menu
    exclude_from_explorer = False # Include in the explorer
    list_display = ('title', 'status_string')  # Fields to display in the list
    search_fields = ('title',) # Fields for the search functionality
    name = 'award_pages'  # Unique name for the ViewSet
    columns = PageListingViewSet.columns + [
        Column("locale", label="Locale", sort_key="locale"), # Custom column for locale
    ]

    create_view_class = AwardPageCreateView # custom create view class
    edit_view_class = AwardPageEditView # custom edit view class

    # Method to define additional URL patterns for creating and editing pages
    def get_urlpatterns(self):
        urlpatterns = super().get_urlpatterns() # Get the default patterns
        return urlpatterns + [
            path('create/', self.create_view_class, name='create-update'), # URL for creating a award page
            path('<int:page_id>/edit/', self.edit_view_class, name='edit-update'), # URL for editing a award page
        ]
          
class BlogViewSetGroup(ViewSetGroup):
    menu_label = 'Blogs' # Label in the admin menu
    menu_icon = 'folder-open-inverse' # Icon for the menu
    menu_order = 210 # Order in the admin menu
    items = [
        BlogPageViewSet,
        MarketUpdatePageViewSet,
        TechnicalAnalysisPageViewSet,
        EconomicReportsViewSet,
        WebinarPageViewSet,
        WorkshopPageViewSet,
        PressReleasePageViewSet,
        ActivityPageViewSet,
        AwardPageViewSet
    ]


# Register the ViewSetGroup
@hooks.register("register_admin_viewset")
def register_viewset():
    return BlogViewSetGroup()




class MarketCategoryViewSet(SnippetViewSet):
    model = MarketCategory # Model associated with this ViewSet
    icon = "crosshairs"
    list_display = ('name', 'sort_order', 'locale')
    list_filter = ('locale',)
    ordering = ['sort_order', 'name']
    menu_label = "Market Updates Category" # Label in the admin menu
    menu_name = "market_updates_category"  # Unique name for the ViewSet

class AnalysisCategoryViewSet(SnippetViewSet):
    model = AnalysisCategory # Model associated with this ViewSet
    icon = "crosshairs"
    list_display = ('name', 'sort_order', 'locale')  # Fields to display in the list
    list_filter = ('locale',)
    ordering = ['sort_order', 'name']
    menu_label = "Technical Analysis Category" # Label in the admin menu
    menu_name = "technical_analysis_category"  # Unique name for the ViewSet


class EconomicReportCategoryViewSet(SnippetViewSet):
    model = ReportCategory # Model associated with this ViewSet
    icon = "crosshairs"
    list_display = ('name', 'sort_order', 'locale')  # Fields to display in the list
    list_filter = ('locale',)
    ordering = ['sort_order', 'name']
    menu_label = "Economic Report Category" # Label in the admin menu
    menu_name = "economic_report_category"  # Unique name for the ViewSet


class BlogCategoriesViewSetGroup(SnippetViewSetGroup):
    items = (MarketCategoryViewSet, AnalysisCategoryViewSet, EconomicReportCategoryViewSet, )
    menu_icon = "folder-inverse"
    menu_label = "Blog Categories" # Label in the admin menu
    menu_name = "blog_categories"  # Unique name for the ViewSet
    menu_order = 209 # Order in the admin menu



# When using a SnippetViewSetGroup class to group several SnippetViewSet classes together,
# only register the SnippetViewSetGroup class. You do not need to register each snippet
# model or viewset separately.
register_snippet(BlogCategoriesViewSetGroup)