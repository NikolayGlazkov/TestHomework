from django.urls import path
from .views import products_list,product_access_list


urlpatterns = [
    path('products/', products_list, name='products_list'),
    # Добавьте следующую строку для обработки уроков конкретного продукта
    path('product_access/', product_access_list, name='product_access_list'),
]
