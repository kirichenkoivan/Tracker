from django.contrib import admin
from django.urls import path, include  # Импортируем include для включения URL-маршрутов из приложения
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # URL-маршруты для allauth
    path('login/', LoginView.as_view(), name='login'),  # URL для входа
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include('task_tracker.urls')),  # Включаем URL-маршруты из приложения task_tracker
]
