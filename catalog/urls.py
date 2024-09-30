from django.urls import path
from . import views
from catalog.views import products_list


app_name = 'catalog'


urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('', products_list)
]

path('', products_list, name='products_list'),
# path('catalog/<int:pk>/', products_detail, name='products_detail'),
