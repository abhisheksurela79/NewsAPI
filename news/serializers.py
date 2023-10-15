from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'country_code', 
            'language', 
            'category', 
            'title', 
            'content', 
            'url_to_image', 
            'url', 
            'author', 
            'published_on', 
            'published_time_stamp'
            ]


    


