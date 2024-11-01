from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from catalog.forms import ProductForm, ProductModeratorForm
# from django.http import HttpResponse
from catalog.models import Product, Category
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from django.urls import reverse_lazy

from catalog.services import get_products_from_cash, get_products_by_category


def home(request):
    """ Главная страница """
    return render(request, "home.html")


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')  # получаем имя
#         message = request.POST.get('message')  # получаем сообщение
#
#         return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
#     return render(request, 'contacts.html')


class Contacts(TemplateView):
    """ Страница контакты """
    template_name = "catalog/contacts.html"


class CategoryListView(ListView):
    """ Страница категории """
    model = Category
    template_name = "catalog/category.html"


class ProductsByCategoryView(ListView):
    def get_queryset(self):
        """Функция получения category_id"""
        category_id = self.get('category_id')
        return get_products_by_category(category_id=category_id)


class Message(TemplateView):
    """ Страница полученное сообщение """
    template_name = "catalog/message.html"


# def products_list(request):
#     product = Product.objects.all()
#     context = {'products': product}  #просто название переменной
#     return render(request, 'products_list.html', context)


class ProductListView(ListView):
    """ Страница с продуктами """
    model = Product
#     catalog/product_list.html

    def get_queryset(self):
        return get_products_from_cash()


# def products_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(request, 'product_detail.html', context)


class ProductDetailView(DetailView):
    """ Страница детальное описание продукта """
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.save()
            return self.object
        raise PermissionDenied


class ProductCreateView(LoginRequiredMixin, CreateView):
    """ Страница создание нового продукта """
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """ Страница редактирование продукта """
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy("catalog:products_list")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.save()
            return self.object
        raise PermissionDenied

    def get_form_class(self):
        user = self.request.user
        # if user == self.object.owner:
        #     return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        # raise PermissionDenied('У Вас отсутствуют права, обратитесь к администратору!')
        return ProductForm


class ProductDeleteView(DeleteView):
    """ Страница удаление продукта """
    model = Product
    success_url = reverse_lazy("catalog:products_list")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.save()
            return self.object
        raise PermissionDenied


