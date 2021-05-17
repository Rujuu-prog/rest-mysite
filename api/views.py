from rest_framework import viewsets
from . import serializers
from .models import Blog

#投稿に対するview
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogSerializer

    def perform_create(self, serializer):
        serializer.save(userPost=self.request.user)