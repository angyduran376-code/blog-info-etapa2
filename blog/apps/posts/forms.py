from django import forms
from .models import Comentario, Post

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={
                'class': 'form-control comentario-textarea',
                'rows': 6,
                'placeholder': 'Editá tu comentario...'
            })
        }
        labels = {
            'texto': ''
        }

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

