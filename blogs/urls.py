from django.urls import path
from blogs.apps import BlogsConfig
from blogs.views import base, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


app_name = BlogsConfig.name


urlpatterns = [
    # path('', base, name='base.html'),
    path('', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete')
]

