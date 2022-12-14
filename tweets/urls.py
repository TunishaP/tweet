from django.urls import path #
from . import views#
from django.urls.resolvers import URLPattern#
from sys import path_hooks
from typing import Pattern
from django import urls

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:tweet_id>/', views.delete, name='delete'),
    path('edit/<int:tweet_id>/', views.edit, name='edit'),
    path('like/<int:tweet_id>/', views.LikeView, name='like_tweet'),
]