from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)
    content = serializers.SerializerMethodField() 
    class Meta:
        model = Blog
        fields = ('id', 'title', 'img', 'text', 'content', 'created_on')
    
    def get_content(self, obj):
        return obj.convert_markdown_to_html()
