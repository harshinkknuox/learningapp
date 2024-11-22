from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from django.utils.translation import gettext_lazy as _
from learningapp.constants import *
from wagtail.snippets.blocks import SnippetChooserBlock
from django import forms

# class BaseContentBlock(blocks.StructBlock):
#     heading = blocks.CharBlock(required=True, max_length=250)  # Heading for the content section
#     content = blocks.RichTextBlock(required=True)  # Main content, supports rich text formatting


# class ContentBlock(blocks.StructBlock):
#     content = blocks.ListBlock(BaseContentBlock(), required=True)
#     class Meta:
#         icon = "link"
#         label = "Content Block"


class ContentBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=250)  # Heading for the content section
    content = blocks.RichTextBlock(required=True)  # Main content, supports rich text formatting
    
    class Meta:
        icon = "link"
        label = "Content Block"