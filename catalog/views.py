from django.shortcuts import render
from catalog.forms import ProductForm
# from django.http import HttpResponse
from catalog.models import Product
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from django.urls import reverse_lazy


def home(request):
    """ Главная страница"""
    return render(request, "home.html")


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')  # получаем имя
#         message = request.POST.get('message')  # получаем сообщение
#
#         return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
#     return render(request, 'contacts.html')


class Contacts(TemplateView):
    """ Страница контакты"""
    template_name = "catalog/contacts.html"


class Message(TemplateView):
    """ Страница полученное сообщение"""
    template_name = "catalog/message.html"


# def products_list(request):
#     product = Product.objects.all()
#     context = {'products': product}  #просто название переменной
#     return render(request, 'products_list.html', context)


class ProductListView(ListView):
    """ Страница с продуктами"""
    model = Product


#     catalog/product_list.html

# def products_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(request, 'product_detail.html', context)


class ProductDetailView(DetailView):
    """ Страница детальное описание продукта"""
    model = Product


class ProductCreateView(CreateView):
    """ Страница создание нового продукта"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy("catalog:products_list")


class ProductUpdateView(UpdateView):
    """ Страница редактирование продукта"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy("catalog:products_list")


class ProductDeleteView(DeleteView):
    """ Страница удаление продукта"""
    model = Product
    success_url = reverse_lazy("catalog:products_list")
