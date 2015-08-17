# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers
from models import Post

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post

class PostListSerializer(PostSerializer):

    class Meta(PostSerializer.Meta):
        fields = ('id', 'title', 'created_at')
