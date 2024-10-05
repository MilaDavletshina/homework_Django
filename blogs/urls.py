from django.urls import path
from blogs.apps import BlogsConfig
from blogs.views import base, PostListView


app_name = BlogsConfig.name


urlpatterns = [
    path('', base, name='base'),
    path('', PostListView.as_view(), name='post_list')
]