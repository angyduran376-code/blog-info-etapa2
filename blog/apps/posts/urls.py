from django.urls import path
from .views import *
from . import views

app_name = 'apps.posts'

urlpatterns = [
    path('posts/', PostListViews.as_view(), name='posts'),
    path("posts/<int:id>/", PostDetailView.as_view(), name="post_individual"),
    path('posts/crear/', PostCreateView.as_view(), name='crear_post'),
    # path('posts/crear/', post_crear, name='post_crear'),
    # path('posts/list/', lista_posts, name='lista_posts'),
    path('posts/categorias/', CategoriaCreateView.as_view(), name='crear_categoria'),
    path('posts/categorias/listar/', CategoriaListView.as_view(), name='categoria_list'),
    path('posts/categorias/eliminar/<int:pk>/', CategoriaDeleteView.as_view(), name='categoria_delete'),
    path('posts/<int:pk>/modificar/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/eliminar/', PostDeleteView.as_view(), name='post_delete'),
]
