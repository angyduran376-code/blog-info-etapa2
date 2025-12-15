from django.urls import path
from . import views

app_name='apps.categoria'

urlpatterns = [
    path('categorias/', views.CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/crear', views.CategoriaCreateView.as_view(), name='crear_categoria'),
    path('categorias/eliminar/<int:pk>/', views.CategoriaDeleteView.as_view(), name='categoria_delete'),
]