from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Product


# Create your views here.
def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')  # получаем имя
        message = request.POST.get('message')  # получаем сообщение

        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
    return render(request, 'catalog/contacts.html')


def products_list(request):
    product = Product.objects.all()
    context = {'catalog': product}
    return render(request, 'products_list.html', context)


# def products_detail(request, pk):
#     product = get_object_or_404(pk=pk)
#     context = {'catalog': product}
#     return render(request, 'products_detail.html', context)