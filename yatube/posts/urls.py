from unicodedata import name
from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.index, name = 'main_list'),
    path('group/<slug:slug>/', views.group_posts, name = 'group_info'),
]