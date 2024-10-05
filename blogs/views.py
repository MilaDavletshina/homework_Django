from django.shortcuts import render
from blogs.models import Post
from django.views.generic import ListView, DetailView


def base(request):
    return render(request, 'base.html')


class PostListView(ListView):
    model = Post

#app_name/<model_name>_<action> т.е будет blogs/post_list.html


class PostDetailView(DetailView):
    model = Post

