from rest_framework import serializers
from wagtail.fields import StreamValue
from .models import CareerPage
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from learningapp.utils import get_image_rendition
from wagtail.images.models import Image
from wagtail.rich_text import RichText
from bs4 import BeautifulSoup
import base64
from wagtail.models import Page


class PageSerializer(serializers.Serializer):
    page_type = serializers.SerializerMethodField()
    class Meta:
        model = Page
        fields = ['slug','page_type']
    def get_page_type(self, obj):
        # import pdb; pdb.set_trace()
        return obj.specific._meta.model_name

class ImageTextCardBlockSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    image = serializers.SerializerMethodField(read_only=True,source='image')

    def get_image(self, obj):
        if obj.get('image'):
            image = obj['image']
            rendition = get_image_rendition(image, 'original')
            if rendition:
                return {
                    "url": rendition['url'],
                    "full_url": rendition['full_url'],
                    "width": rendition['width'],
                    "height": rendition['height'],
                    "alt": rendition['alt']
                }
        return None
    
class BaseFaqBlockSerializer(serializers.Serializer):
    question = serializers.CharField(read_only=True)
    answer = serializers.SerializerMethodField(read_only=True)
    def get_answer(self, instance):
        content = instance.get('answer')
        if not content:
            return None

        # Ensure content is a string
        if isinstance(content, RichText):
            content = str(content)

        request = self.context.get('request')
        if not request:
            return content  # or raise an exception if request is required

        soup = BeautifulSoup(content, 'html.parser')
        for img_tag in soup.find_all('img'):
            src = img_tag.get('src')
            if src:
                img_tag['src'] = request.build_absolute_uri(src)
        return str(soup)
    
class FAQBlockSerializer(serializers.Serializer):
    heading = serializers.CharField(read_only=True)
    sub_heading = serializers.CharField(read_only=True)
    description = serializers.SerializerMethodField(read_only=True)
    points = serializers.ListField(child=BaseFaqBlockSerializer())

    def get_description(self, instance):
        content = instance.get('description')
        if not content:
            return None

        # Ensure content is a string
        if isinstance(content, RichText):
            content = str(content)

        request = self.context.get('request')
        if not request:
            return content  # or raise an exception if request is required

        soup = BeautifulSoup(content, 'html.parser')
        for img_tag in soup.find_all('img'):
            src = img_tag.get('src')
            if src:
                img_tag['src'] = request.build_absolute_uri(src)

        return str(soup)
    

class BlogBlockSerializer(serializers.Serializer):
    internal_page = PageSerializer(required=False)

    def to_representation(self, instance):
        # import pdb; pdb.set_trace()
        data = super().to_representation(instance)
        if instance.get('internal_page'):
            if isinstance(instance['internal_page'], Page):
                data['internal_page'] = PageSerializer(instance['internal_page']).data
            else:
                try:
                    page = Page.objects.get(id=instance['internal_page'])
                    data['internal_page'] = PageSerializer(page).data
                except Page.DoesNotExist:
                    data['internal_page'] = None
        return data
    
class CareerPageSerializer(serializers.Serializer):
    heading = serializers.CharField(read_only=True)
    subheading = serializers.CharField(read_only=True)
    content = serializers.SerializerMethodField()

    def get_content(self, obj):
        return super().get_content(obj)