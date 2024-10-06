from django.shortcuts import render
from blogs.models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse


def base(request):
    return render(request, 'base.html')


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


#app_name/<model_name>_<action> т.е будет blogs/post_list.html


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('blogs:post_list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'content', 'preview')
    success_url = reverse_lazy('blogs:post_list')

    def get_success_url(self):
        return reverse('blogs:post_detail', args=[self.kwargs.get('pk')])


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blogs:post_list')