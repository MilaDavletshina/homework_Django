from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, products_detail, contacts


app_name = CatalogConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('products/<int:pk>/', products_detail, name='products_detail'),
    path('contacts/', contacts, name='contacts')
]

