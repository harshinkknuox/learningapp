from django.db import models
from django import forms

from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel,MultiFieldPanel,InlinePanel
from django.utils.translation import gettext_lazy as _
from wagtail.models import Page,Orderable
from wagtail.fields import StreamField

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
