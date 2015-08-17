from django.conf.urls import include, url
from django.contrib import admin
from blogs.views import HomeView, PostDetailView, BlogListView, BlogListDetailView, CreatePostView, PostCurrentUser
from users.views import LoginView, LogoutView, SignupView
from users.api import UserListAPI, UserDetailAPI
from blogs.api import BlogUserApi, PostDetailAPI, BlogListAPI
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),

    # Blogs
    url(r'^blogs/$', BlogListView.as_view(), name='blogs_list'),
    url(r'^blogs/(?P<user>[A-Za-z0-9]+)$', BlogListDetailView.as_view(), name='blog_user'),
    url(r'^blogs/(?P<user>[A-Za-z0-9]+)/(?P<pk>[0-9]+)$', PostDetailView.as_view(), name='post_detail'),

    # Posts
    url(r'^new-post$', CreatePostView.as_view(), name='new_post'),

    # Blogs API
    url(r'^api/1.0/blogs/$', BlogListAPI.as_view(), name='post_list_api'),
    url(r'^api/1.0/blogs/(?P<user>[A-Za-z0-9]+)$', BlogUserApi.as_view(), name='blog_user_api'),
    url(r'^api/1.0/blogs/(?P<user>[A-Za-z0-9]+)/(?P<pk>[0-9]+)$', PostDetailAPI.as_view(), name='post_detail_api'),

    # Users URL

    url(r'^login$', LoginView.as_view(), name='user_login'),
    url(r'^logout$', LogoutView.as_view(), name='user_logout'),
    url(r'^signup$', SignupView.as_view(), name='user_signup'),

    # User API

    url(r'^api/1.0/users/$', UserListAPI.as_view(), name='user_list_api'),
    url(r'^api/1.0/users/(?P<pk>[0-9]+)$', UserDetailAPI.as_view(), name='user_detail_api'),
]
