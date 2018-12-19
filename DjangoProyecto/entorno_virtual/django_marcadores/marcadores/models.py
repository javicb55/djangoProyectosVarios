from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Link(models.Model):
    url = models.URLField(unique=True)
    def __str__(self):
        return self.url

class Marcadores(models.Model):
    titulo = models.CharField(max_length=200)
    usuario = models.ForeignKey(User)
    link = models.ForeignKey(Link)
    def __str__(self):
        return '%s, %s,' % (self.usuario.usuario, self.link.url)

class Tag(models.Model):
    nombre = models.CharField(max_length=64, unique=True)
    marcadores = models.ManyToManyField(Marcadores)
    def __str__(self):
        return self.nombre  