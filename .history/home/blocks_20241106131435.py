from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from learningapp.constants import CARD_CHOICES

class LinkBlock(blocks.StructBlock):
    label = blocks.CharBlock(required=False, help_text=_("Enter the label of the link"))
    link_type = blocks.ChoiceBlock(
        choices = [
            ('internal', _('Internal Page')),
            ('external', _('External URL')),
        ],
        default='internal',
        help_text=_("Select the type of link"),
    )
    internal_page = blocks.PageChooserBlock(
        required=False, 
        help_text=_("Select an internal page"),
        
    )
    external_url = blocks.URLBlock(
        required=False, 
        help_text=_("Enter an external URL"),
    )

    def clean(self, value):
        """
        Custom validation to ensure that only one type of link (internal or external) is provided,
        and that the appropriate fields are filled based on the selected link type.
        """
        cleaned_data = super().clean(value)
        link_type = cleaned_data.get('link_type')
        internal_page = cleaned_data.get('internal_page')
        external_url = cleaned_data.get('external_url')

        # Validation logic based on link type
        if link_type == 'internal' and not internal_page:
            raise ValidationError(_('An internal page must be selected when "Internal Page" is chosen.'))
        elif link_type == 'external' and not external_url:
            raise ValidationError(_('A URL must be provided when "External URL" is chosen.'))

        if link_type == 'internal' and external_url:
            raise ValidationError(_('An external URL should not be provided when linking to an internal page.'))
        if link_type == 'external' and internal_page:
            raise ValidationError(_('An internal page should not be provided when linking to an external URL.'))

        return cleaned_data
    
    class Meta:
        label = _("Link Information")
        icon = 'link'

class ImageSliderBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False, help_text="Title for the image slider (Please add the '&lt;/br&gt;' tag where you want to break the line.)")
    description = blocks.RichTextBlock(editor='default',required=False, help_text="Description for the image slider (Please add the '&lt;/br&gt;' tag where you want to break the line.)")    
    main_image = ImageChooserBlock(required=True, help_text="Main image of the slider")

    links = blocks.ListBlock(
        LinkBlock(),
        min_num=0,  # No minimum requirement
        max_num=2,  # Maximum of two links
        help_text=_("Add button/link information to this section"),
        label="Add link details"
    )

    class Meta:
        icon = 'image'
        label = "Image Slider"

class HomePageSharesListBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text=_("Add your heading"))
    sub_heading = blocks.CharBlock(required=False, help_text=_("Add sub heading"))
    description = blocks.RichTextBlock(editor='default',required=False, help_text=_("Add additional text"))
    class Meta:
        template = "blocks/base_text_block.html"
        icon = "table"
        label = "Home Page Shares List Block"

class HomePagesectionsecondBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text=_("Add your heading"))
    sub_heading = blocks.CharBlock(required=False, help_text=_("Add sub heading"))
    description = blocks.RichTextBlock(editor='default',required=False, help_text=_("Add additional text"))
    main_image = ImageChooserBlock(required=True, help_text="Main image of the slider")
    links = blocks.ListBlock(
        LinkBlock(),
        min_num=0,  # No minimum requirement
        max_num=2,  # Maximum of two links
        help_text=_("Add button/link information to this section"),
        label="Add link details"
    )

    class Meta:
        template = "blocks/base_section_second_block.html"
        icon = "table"
        label = "Home Page section second Block"

class HomeSubjectSectionLink(blocks.StructBlock):
    image = ImageChooserBlock(required=True) 
    heading = blocks.CharBlock(required=True, help_text=_("Add your heading"))
    count  = blocks.CharBlock(required=True, help_text=_("Add your Subject Count"))

    class Meta:
        label = _("Subject Information")
        icon = 'link'

class HomeSubjectSectionBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text=_("Add your heading"))
    sub_heading = blocks.CharBlock(required=False, help_text=_("Add sub heading"))
    subject_block = 