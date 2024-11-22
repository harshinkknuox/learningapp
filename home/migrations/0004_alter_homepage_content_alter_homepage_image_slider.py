# Generated by Django 5.1.3 on 2024-11-06 08:00

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_homepage_options_homepage_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('banner_text', 3), ('link_information', 8), ('section_section', 12), ('subject_section', 17)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'help_text': 'Add your heading', 'required': True}), 1: ('wagtail.blocks.CharBlock', (), {'help_text': 'Add sub heading', 'required': False}), 2: ('wagtail.blocks.RichTextBlock', (), {'editor': 'default', 'help_text': 'Add additional text', 'required': False}), 3: ('wagtail.blocks.StructBlock', [[('heading', 0), ('sub_heading', 1), ('description', 2)]], {'group': 'Card Blocks'}), 4: ('wagtail.blocks.CharBlock', (), {'help_text': 'Enter the label of the link', 'required': False}), 5: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('internal', 'Internal Page'), ('external', 'External URL')], 'help_text': 'Select the type of link'}), 6: ('wagtail.blocks.PageChooserBlock', (), {'help_text': 'Select an internal page', 'required': False}), 7: ('wagtail.blocks.URLBlock', (), {'help_text': 'Enter an external URL', 'required': False}), 8: ('wagtail.blocks.StructBlock', [[('label', 4), ('link_type', 5), ('internal_page', 6), ('external_url', 7)]], {'group': 'Card Blocks'}), 9: ('wagtail.images.blocks.ImageChooserBlock', (), {'help_text': 'Main image of the slider', 'required': True}), 10: ('wagtail.blocks.StructBlock', [[('label', 4), ('link_type', 5), ('internal_page', 6), ('external_url', 7)]], {}), 11: ('wagtail.blocks.ListBlock', (10,), {'help_text': 'Add button/link information to this section', 'label': 'Add link details', 'max_num': 2, 'min_num': 0}), 12: ('wagtail.blocks.StructBlock', [[('heading', 0), ('sub_heading', 1), ('description', 2), ('main_image', 9), ('links', 11)]], {'group': 'Card Blocks'}), 13: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': True}), 14: ('wagtail.blocks.CharBlock', (), {'help_text': 'Add your Subject Count', 'required': True}), 15: ('wagtail.blocks.StructBlock', [[('image', 13), ('heading', 0), ('count', 14)]], {}), 16: ('wagtail.blocks.ListBlock', (15,), {'help_text': 'Add Subject information to this section', 'label': 'Add Subject details', 'max_num': 2, 'min_num': 0}), 17: ('wagtail.blocks.StructBlock', [[('heading', 0), ('sub_heading', 1), ('subject_block', 16)]], {'group': 'Card Blocks'})}),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='image_slider',
            field=wagtail.fields.StreamField([('image_slider', 9)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'help_text': "Title for the image slider (Please add the '&lt;/br&gt;' tag where you want to break the line.)", 'required': False}), 1: ('wagtail.blocks.RichTextBlock', (), {'editor': 'default', 'help_text': "Description for the image slider (Please add the '&lt;/br&gt;' tag where you want to break the line.)", 'required': False}), 2: ('wagtail.images.blocks.ImageChooserBlock', (), {'help_text': 'Main image of the slider', 'required': True}), 3: ('wagtail.blocks.CharBlock', (), {'help_text': 'Enter the label of the link', 'required': False}), 4: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('internal', 'Internal Page'), ('external', 'External URL')], 'help_text': 'Select the type of link'}), 5: ('wagtail.blocks.PageChooserBlock', (), {'help_text': 'Select an internal page', 'required': False}), 6: ('wagtail.blocks.URLBlock', (), {'help_text': 'Enter an external URL', 'required': False}), 7: ('wagtail.blocks.StructBlock', [[('label', 3), ('link_type', 4), ('internal_page', 5), ('external_url', 6)]], {}), 8: ('wagtail.blocks.ListBlock', (7,), {'help_text': 'Add button/link information to this section', 'label': 'Add link details', 'max_num': 2, 'min_num': 0}), 9: ('wagtail.blocks.StructBlock', [[('title', 0), ('description', 1), ('main_image', 2), ('links', 8)]], {})}),
        ),
    ]
