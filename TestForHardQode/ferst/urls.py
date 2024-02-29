from django.urls import path
from .views import products_list,user_accessible_lessons


urlpatterns = [
    path('products/', products_list, name='products_list'),
    # Добавьте следующую строку для обработки уроков конкретного продукта
    path('products/<int:product_id>/lessons/', user_accessible_lessons, name='user_accessible_lessons'),
]
