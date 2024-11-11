from rest_framework import serializers
from wagtail.rich_text import RichText
from bs4 import BeautifulSoup
from learningapp.utils import get_image_rendition
import base64

class LinkBlockSerializer(serializers.Serializer):
    label = serializers.CharField(read_only=True)
    link_url = serializers.URLField(required=False)

class ImageCardBlockSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)
    points = serializers.SerializerMethodField(read_only=True)
    image = serializers.SerializerMethodField(read_only=True)
    
    heading = serializers.CharField(read_only=True)
    subheading = serializers.CharField(read_only=True)
    description = serializers.SerializerMethodField(read_only=True)
    links = serializers.SerializerMethodField(read_only=True)

    def get_links(self, instance):
        links = instance.get('links')
        return LinkBlockSerializer(links, many=True).data 

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
    
    def get_points(self, instance):
        content = instance.get('points')
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
    
class PhotoBlockSerializer(serializers.Serializer):
    image = serializers.SerializerMethodField(read_only=True)

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
    

class BaseImageTextCardSerializer(serializers.Serializer):
    heading = serializers.CharField(read_only=True)
    image = serializers.SerializerMethodField(read_only=True)
    description = serializers.SerializerMethodField(read_only=True)

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


class PropertySerializer(serializers.Serializer):
    heading = serializers.CharField(read_only=True)
    sub_heading = serializers.CharField(read_only=True)
    points = serializers.ListField(child=ImageCardBlockSerializer())

    def get_points(self, instance):
        points = instance.get('points')
        return LinkBlockSerializer(points, many=True).data 
    
class TextBlockSerializer(serializers.Serializer):
    heading = serializers.CharField(read_only=True)
    developer = serializers.CharField(read_only=True)
    links = serializers.SerializerMethodField(read_only=True)

    def get_links(self, instance):
        links = instance.get('links')
        return LinkBlockSerializer(links, many=True).data 
    
class ImageBlockSerializer(serializers.Serializer):
    heading = serializers.CharField(read_only=True)
    image = serializers.SerializerMethodField(read_only=True)

    def get_image(self, instance):
        image = instance.get('image')
        return PhotoBlockSerializer(image, many=True).data 
    

class AboutSerializer(serializers.Serializer):
    heading = serializers.CharField(read_only=True)
    sub_heading = serializers.CharField(read_only=True)
    description = serializers.SerializerMethodField(read_only=True)
    links = serializers.SerializerMethodField(read_only=True)
    cards = serializers.SerializerMethodField(read_only=True)

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
    
    def get_links(self, instance):
        links = instance.get('links')
        return LinkBlockSerializer(links, many=True).data 
    
    def get_cards(self, instance):
        cards = instance.get('cards')
        return BaseImageTextCardSerializer(cards, many=True).data 
    

class CardWithLinkSerializer(serializers.Serializer):
    heading = serializers.CharField(read_only=True)
    image = serializers.SerializerMethodField(read_only=True)
    description = serializers.SerializerMethodField(read_only=True)
    links = serializers.SerializerMethodField(read_only=True)

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
    
    def get_links(self, instance):
        links = instance.get('links')
        return LinkBlockSerializer(links, many=True).data 
    
class TextCardSerializer(serializers.Serializer):
    heading = serializers.CharField(read_only=True)
    sub_heading = serializers.CharField(read_only=True)
    description = serializers.SerializerMethodField(read_only=True)
    card = serializers.SerializerMethodField(read_only=True)

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
    
    def get_card(self, instance):
        card = instance.get('card')
        return BaseImageTextCardSerializer(card, many=True).data

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
    
class NearbyLocationDetailSerializer(serializers.Serializer):
    nearbylocation = serializers.CharField(read_only=True)
    latitude = serializers.FloatField(read_only=True)
    longitude = serializers.FloatField(read_only=True)
    distance = serializers.FloatField(read_only=True)
    
class NearbyLocationSerializer(serializers.Serializer):    
    heading = serializers.CharField(read_only=True)
    description = serializers.SerializerMethodField(read_only=True)
    locations = NearbyLocationDetailSerializer(many=True,read_only=True)

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

    
class LocationBlockSerializer(serializers.Serializer):
    heading = serializers.CharField(read_only=True)
    latitude = serializers.FloatField(read_only=True)
    longitude = serializers.FloatField(read_only=True)
    nearby_locations = serializers.ListField(child=NearbyLocationSerializer())

class AmenitiesSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)
    icon = serializers.SerializerMethodField(read_only=True)

    def get_icon(self, obj):
        if obj.icon:
            icon = obj.icon
            rendition = get_image_rendition(icon, 'original')
            if rendition:
                return {
                    "url": rendition['url'],
                    "full_url": rendition['full_url'],
                    "width": rendition['width'],
                    "height": rendition['height'],
                    "alt": rendition['alt']
                }
        return None

class AmenitiesBlockSerializer(serializers.Serializer):
    heading = serializers.CharField(read_only=True)
    amenities = AmenitiesSerializer(many=True,read_only=True)

class FloorPlanBlockSerializer(serializers.Serializer):
    heading = serializers.CharField(read_only=True)
    sub_heading = serializers.CharField(read_only=True)
    description = serializers.SerializerMethodField(read_only=True)
    images = PhotoBlockSerializer(many=True,read_only=True)

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


class AgentSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    introduction = serializers.SerializerMethodField(read_only=True)
    image = serializers.SerializerMethodField(read_only=True)
    description = serializers.SerializerMethodField(read_only=True)
    id_number = serializers.IntegerField(read_only=True)
    whatsapp_number = serializers.IntegerField(read_only=True)
    call_number = serializers.IntegerField(read_only=True)
    
    def get_introduction(self, instance):
        content = instance.introduction
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

    def get_image(self, obj):
        if obj.image:
            image = obj.image
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
    
    def get_description(self, instance):
        content = instance.description
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

###### List serializer #######
class ProjectsPageSerializer(serializers.Serializer):
    project_name = serializers.CharField(read_only=True)
    image = serializers.SerializerMethodField(read_only=True,source='project_image')
    project_description = serializers.SerializerMethodField(read_only=True)
    communities = serializers.CharField(read_only=True)
    developers = serializers.CharField(read_only=True)
    agent = AgentSerializer(read_only=True)
    floor_plan = serializers.FileField()
    slug = serializers.CharField(read_only=True)


    def get_image(self, obj):
        return obj.main_image_data
    
    def get_resized_image(self, obj):
        return obj.resized_image_data

    def get_project_description(self, instance):
        content = instance.project_description
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
    

#### Detailpage Serializer #######

class ProjectsDetailSerializer(ProjectsPageSerializer):
    content = serializers.SerializerMethodField()
    def get_content(self, obj):
        """
        Extracts the first content block of type 'content_block' from the given object's content stream,
        serializes its 'content' field, and returns the serialized data.
        """
        content_blocks = []
        for block in obj.content:
            print("=----block----=",block)
            datas = None
            print("------block.block_type------",block.block_type)
            if block.block_type == 'text_block':
                serializer = TextBlockSerializer(block.value, context=self.context)
                datas =  serializer.data
            elif block.block_type == 'about_block':
                serializer = AboutSerializer(block.value,context=self.context)
                datas = serializer.data
            elif block.block_type == 'photo_gallery_block':
                serializer = ImageBlockSerializer(block.value,context=self.context)
                datas = serializer.data
            elif block.block_type == 'card_block_with_link':
                serializer = CardWithLinkSerializer(block.value,context=self.context)
                datas = serializer.data
            elif block.block_type == 'text_card_block':
                serializer = TextCardSerializer(block.value,context=self.context)
                datas = serializer.data
            elif block.block_type == 'faq_block':
                serializer = FAQBlockSerializer(block.value,context=self.context)
                datas = serializer.data
            elif block.block_type == 'location_block':
                serializer = LocationBlockSerializer(block.value,context=self.context)
                datas = serializer.data
            elif block.block_type == 'amenities_block':
                serializer = AmenitiesBlockSerializer(block.value,context=self.context)
                datas = serializer.data
            elif block.block_type == 'floor_plan_block':
                serializer = FloorPlanBlockSerializer(block.value,context=self.context)
                datas = serializer.data