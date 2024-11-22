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
class Agent(models.Model):
    name = models.CharField(max_length=100)
    introduction  = RichTextField(help_text=_("Add Introduction"),verbose_name=_('Introduction'))
    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.CASCADE
    )
    description  = RichTextField(blank=True, null=True,default='',help_text=_("Add description"),verbose_name=_('Description'))
    id_number =  models.IntegerField(help_text = _("Add ID Number"))
    whatsapp_number =  models.IntegerField(help_text = _("Add Whatsapp Number"))
    call_number =  models.IntegerField(help_text = _("Add Number"))

    def __str__(self):
        return self.name
    
    class Mets:
        verbose_name = 'Agent'
        verbose_name_plural = 'Agents'

@register_snippet       
class Amenities(models.Model):
    title = models.CharField(max_length=100)
    icon = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
    
    class Mets:
        verbose_name = 'Amenity'
        verbose_name_plural = 'Amenities'

agent = ParentalManyToManyField("project.Agent",blank=True)
agent = ParentalManyToManyField("project.Amenities",blank=True)


class ProjectsIndexPage(Page):
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

    max_count = 1  # Only one page is allowed
    parent_page_types = ['home.HomePage']  # Adjust according to your site structure
    subpage_types = ['project.ProjectsPage']  # Adjust according to your site structure

    class Meta:
        verbose_name = _("Project Index Page")
        verbose_name_plural = _("Project Index Pages")

class ProjectsPage(Page):
    project_name = models.CharField(max_length=225,help_text=_("Project Name"), default='', verbose_name=_('Project Name'))
    project_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Project image"),
    )
    project_description = RichTextField(blank=True,null=True,default='',help_text=_("Project description"),verbose_name=_('Project description'))
    communities = models.CharField(max_length=20, choices=COMMUNITIES,  null=True, blank=True)
    developers = models.CharField(max_length=20, choices=DEVELOPERS,  null=True, blank=True)
    agent=models.ForeignKey("project.Agent",on_delete=models.SET_NULL, null=True,blank=True,)
    floor_plan = models.FileField(upload_to='uploads/', null=True, blank=True)
    content = StreamField([
        ('text_block', TextBlock()),
        ('about_block', AboutBlock()),
        ('photo_gallery_block', PhotoGalleryBlock()),
        ('card_block_with_link', CardBlockWithLink()),
        ('text_card_block', TextCardBlock()),
        ('faq_block', FAQBlock()),
        ('location_block', LocationBlock()),
        ('amenities_block', AmenitiesBlock()),
        ('floor_plan_block', FloorPlanBlock()),
    ],use_json_field=True,null=True,blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('project_name'),
            FieldPanel('project_image'),
            FieldPanel('project_description'),
            FieldPanel('communities'),
            FieldPanel('developers'),
            FieldPanel("agent",widget=forms.Select),
            
        ],heading="Project Information"),
        FieldPanel('content'),
    ]

    @property
    def main_image_data(self):
        return get_image_rendition(self.project_image, 'original')

    @property
    def resized_image_data(self):
        return get_image_rendition(self.project_image, 'width-370|height-350')
    

    def clean(self):
        super().clean()  # Call the parent class's clean method first

        # Perform custom file size validation
        if self.floor_plan:
            if self.floor_plan.size > 5242880:  # 5MB size limit
                raise ValidationError("The maximum file size that can be uploaded is 5MB")

        # Perform custom file extension validation
        if self.floor_plan:
            ext = self.floor_plan.name.split('.')[-1].lower()
            valid_extensions = ['pdf', 'docx', 'jpg']
            if ext not in valid_extensions:
                raise ValidationError("Unsupported file extension. Allowed extensions are: .pdf, .docx, .jpg")

    subpage_types = []
    parent_page_types = ['project.ProjectsIndexPage']  # Ensure the correct path

    class Meta:
        verbose_name = _("Project Page")
        verbose_name_plural = _("Project Pages")