# Generated by Django 5.1.3 on 2024-11-06 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_homepage_content_alter_homepage_image_slider'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='content',
            new_name='body',
        ),
    ]
