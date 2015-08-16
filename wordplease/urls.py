from django.conf.urls import include, url
from django.contrib import admin
from blogs.views import HomeView, PostDetailView, BlogListView, BlogListDetailView, CreatePostView, PostCurrentUser
from users.views import LoginView, LogoutView, SignupView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Blogs

    url(r'^blogs/$', BlogListView.as_view(), name='blog_list'),
    url(r'^blogs/(?P<user>[A-Za-z0-9]+)$', BlogListDetailView.as_view(), name='blog_list_detail'),

    # Posts
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^posts/(?P<pk>[0-9]+)$', PostDetailView.as_view(), name='post'),
    url(r'^posts/new$', CreatePostView.as_view(), name='post_create'),
    url(r'^myposts/$', login_required(PostCurrentUser.as_view()), name='posts_current_user'),
    # Users URL

    url(r'^login$', LoginView.as_view(), name='user_login'),
    url(r'^logout$', LogoutView.as_view(), name='user_logout'),
    url(r'^signup$', SignupView.as_view(), name='user_signup'),
]
