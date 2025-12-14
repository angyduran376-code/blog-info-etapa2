from django.urls import path
from .views import *

app_name = 'apps.posts'

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:id>/', PostDetailView.as_view(), name='post_individual'),
    path('posts/crear/', PostCreateView.as_view(), name='crear_post'),
    path('posts/categorias/', CategoriaCreateView.as_view(), name='crear_categoria'),
    path('posts/categorias/listar/', CategoriaListView.as_view(), name='categoria_list'),
    path('posts/categorias/eliminar/<int:pk>/', CategoriaDeleteView.as_view(), name='categoria_delete'),

]
