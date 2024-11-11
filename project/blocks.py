from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from django.utils.translation import gettext_lazy as _
from learningapp.constants import *
from wagtail.snippets.blocks import SnippetChooserBlock
from django import forms

class LinkBlock(blocks.StructBlock):
    label = blocks.CharBlock(required=False, help_text=_("Enter the label of the link"))
    link_url = blocks.URLBlock(
        required=False, 
        help_text=_("Enter a URL"),
    )
    class Meta:
        label = _("Link Information")
        icon = 'link'

class BaseImageTextCardBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, help_text=_("Add your heading"))
    sub_heading = blocks.CharBlock(required=False, help_text=_("Add your heading"))
    image = ImageChooserBlock(required=False) 
    description  = blocks.RichTextBlock(required=False, help_text=_("Add description"))

    class Meta:
        icon = "image"
        label = "Base Image Text Card Block"


class ImageTextCardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Enter the card title")
    points  = blocks.RichTextBlock(required=True, help_text=_("Add the key points"))
    image = ImageChooserBlock(required=True, help_text="Select the background image for the card")

    # Fields for the heading, subheading, and description
    heading = blocks.CharBlock(required=True, help_text="Enter the heading")
    subheading = blocks.CharBlock(required=False, help_text="Enter the subheading")
    description = blocks.TextBlock(required=False, help_text="Enter the description")

    class Meta:
        # template = "blocks/text_block_with_links.html"
        icon = "image"
        label = "Image Text Card Block"

class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)


class ImageTextCardBlockWithLinks(ImageTextCardBlock):
    links = blocks.ListBlock(
        LinkBlock(),
        min_num=0,
        max_num=2,
        help_text=_("Add button/link information to this section"),
        label="Add link details"
    )

    class Meta:
        # template = "blocks/text_block_with_links.html"
        icon = "doc-full"
        label = "Image Text Card Block with Links"

class BaseFaqBlock(blocks.StructBlock):
    question = blocks.CharBlock(required=True, help_text=_("Add your question"))
    answer = blocks.RichTextBlock(required=False, help_text=_("Add your answer"))

    class Meta:
        # template = "blocks/base_text_block.html"
        icon = "help"
        label = "FAQ Block"        

class NearbyLocationBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text=_("Add sub heading"))
    description = blocks.RichTextBlock(required=False, help_text=_("Add description"))
    locations = blocks.ListBlock(
        blocks.StructBlock(
            [
            ('nearbylocation', blocks.ChoiceBlock(max_length=20, choices=NEARBY_LOCATIONS,  null=True, blank=True, default="", help_text=_("Nearby Locations"))),
            ('latitude', blocks.FloatBlock(required=False, help_text=_("Add Latitude of the nearby location"))),
            ('longitude', blocks.FloatBlock(required=False, help_text=_("Add Longitude of the nearby location"))),
            ('distance' ,blocks.FloatBlock(required=False, help_text=_("Add distance in Kilometer")))
            ]
        )
    )


############## main blocks ################

class TextBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text=_("Add your heading"))
    sub_heading = blocks.CharBlock(required=True, help_text=_("Add sub heading"))
    description = blocks.RichTextBlock(required=False, help_text=_("Add description"))
    links = blocks.ListBlock(
        LinkBlock(),
        min_num=0,
        max_num=2,
        help_text=_("Add button/link information to this section"),
        label="Add link details"
    )

    class Meta:
        # template = "blocks/base_text_block.html"
        icon = "doc-full"
        label = "Text Block With Link"


class AboutBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text=_("Add your heading"))
    sub_heading = blocks.CharBlock(required=False, help_text=_("Add sub heading"))
    description = blocks.RichTextBlock(required=False, help_text=_("Add additional text"))
    links = blocks.ListBlock(
        LinkBlock(),
        min_num=0,
        max_num=2,
        help_text=_("Add button/link information to this section"),
        label="Add link details"
    )
    cards = blocks.ListBlock(
        BaseImageTextCardBlock(),
        help_text=_("Add card to this section"),
        label="Add card details"
    )

    class Meta:
        # template = "blocks/base_text_block.html"
        icon = "doc-full"
        label = "About Block"


class CardBlockWithTextOverlayImage(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text=_("Add your heading"))  
    sub_heading = blocks.CharBlock(required=False, help_text=_("Add sub heading"))
    points = blocks.ListBlock(ImageTextCardBlockWithLinks(), 
                              label="Add image card", 
                              help_text="Add multiple image cards to this section. The image alignment is at the top.")


class PhotoGalleryBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text=_("Add your heading"))  
    image = blocks.ListBlock(ImageBlock(),label='Add Images')

    class Meta:
        # template = "blocks/base_text_block.html"
        icon = "doc-full"
        label = "Image Block"


class CardBlockWithLink(BaseImageTextCardBlock):
    links = blocks.ListBlock(
        LinkBlock(),
        min_num=0,
        max_num=2,
        help_text=_("Add button/link information to this section"),
        label="Add link details"
    )

    class Meta:
        # template = "blocks/text_block_with_links.html"
        icon = "doc-full"
        label = "Card Block with Links"


class TextCardBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, help_text=_("Add your heading"))
    sub_heading = blocks.CharBlock(required=False, help_text=_("Add your heading")) 
    description  = blocks.RichTextBlock(required=False, help_text=_("Add description"))
    card = blocks.ListBlock(
        BaseImageTextCardBlock()
    )


class FAQBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, help_text=_("Add your heading"))
    sub_heading = blocks.CharBlock(required=False, help_text=_("Add sub heading"))
    description  = blocks.RichTextBlock(required=False, help_text=_("Add additional text"))
    points = blocks.ListBlock(BaseFaqBlock(), label="Add FAQ", help_text="Add frequently asked questions to this section")
 
    class Meta:
        icon = "help"
        label = _("Frequently asked questions")


class LocationBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, help_text=_("Add your heading"))
    latitude = blocks.FloatBlock(required=False, help_text=_("Add Latitude of the location"))
    longitude = blocks.FloatBlock(required=False, help_text=_("Add Longitude of the location"))
    nearby_locations = blocks.ListBlock(
        NearbyLocationBlock()
    )

    class Meta:
        # template = "blocks/base_text_block.html"
        icon = "doc-full"
        label = "Nearby Location Block"  



class AmenitiesBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, help_text=_("Add your heading"))
    amenities = blocks.ListBlock(SnippetChooserBlock(target_model='project.Amenities'))
    # data_list = blocks.ListBlock(
    #     blocks.StructBlock(
    #         [
    #             ("title",blocks.CharBlock(required=True,max_length=40)),
    #             ("image",ImageChooserBlock(required=True)),
    #         ]
    #     )
    # )
    # def get_form(self, value=None, prefix='', **kwargs):
    #     # Set up the form field for selecting multiple snippets
    #     form_field = AmenitiesCheckboxFormField(
    #         queryset=project.Amenities.objects.all(),
    #         widget=forms.CheckboxSelectMultiple,
    #         required=False
    #     )
    #     return form_field
    class Meta:
        icon = "doc-full"
        label = "Amenities Block"  


class FloorPlanBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, help_text=_("Add your heading"))
    sub_heading = blocks.CharBlock(required=False, help_text=_("Add your heading")) 
    description  = blocks.RichTextBlock(required=False, help_text=_("Add description"))
    images = blocks.ListBlock(
        ImageBlock()
    )

    class Meta:
        icon = "doc-full"
        label = "Floor Plan Block"  