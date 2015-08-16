from django.conf.urls import include, url
from django.contrib import admin
from blogs.views import HomeView, PostDetailView
from users.views import LoginView, LogoutView, SignupView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Posts
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^posts/(?P<pk>[0-9]+)$', PostDetailView.as_view(), name='post'),

        # Users URL

    url(r'^login$', LoginView.as_view(), name='user_login'),
    url(r'^logout$', LogoutView.as_view(), name='user_logout'),
    url(r'^signup$', SignupView.as_view(), name='user_signup'),
]
