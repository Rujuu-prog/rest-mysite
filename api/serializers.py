from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)
    class Meta:
        model = Blog
        fields = ('id', 'title', 'img', 'text','created_on')
