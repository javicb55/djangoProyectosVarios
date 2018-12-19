from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import os
# Create your models here.

SERIE_ELEGIR = (
        ('Nar', 'Naruto'),
        ('Dgb','Dragon Ball'),
        ('DeN', 'Death Note'),
        ('Opm', 'One Punch Man')
    )

PERSONAJE_ELEGIR = (
        ('Naruto','Naruto'),
        ('Saitama','Saitama')
    )


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    serie = models.CharField(max_length=3, choices=SERIE_ELEGIR)
    fecha_subida = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    frase = models.TextField()
    
    nombre_personaje = models.CharField(max_length=50, choices=PERSONAJE_ELEGIR)

    def __str__(self):
        return self.frase
