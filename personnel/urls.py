from django.urls import path
from . import views

urlpatterns = [
    path('', views.personel_list, name='personel_list'),
    path('ekle/', views.personel_create, name='personel_create'),
    path('<int:pk>/', views.personel_detail, name='personel_detail'),
    path('<int:pk>/duzenle/', views.personel_update, name='personel_update'),
    path('<int:pk>/sil/', views.personel_delete, name='personel_delete'),
]
