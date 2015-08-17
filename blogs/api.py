# -*- coding: utf-8 -*-
from blogs.models import Post
from blogs.serializers import PostSerializer, PostListSerializer
from blogs.views import PostsQuerySet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PostListAPI(ListCreateAPIView, PostsQuerySet):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # Si el metodo es post uso PostSerializer porque PostListSerializer solamente
    # tiene 3 campos y daría error por los demás campos. Sobreescribo get_serializer_class

    def get_serializer_class(self):
        return PostSerializer if self.request.method == "POST" else PostListSerializer

    def get_queryset(self):
        return self.get_posts_queryset(self.request)

class PostDetailAPI(RetrieveUpdateDestroyAPIView, PostsQuerySet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return self.get_posts_queryset(self.request)