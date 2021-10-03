from rest_framework import viewsets
from api.permissions import IsAdminOrReadOnly 
from . import serializers
from .models import Blog

#投稿に対するview
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.filter(is_public=True)
    # queryset = Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = (IsAdminOrReadOnly,) 

    