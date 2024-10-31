from config.settings import CACHE_ENABLED
from catalog.models import Product
from django.core.cache import cache


def get_products_from_cash():
    """Получает данные по товарам из кэша, если кэш пуст, получает данные из бд"""
    if not CACHE_ENABLED:
        return Product.objects.all()

    key = "products_list"
    products = cache.get(key)

    if products is not None:
        return products

    products = Product.object.all()
    cache.set(key, products)

    return products