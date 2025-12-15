from .models import Categoria
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NuevaCategoriaForm
from django.urls import reverse_lazy

# Create your views here.
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria/categoria_list.html'
    context_object_name = 'categorias'

class CategoriaCreateView(LoginRequiredMixin, CreateView):

    model = Categoria
    form_class = NuevaCategoriaForm
    template_name = 'categoria/crear_categoria.html'
    success_url = reverse_lazy('apps.categoria:categoria_list')
    
    # def get_success_url(self):
    #     next_url = self.request.GET.get('next')
    #     if next_url:
    #         return next_url
    #     else:
    #         return reverse_lazy('apps.categoria:crear_post')
        
class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'categoria/categoria_confirm_delete.html'
    success_url = reverse_lazy('apps.categoria:categoria_list')