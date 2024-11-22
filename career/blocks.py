from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from django.utils.translation import gettext_lazy as _
from learningapp.constants import *
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.blocks import StructBlock, PageChooserBlock, ListBlock
from django import forms


class ImageTextCardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Enter the card title")
    description = blocks.TextBlock(required=False, help_text="Enter the description")
    image = ImageChooserBlock(required=True, help_text="Select the background image for the card")
    
    class Meta:
        # template = "blocks/text_block_with_links.html"
        icon = "doc-full"
        label = "Image Text Card Block"

class BaseFaqBlock(blocks.StructBlock):
    question = blocks.CharBlock(required=True, help_text=_("Add your question"))
    answer = blocks.RichTextBlock(required=False, help_text=_("Add your answer"))

    class Meta:
        # template = "blocks/base_text_block.html"
        icon = "help"
        label = "FAQ Block"  

class FAQBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, help_text=_("Add your heading"))
    sub_heading = blocks.CharBlock(required=False, help_text=_("Add sub heading"))
    description  = blocks.RichTextBlock(required=False, help_text=_("Add additional text"))
    points = blocks.ListBlock(BaseFaqBlock(), label="Add FAQ", help_text="Add frequently asked questions to this section")
 
    class Meta:
        icon = "help"
        label = _("Frequently asked questions")


class BlogBlock(blocks.StructBlock):
    blog_pages = ListBlock(
        PageChooserBlock(
            required=True,
            help_text="Choose a blog page",
            
        ),
        label="Blog Pages",
        help_text="Add multiple blog pages to this block"
    )

    class Meta:
        icon = "doc-empty"
        label = "Blog Selector Block (Multiple)"
        help_text = "A block for selecting multiple blog pages"