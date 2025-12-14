from django import forms
from .models import Comentario, Post, Categoria

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']

# class CrearPostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = '__all__'
#         widgets = {
#             'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del post'}),
#             'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Contenido del post...'}),
#         }

class CrearPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'titulo',
            'subtitulo',
            'texto',
            'categoria',
            'imagen',
        ]

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título del post'
            }),
            'subtitulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subtítulo (opcional)'
            }),
            'texto': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 8,
                'placeholder': 'Escribí el contenido del post...'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

class NuevaCategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la categoría'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descripción de la categoría...'}),
        }