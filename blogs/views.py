# -*- coding: utf-8 -*-
from blogs.forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from blogs.models import Post
from django.utils.decorators import method_decorator
from django.views.generic import View, ListView
from django.contrib.auth.models import User

class PostCurrentUser(ListView):
    model = Post
    template_name ='blogs/posts_current_user.html'

    def get_queryset(self):
        queryset = super(PostCurrentUser, self).get_queryset()
        return queryset.filter(owner=self.request.user)

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

class CreatePostView(View):

    @method_decorator(login_required())
    def get(self, request):

        success_message = ''
        form = PostForm()

        context = {
            'form': form,
            'success_message': success_message
        }

        return render(request, 'blogs/post_create.html', context)

    @method_decorator(login_required())
    def post(self, request):
        success_message = ''

        # Creo un post vacío con el usuario para pasarselo al formulario
        # De este modo oculto el campo owner y lo cargo automaticamente.
        post_with_owner = Post()
        post_with_owner.owner = request.user
        form = PostForm(request.POST, instance=post_with_owner)

        if form.is_valid():
            # Creo el post con los datos del formulario y lo almaceno en nueva new_post
            new_post = form.save()
            form = PostForm()
            success_message = 'Guardado con exito!'
            success_message += '<a href="{0}">'.format(reverse('post', args=[new_post.pk]))
            success_message += 'Ver post'
            success_message += '</a>'

        context = {
            'form': form,
            'success_message': success_message
        }

        return render(request, 'blogs/post_create.html', context)