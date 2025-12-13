from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.urls import reverse_lazy

# Create your views here.

class RegistrarUsuario(CreateView):
    template_name = 'registration/registrar.html'
    form_class = RegistroUsuarioForm

    def form_valid(self, form):
        messages.success(self.request, 'Registro exitoso, por fvor, inicia sesion.')
        form.save()
        return redirect('apps.usuario:registrar')

class LoginUsuario(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        messages.success(self.request, 'Login exitoso')
        #return reverse_lazy('index')
        #return  reverse('apps.usuario:login')
        return  reverse('index')
"""
###########################################codigo de arriba sustituido por el de abajo
class LoginUsuario(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Login exitoso")
        return response

    def get_success_url(self):
        return reverse_lazy('index')
########################################### fin codigo sustituto"""


class LogoutUsuario(LogoutView):
    template_name = 'registration/logout.html'

    def get_success_url(self):
        messages.success(self.request, 'Logout exitoso')

        #return reverse('apps.usuario:logout')
        return reverse('index')
"""  
class LogoutUsuario(LogoutView):
    next_page = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Logout exitoso")
        return super().dispatch(request, *args, **kwargs)"""