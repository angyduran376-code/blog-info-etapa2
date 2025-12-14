from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def pagina_404(request, exception):
    return HttpResponseNotFound('<h1>Página no encontrada</h1>')


