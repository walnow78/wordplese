# -*- coding: utf-8 -*-
from rest_framework import serializers
from models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post


class PostListSerializer(PostSerializer):

    class Meta(PostSerializer.Meta):
        fields = ('id', 'title', 'created_at')
