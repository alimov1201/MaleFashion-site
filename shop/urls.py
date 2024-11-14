from django.urls import path
from shop.views import shop, shop_detail

urlpatterns = [
    path('shop/', shop, name='shop'),
    path('product_detail/<int:id>', shop_detail, name='product_detail')
]