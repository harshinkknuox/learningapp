
from career.serializers import *
from blog.serializers import *
from django.utils.translation import get_language_from_request
from django.shortcuts import get_object_or_404
from wagtail.models import Locale

class PageContentMixin:
    def get_content(self, obj):
        content_blocks = []
        request = self.context.get('request')
        view_type = self.context.get('view_type','')
        content = obj.content
        
        lang = get_language_from_request(request)
        locale = get_object_or_404(Locale, language_code=lang)
        
        for block in content:            
            if block.block_type == 'image_text_card_block':
                
                content_blocks.append({
                    'type': 'base_text_block',
                    'value':  ImageTextCardBlockSerializer(block.value, context={'parent': self}).data
                })
            elif block.block_type == 'faq_block':
                content_blocks.append({
                    'type': 'overlayed_image_block',
                    'value':  FAQBlockSerializer(block.value, context={'parent': self}).data
                })                
            elif block.block_type == 'blog_block':
                
                content_blocks.append({
                    'type': 'base_image_block',
                    'value':  BlogBlockSerializer(block.value, context={'parent': self}).data
                })
            elif block.block_type == 'content_block':
                
                content_blocks.append({
                    'type': 'content_block',
                    'value':  ContentBlockSerializer(block.value, context={'parent': self}).data
                })
        return content_blocks  