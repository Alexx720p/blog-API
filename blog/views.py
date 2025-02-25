from rest_framework import viewsets, filters
from .serializer import PostSerializer
from .models import Post

class PostView(viewsets.ModelViewSet):
    serializer_class=PostSerializer
    queryset=Post.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content', 'tags']

