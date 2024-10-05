from django.urls import path
from blogs.apps import BlogsConfig
from blogs.views import base, PostListView, PostDetailView


app_name = BlogsConfig.name


urlpatterns = [
    # path('', base, name='base.html'),
    path('', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail')
]