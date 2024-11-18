from django.db import models
from django import forms

from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel,MultiFieldPanel,InlinePanel
from django.utils.translation import gettext_lazy as _
from wagtail.models import Page,Orderable
from wagtail.fields import StreamField
from .blocks import *
from learningapp.constants import *
from learningapp.utils import get_image_rendition
from modelcluster.fields import ParentalKey,ParentalManyToManyField
from wagtail.snippets.models import register_snippet
from django.core.exceptions import ValidationError
import os
# Create your models here.

class BlogsIndexPage(Page):
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

    max_count = 1  # Only one page is allowed
    parent_page_types = ['home.HomePage']  # Adjust according to your site structure
    

    class Meta:
        verbose_name = _("Blog Index Page")
        verbose_name_plural = _("Blog Index Pages")

