from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import Group

from .models import Usuario
from apps.posts.models import Post, Comentario



from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class RegistrarUsuario(CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'registration/registrar.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Usuario registrado exitosamente. Por favor Inicie sesión.")
        group=Group.objects.get(name='Registrado')
        self.object.groups.add(group)
        form.save()
        return redirect('apps.usuario:registrar')

class LoginUsuario(LoginView):
    template_name = 'registration/login.html'
    
    def get_success_url(self):
        messages.success(self.request, "Inicio de sesión exitoso.")
        return reverse('apps.usuario:login')

class LogoutUsuario(LogoutView):
    template_name = 'registration/logout.html'
    def get_success_url(self):
        messages.success(self.request, "Cierre de sesión exitoso.")
        return reverse('apps.usuario:logout')

class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = 'registration/usuario_list.html'
    context_object_name = 'usuarios'

    def get_queryset(self):
        queryset= super().get_queryset()
        queryset = queryset.exclude(is_superuser=True)
        return queryset

class UsuarioDetailView(LoginRequiredMixin, DetailView):
    model = Usuario
    template_name = 'usuario/eliminar_usuario.html'
    success_url = reverse_lazy('apps.usuario:usuario_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        colaborador_group= Group.objects.get(name='Colaborador')
        es_colaborador= colaborador_group in self.object.groups.all()
        context['es_colaborador']= es_colaborador
        
        return context       
    def post(self, request, *args, **kwargs):
        eliminar_comentarios= request.POST.get('eliminar_comentario',False)
        eliminar_post= request.POST.get('eliminar_post',False)
        self.object= self.get_object()

        if eliminar_comentarios:
            Comentario.objects.filter(usuario=self.object).delete()

        if eliminar_post:
            Post.objects.filter(autor=self.object).delete()
            messages.success(request, f'Usuario {self.object.username} y sus posts eliminados exitosamente.')
        return redirect('apps.usuario:usuario_list')
    
class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Usuario
    template_name = 'usuario/eliminar_usuario.html'
    success_url = reverse_lazy('apps.usuario:usuario_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        colaborador_group = Group.objects.get(name='Colaborador')
        es_colaborador = colaborador_group in self.object.groups.all()
        context['es_colaborador'] = es_colaborador 
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        eliminar_comentarios = request.POST.get('eliminar_comentarios', False)
        eliminar_post = request.POST.get('eliminar_posts', False)
        
        if eliminar_comentarios:
            Comentario.objects.filter(usuario=self.object).delete()
        
        if eliminar_post:
            Post.objects.filter(autor=self.object).delete()
                
        messages.success(request,f'Usuario {self.object.username} y sus datos eliminados exitosamente.')
        
        return self.delete(request, *args, **kwargs)