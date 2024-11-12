# Generated by Django 5.1.3 on 2024-11-12 07:19

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('wagtailcore', '0094_alter_page_locale'),
        ('wagtailimages', '0027_image_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('course_name', models.CharField(default='', help_text='Course Name', max_length=225, verbose_name='Course Name')),
                ('course_description', wagtail.fields.RichTextField(blank=True, help_text='Course Description', verbose_name='Course Description')),
                ('content', wagtail.fields.StreamField([('text_block', 7), ('about_block', 14), ('faq_block', 19)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'help_text': 'Add your heading', 'required': True}), 1: ('wagtail.blocks.CharBlock', (), {'help_text': 'Add sub heading', 'required': True}), 2: ('wagtail.blocks.RichTextBlock', (), {'help_text': 'Add description', 'required': False}), 3: ('wagtail.blocks.CharBlock', (), {'help_text': 'Enter the label of the link', 'required': False}), 4: ('wagtail.blocks.URLBlock', (), {'help_text': 'Enter a URL', 'required': False}), 5: ('wagtail.blocks.StructBlock', [[('label', 3), ('link_url', 4)]], {}), 6: ('wagtail.blocks.ListBlock', (5,), {'help_text': 'Add button/link information to this section', 'label': 'Add link details', 'max_num': 2, 'min_num': 0}), 7: ('wagtail.blocks.StructBlock', [[('heading', 0), ('sub_heading', 1), ('description', 2), ('links', 6)]], {}), 8: ('wagtail.blocks.CharBlock', (), {'help_text': 'Add sub heading', 'required': False}), 9: ('wagtail.blocks.RichTextBlock', (), {'help_text': 'Add additional text', 'required': False}), 10: ('wagtail.blocks.CharBlock', (), {'help_text': 'Add your heading', 'required': False}), 11: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': False}), 12: ('wagtail.blocks.StructBlock', [[('heading', 10), ('sub_heading', 10), ('image', 11), ('description', 2)]], {}), 13: ('wagtail.blocks.ListBlock', (12,), {'help_text': 'Add card to this section', 'label': 'Add card details'}), 14: ('wagtail.blocks.StructBlock', [[('heading', 0), ('sub_heading', 8), ('description', 9), ('links', 6), ('cards', 13)]], {}), 15: ('wagtail.blocks.CharBlock', (), {'help_text': 'Add your question', 'required': True}), 16: ('wagtail.blocks.RichTextBlock', (), {'help_text': 'Add your answer', 'required': False}), 17: ('wagtail.blocks.StructBlock', [[('question', 15), ('answer', 16)]], {}), 18: ('wagtail.blocks.ListBlock', (17,), {'help_text': 'Add frequently asked questions to this section', 'label': 'Add FAQ'}), 19: ('wagtail.blocks.StructBlock', [[('heading', 10), ('sub_heading', 8), ('description', 9), ('points', 18)]], {})}, null=True)),
                ('course_image', models.ForeignKey(blank=True, help_text='Course Image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Course Page',
                'verbose_name_plural': 'Course Pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]