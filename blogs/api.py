# -*- coding: utf-8 -*-
from blogs.models import Post
from blogs.serializers import PostDetailSerializer, PostListSerializer, BlogSerializer
from blogs.views import PostsQuerySet, PostsDetailQuerySet
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet, GenericViewSet


class BlogListAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = BlogSerializer

class PostViewSet(PostsQuerySet, PostsDetailQuerySet, ModelViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        if self.action == 'list':
            return self.get_posts_queryset(self.request)
        else:
            return self.get_post_detail_queryset(self.request)

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        else:
            return PostDetailSerializer


class PostListAPI(ListCreateAPIView, PostsQuerySet):

    permission_classes = (IsAuthenticatedOrReadOnly,)
    # Si el metodo es post uso PostSerializer porque PostListSerializer solamente
    # tiene 3 campos y daría error por los demás campos. Sobreescribo get_serializer_class

    def get_serializer_class(self):
        return PostDetailSerializer if self.request.method == "POST" else PostListSerializer

    # Dejo el usuario autentificado antes de guardar.
    def get_queryset(self):
        return self.get_posts_queryset(self.request)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetailAPI(RetrieveUpdateDestroyAPIView, PostsDetailQuerySet):
    serializer_class = PostDetailSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return self.get_posts_detail_queryset(self.request)

# Creación de un post con ViewSet

class CreatePostViewSet(CreateModelMixin, GenericViewSet):

    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # Meto el owner del usuario autentificado.
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

