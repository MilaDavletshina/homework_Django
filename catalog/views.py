from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy


def home(request):
    return render(request, 'home.html')


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')  # получаем имя
#         message = request.POST.get('message')  # получаем сообщение
#
#         return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
#     return render(request, 'contacts.html')


class Contacts(TemplateView):
    template_name = 'catalog/contacts.html'


class Message(TemplateView):
    template_name = 'catalog/message.html'


# def products_list(request):
#     product = Product.objects.all()
#     context = {'products': product}  #просто название переменной
#     return render(request, 'products_list.html', context)


class ProductListView(ListView):
    model = Product
#     catalog/product_list.html

# def products_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(request, 'product_detail.html', context)


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price')
    success_url = reverse_lazy('catalog:products_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price', 'created_at', 'updated_at')
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

