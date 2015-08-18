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

        # Hago que los campos owner, id, created_at y modified_at sean
        # de solo lectura así no es necesario pasarlos en POST y PUT.
        # El campo owner lo inserto en api con el usuario autentificado.

        read_only_fields = ('owner', 'id', 'created_at', 'modified_at')

class PostListSerializer(PostSerializer):

    class Meta(PostSerializer.Meta):
        fields = ('id', 'title', 'created_at')
