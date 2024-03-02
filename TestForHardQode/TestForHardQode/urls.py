from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('ferst/', include('ferst.urls')),  # Подключите URL-шаблоны вашего приложения ferst
]