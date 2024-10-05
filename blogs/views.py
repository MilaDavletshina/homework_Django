from django.shortcuts import render
from blogs.models import Post
from django.views.generic import ListView


def base(request):
    return render(request, 'base.html')


class PostListView(ListView):
    model = Post