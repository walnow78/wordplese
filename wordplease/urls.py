from django.conf.urls import include, url
from django.contrib import admin
from blogs.views import HomeView, PostDetailView, BlogListView, BlogListDetailView, CreatePostView, PostCurrentUser
from rest_framework.routers import DefaultRouter
from users.views import LoginView, LogoutView, SignupView
from users.api import UserViewSet
from blogs.api import PostListAPI, PostDetailAPI, BlogListAPI, CreatePostViewSet
from django.contrib.auth.decorators import login_required

# APIRouter

router = DefaultRouter()

router.register(r'api/1.0/users', UserViewSet, base_name='user')

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
    url(r'^api/1.0/blogs/(?P<user>[A-Za-z0-9]+)$', PostListAPI.as_view(), name='blog_user_api'),
    url(r'^api/1.0/blogs/(?P<user>[A-Za-z0-9]+)/(?P<pk>[0-9]+)$', PostDetailAPI.as_view(), name='post_detail_api'),

    url(r'^api/1.0/post/new-post$', CreatePostViewSet, name='new_post_api'),

    # Users URL
    url(r'^login$', LoginView.as_view(), name='user_login'),
    url(r'^logout$', LogoutView.as_view(), name='user_logout'),
    url(r'^signup$', SignupView.as_view(), name='user_signup'),

    # User API

    url(r'', include(router.urls)),
]
