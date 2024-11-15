class PropertyViewSetGroup( ViewSetGroup ):
    menu_label = "Property"
    menu_icon = "folder-open-inverse"
    menu_order = 11
    items = [
        AgentPageViewSet(),
        PurposePageViewSet(),
        DeveloperPageViewSet(),
    ]

@hooks.register("register_admin_viewset")
def register_property_group_viewset():
    return PropertyViewSetGroup()


class AgentPageCreateView(CreateView):
    pass

class AgentPageEditView(EditView):
    pass

class AgentPageViewSet(PageListingViewSet):
    model = AgentIndexPage
    name = "agents"
    icon = 'pick'
    menu_label = 'Agents'
    menu_order = 202

    add_to_settings_menu = False
    exclude_from_explorer = False
    add_to_admin_menu = False

    list_display = ('title', 'status_string')
    search_fields = ('title',)
    columns = PageListingViewSet.columns + [
        Column("locale", label="Locale", sort_key="locale"),
        Column("", accessor="get_children_buttons" ,classname="children"),
    ]

    create_view_class = AgentPageCreateView
    edit_view_class = AgentPageEditView

    def get_urlpatterns(self):
        urlpatterns = super().get_urlpatterns()
        return urlpatterns + [
            path('create/', self.create_view_class, name='create'),
            path('<int:page_id>/edit/', self.edit_view_class, name='edit'),
        ]
    
#developer page menu
class DeveloperPageCreateView(CreateView):
    pass

class DeveloperPageEditView(EditView):
    pass

class DeveloperPageViewSet(PageListingViewSet):
    model = DeveloperIndexPage
    name = "developer"
    icon = 'pick'
    menu_label = 'Developers'
    menu_order = 203

    add_to_settings_menu = False
    exclude_from_explorer = False
    add_to_admin_menu = False

    list_display = ('title', 'status_string')
    search_fields = ('title',)
    columns = PageListingViewSet.columns + [
        Column("locale", label="Locale", sort_key="locale"),
        Column("", accessor="get_children_buttons" ,classname="children"),
    ]

    create_view_class = DeveloperPageCreateView
    edit_view_class = DeveloperPageEditView

    def get_urlpatterns(self):
        urlpatterns = super().get_urlpatterns()
        return urlpatterns + [
            path('create/', self.create_view_class, name='create'),
            path('<int:page_id>/edit/', self.edit_view_class, name='edit'),
        ]