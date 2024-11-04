from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    Contacts,
    Message,
    CategoryListView, ProductsByCategoryListView,

)
from . import views

app_name = CatalogConfig.name


urlpatterns = [
    path("", cache_page(60)(ProductListView.as_view()), name="products_list"),
    path("products/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="products_detail"),
    path("products/create", ProductCreateView.as_view(), name="products_create"),
    path(
        "products/<int:pk>/update/", ProductUpdateView.as_view(), name="products_update"
    ),
    path(
        "products/<int:pk>/delete/", ProductDeleteView.as_view(), name="products_delete"
    ),
    path("contacts/", Contacts.as_view(), name="contacts"),
    path("message/", Message.as_view(), name="message"),
    path("category/", CategoryListView.as_view(), name="category"),
    path('category/<str:category_name>/', ProductsByCategoryListView.as_view(), name='products_by_category'),
]


