from django.db import models
from django import forms

from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel,MultiFieldPanel,InlinePanel
from django.utils.translation import gettext_lazy as _
from wagtail.models import Page,Orderable
from wagtail.fields import StreamField
from project.blocks import *
from learningapp.utils import get_image_rendition


# Create your models here.
class CoursesIndexPage(Page):
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

    max_count = 1  # Only one page is allowed
    parent_page_types = ['home.HomePage']  # Adjust according to your site structure
    
    class Meta:
        verbose_name = _("Course Index Page")
        verbose_name_plural = _("Course Index Pages")


class CoursePage(Page):
    course_name = models.CharField(max_length=225,help_text=_("Course Name"), default='', verbose_name=_('Course Name'))
    course_description = RichTextField(blank=True,help_text=_("Course Description"), verbose_name=_('Course Description'))
    course_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Course Image"),
    )
    content = StreamField([
        ('text_block',TextBlock()),
        ('about_block',AboutBlock()),
        ('faq_block',FAQBlock()),
    ],use_json_field=True,null=True,blank=True)

    content_panels = Page.content_panels +[
        MultiFieldPanel([
            FieldPanel('course_name'),
            FieldPanel('course_description'),
            FieldPanel('course_image'),
            
        ],heading="Course Details"),
        FieldPanel('content'),
    ]

    @property
    def main_image_data(self):
        return get_image_rendition(self.course_image, 'original')

    @property
    def resized_image_data(self):
        return get_image_rendition(self.course_image, 'width-370|height-350')


    subpage_types = []
    parent_page_types = ['course.CoursesIndexPage']

    class Meta:
        verbose_name = _("Course Page")
        verbose_name_plural = _("Course Pages")