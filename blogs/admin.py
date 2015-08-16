# -*- coding: utf-8 -*-
from django.contrib import admin
from blogs.models import Post, Category

admin.site.register(Category)
admin.site.register(Post)
