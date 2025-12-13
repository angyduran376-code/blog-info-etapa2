from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
    imagen = models.ImageField(upload_to='usuario/', null=True, blank=True, default='usuario/user-default.jpg')

    def get_absolute_url(self):
        return reverse('index')
        