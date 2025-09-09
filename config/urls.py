from django.contrib import admin
from django.urls import path, include
from core.views import HomeView, home, register

urlpatterns = [
    path('', home, name='home'),
    path('accounts/register/', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]