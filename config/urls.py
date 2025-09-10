from django.contrib import admin
from django.urls import path, include
from core.views import HomeView, home, register
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name='home'),
    path('accounts/register/', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('personel/', include('personel.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)