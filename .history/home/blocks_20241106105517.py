from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from learning.constants import PAGE_TARGETS,BG_CHOICES,CARD_CHOICES,

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
        target_model = PAGE_TARGETS
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
        target_model = PAGE_TARGETS
    )
    external_url = blocks.URLBlock(
        required=False, 
        help_text=_("Enter an external URL"),
    )

    def clean(self, value):
      
        cleaned_data = super().clean(value)
        link_type = cleaned_data.get('link_type')
        internal_page = cleaned_data.get('internal_page')
        external_url = cleaned_data.get('external_url')

        # Validation logic based on link type
        if link_type == 'internal' and not internal_page:
            raise ValidationError(_('An internal page must be selected when "Internal Page" is chosen.'))
        elif link_type == 'external' and not external_url:
            raise ValidationError(_('A URL must be provided when "External URL" is chosen.'))

        # Prevent both internal and external links from being filled
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
    description = blocks.RichTextBlock(editor='default',required=False, help_text=_("Add additional text"))    
    main_image = ImageChooserBlock(required=True, help_text="Main image of the slider")
    # related_images = blocks.ListBlock(
    #     ImageChooserBlock(),
    #     max_num=10,  # Limit to 10 images
    #     required=False,  # Make the field optional
    #     help_text="Up to 10 small images"
    # )
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