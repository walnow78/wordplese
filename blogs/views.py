# -*- coding: utf-8 -*-
from django.http import HttpResponseNotFound
from django.shortcuts import render
from blogs.models import Post
from django.views.generic import View, ListView
from django.contrib.auth.models import User

class HomeView(View):

    def get(self, request):
        posts = Post.objects.all().order_by('-publication_date')

        context = {
            'post_list': posts[:5]
        }

        return render(request, 'blogs/home.html', context)

class PostDetailView(View):
    def get(self, request, pk):
        # optimizo la consulta para que traiga tanto el post como el usuario haciendo el join a la bd
        possible_post = Post.objects.filter(pk=pk).select_related('owner')

        post = possible_post[0] if len(possible_post) == 1 else None

        if post is not None:
            context = {
                'post': post
            }
            return render(request, 'blogs/post_detail.html', context)
        else:
            return HttpResponseNotFound("No existe el post")

class BlogListView(View):
    def get(self, request):
        blogs = User.objects.all()
        context = {
            "blogs" : blogs
        }
        return render(request, 'blogs/blogs.html', context)

class BlogListDetailView(View):
    def get(self, request, user):
        possible_posts = Post.objects.filter(owner__username=self.kwargs['user'])

        context = {
            'post_list': possible_posts
        }

        return render(request, 'blogs/home.html', context)
