
# from career.serializers import ImageTextCardBlockSerializer,FAQBlockSerializer,BlogBlockSerializer
# from blog.serializers import BaseContentBlockSerializer
from django.utils.translation import get_language_from_request
from django.shortcuts import get_object_or_404
# from wagtail.models import Locale


class PageContentMixin:
    def get_content(self, obj):
        content_blocks = []
        request = self.context.get('request')
        view_type = self.context.get('view_type','')
        content = obj.content
        
        lang = get_language_from_request(request)
        
        
        for block in content:
            # import pdb; pdb.set_trace()
            if block.block_type == 'image_text_card_block':
                from career.serializers import ImageTextCardBlockSerializer
                content_blocks.append({
                    'type': 'image_text_card_block',
                    'value':  ImageTextCardBlockSerializer(block.value, context={'parent': self}).data
                })
            elif block.block_type == 'faq_block':
                from career.serializers import FAQBlockSerializer
                content_blocks.append({
                    'type': 'faq_block',
                    'value':  FAQBlockSerializer(block.value, context={'parent': self}).data
                })                
            elif block.block_type == 'blog_block':
                from career.serializers import BlogBlockSerializer
                print("Blog Block Value:", block.value)  # Debug
                content_blocks.append({
                    'type': 'blog_block',
                    'value':  BlogBlockSerializer(block.value, context={'parent': self}).data
                })
            elif block.block_type == 'content_block':
                from blog.serializers import BaseContentBlockSerializer
                content_blocks.append({
                    'type': 'content_block',
                    'value':  BaseContentBlockSerializer(block.value, context={'parent': self}).data
                })
        return content_blocks  