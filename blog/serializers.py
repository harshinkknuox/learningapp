import base64
from rest_framework import serializers
from wagtail.fields import StreamValue
from .models import BlogPage
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from learningapp.utils import get_image_rendition
from wagtail.images.models import Image
from wagtail.rich_text import RichText
from bs4 import BeautifulSoup
from home.mixins import PageContentMixin


class BaseContentBlockSerializer(serializers.Serializer):
    heading = serializers.CharField(read_only=True)
    content = serializers.SerializerMethodField(read_only=True)

    def get_content(self, instance):
        # import pdb; pdb.set_trace()
        content =  instance['content']
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

    
class BlogPageSerializer(serializers.Serializer,PageContentMixin):
    date = serializers.CharField(read_only=True)
    title = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    image = serializers.SerializerMethodField(read_only=True,source='blog_image')
    category = serializers.CharField(read_only=True)
    
    slug = serializers.CharField(read_only=True)
    content = serializers.SerializerMethodField()
    
    def get_content(self, obj):
        return super().get_content(obj)

    def get_image(self, obj):
        return obj.main_image_data
    
    def get_resized_image(self, obj):
        return obj.resized_image_data
    
    
class BlogDetailSerializer(BlogPageSerializer):
    content = serializers.SerializerMethodField()

    def get_content(self, obj):
        return super().get_content(obj)