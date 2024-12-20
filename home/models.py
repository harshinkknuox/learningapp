from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from django.utils.translation import gettext_lazy as _
from .blocks import ImageSliderBlock,LinkBlock,HomePageSharesListBlock,HomePagesectionsecondBlock,HomeSubjectSectionBlock
from project.models import ProjectsPage
class HomePage(Page):
    image_slider = StreamField(
        [('image_slider', ImageSliderBlock())], 
        use_json_field=True, 
        blank=True,
        min_num=1,
    )

    body = StreamField([
        #home page blocks
        ('banner_text', HomePageSharesListBlock(group="Card Blocks")),
        ('link_information', LinkBlock(group="Card Blocks")),
        ('section_section', HomePagesectionsecondBlock(group="Card Blocks")),
        ('subject_section', HomeSubjectSectionBlock(group="Card Blocks")),
        
        ],use_json_field=True, blank=True  )
    max_count = 1

    content_panels = Page.content_panels + [
        FieldPanel('image_slider'),
        FieldPanel('body'),        
    ]
    template ="home/index.html"
    class Meta:
        verbose_name = _("Home Page")
        verbose_name_plural = _("Home Pages")

    def get_locale_display(self):
        return str(self.locale)
    

    def get_projects(self):
        # Get the project index page
        project_index = ProjectsPage.objects.all()  # Assuming there's only one projectIndexPage
        if project_index:
            return project_index # Get the latest 5 project posts
        return project_index  # Return an empty queryset if no project index page exists