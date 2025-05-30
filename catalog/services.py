from django.core.cache import cache
from .models import Product

def get_products_by_category(category_id):
    cache_key = f"products_category_{category_id}"
    products = cache.get(cache_key)
    if products is None:
        products = list(Product.objects.filter(category_id=category_id, is_published=True))
        cache.set(cache_key, products, 60 * 10)  # 10 минут, можно изменить время
    return products
