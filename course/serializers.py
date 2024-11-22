from rest_framework import serializers
from wagtail.rich_text import RichText
from bs4 import BeautifulSoup
from learningapp.utils import get_image_rendition
import base64


class CoursePageSerializer(serializers.Serializer):
    course_name = serializers.CharField(read_only=True)
    course_description = serializers.SerializerMethodField(read_only=True)
    course_image = serializers.SerializerMethodField(read_only=True,source='course_image')
    slug = serializers.CharField(read_only=True)
    def get_course_image(self,obj):
        return obj.main_image_data
    
    def get_resized_image(self,obj):
        return obj.resized_image_data
    
    def get_course_description(self, instance):
        content = instance.course_description
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