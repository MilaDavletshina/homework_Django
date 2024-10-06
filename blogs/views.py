from django.shortcuts import render
from blogs.models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def base(request):
    return render(request, 'base.html')


class PostListView(ListView):
    model = Post

#app_name/<model_name>_<action> т.е будет blogs/post_list.html


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('blogs:post_list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'content', 'preview')
    success_url = reverse_lazy('blogs:post_list')


class ProductDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blogs:post_list')