"""hacker_news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (login, logout)
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from django.conf.urls.static import static

from newsfeed.views import (
    NewsItemListView, NewsItemReadView, NewsItemDeleteView)
from user_management.views import RegistrationView

login_forbidden = user_passes_test(lambda u : u.is_anonymous(), '/posts/')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login_forbidden(login), name='login'),
    url(r'^accounts/register/$', login_forbidden(RegistrationView.as_view()), name='register'),
    url(r'^accounts/logout/$', login_required(logout), {'next_page': '/accounts/login/'}, name='logout'),
    url(r'^$', login_required(NewsItemListView.as_view()), name='main'),
    url(r'^posts/$', login_required(NewsItemListView.as_view()), name='post-list-view'),
    url(r'^post/read/$', login_required(NewsItemReadView.as_view()), name='read'),
    url(r'^post/delete/$', login_required(NewsItemDeleteView.as_view()), name='delete'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
