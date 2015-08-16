# -*- coding: utf-8 -*-
from blogs.models import Post
from blogs.serializers import PostSerializer, PostListSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PostListAPI(ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # Si el metodo es post uso PostSerializer porque PostListSerializer solamente
    # tiene 3 campos y daría error por los demás campos. Sobreescribo get_serializer_class

    def get_serializer_class(self):
        return PostSerializer if self.request.method == "POST" else PostListSerializer



class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
