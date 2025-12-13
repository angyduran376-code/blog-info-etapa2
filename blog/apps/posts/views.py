from django.shortcuts import render
from .models import Post, Comentario, Categoria
from django.views.generic import ListView, DetailView, CreateView
from .forms import ComentarioForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Create your views here.

#Vista basada en Funciones

#Vista basada en Clases
class PostListViews(ListView):
    model = Post
    template_name = "posts/posts.html"
    context_object_name ="posts"
    
class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_individual.html"
    context_object_name = "posts"
    pk_url_kwarg = "id"
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['form']= ComentarioForm() 
        context ['comentarios']=Comentario.objects.filter(posts_id=self.kwargs['id'])
        return context
    
    def post(self, request, *args, **kwargs):
        form = ComentarioForm(request.POST)
        if  form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.posts_id = self.kwargs['id']
            comentario.save()
            return redirect('apps.posts:post_individual', id=self.kwargs['id'])
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)
    
class ComentarioCreateView(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comentario/agregarComentario.html'
    success_url = ' comentario/comentarios/'
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.posts_id = self.kwargs['posts_id']
        return super().form_valid(form)

def post_crear(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        subtitulo = request.POST.get("subtitulo")
        texto = request.POST.get("texto")
        categoria_id = request.POST.get("categoria")
        imagen = request.FILES.get("imagen")  # importante para ImageField

        categoria = Categoria.objects.get(id=categoria_id) if categoria_id else None

        Post.objects.create(
            titulo=titulo,
            subtitulo=subtitulo,
            texto=texto,
            categoria=categoria,
            imagen=imagen
        )

        # Mensaje de éxito
        messages.success(request, "¡Post creado con éxito!")

        # Redirige a la vista que muestra todos los posts
        return redirect('apps.posts:posts')

    categorias = Categoria.objects.all()
    return render(request, "posts/crear_post.html", {"categorias": categorias})

def lista_posts(request):

    posts = Post.objects.all().order_by('-publicado')
    return render(request, 'posts/lista_posts.html', {'posts': posts})