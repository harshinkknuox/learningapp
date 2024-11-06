from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from django.utils.translation import gettext_lazy as _
from .blocks import ImageSliderBlock,LinkBlock,HomePagesectionsecondBlock

class HomePage(Page):
    image_slider = StreamField(
        [('image_slider', ImageSliderBlock())], 
        use_json_field=True, 
        blank=True,
        min_num=1,
    )
    