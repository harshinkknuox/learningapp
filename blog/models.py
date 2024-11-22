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

@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    class Mets:
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categorys'
        
category = ParentalManyToManyField("blog.BlogCategory",blank=True)

class BlogsIndexPage(Page):
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

    max_count = 1  # Only one page is allowed
    parent_page_types = ['home.HomePage']  # Adjust according to your site structure
    subpage_types = ['blog.BlogPage']  # Adjust according to your site structure

    class Meta:
        verbose_name = _("Blog Index Page")
        verbose_name_plural = _("Blog Index Pages")

class BlogPage(Page):
    date = models.DateField(_("Post date"), null=True,blank=True)  # Required post date
    name = models.CharField(max_length=225,help_text=_("Blog Name"), default='', verbose_name=_('Blog Name'))
    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Blog image"),
    )
    category = models.ForeignKey("blog.BlogCategory",on_delete=models.SET_NULL, null=True,blank=True,verbose_name=_('Blog Category'))

    content =  StreamField([
        ('content_block',ContentBlock()),

    ],use_json_field=True,null=True,blank=True)
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('name'),
            FieldPanel('blog_image'),           
            FieldPanel('category'),           
        ],heading="Blog Information"),
        FieldPanel('content'),
    ]

    @property
    def main_image_data(self):
        return get_image_rendition(self.blog_image, 'original')

    @property
    def resized_image_data(self):
        return get_image_rendition(self.blog_image, 'width-370|height-350')
    

    subpage_types = []
    parent_page_types = ['blog.BlogsIndexPage'] 

    template = "blog/blog_detail.html"

    class Meta:
        verbose_name = _("Blog Page")
        verbose_name_plural = _("Blog Pages")