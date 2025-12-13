from django.urls import path
from .views import PostListViews, PostDetailView, post_crear, lista_posts
from . import views

app_name = 'apps.posts'

urlpatterns = [
    path('posts/', PostListViews.as_view(), name='posts'),
    path("posts/<int:id>/", PostDetailView.as_view(), name="post_individual"),
    path('posts/crear/', post_crear, name='post_crear'),
    path('posts/list/', lista_posts, name='lista_posts'),
]
