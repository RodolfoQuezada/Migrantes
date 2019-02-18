from django.db import models
from django.contrib.auth.models import User
from Migrantes.models import PerfilesDeUsuario
from embed_video.fields import EmbedVideoField

class Course(models.Model):
    titulo = models.CharField(max_length=100)
    estudiante = models.ManyToManyField(User, blank=True)
    slug = models.SlugField(null=False,default='')
    imagen = models.ImageField()
    descripcion = models.TextField(default='',max_length=300)

    def __str__(self):
        return self.titulo

    def recorte(self):
        return self.descripcion[:50] + '...'


class Unidad(models.Model):
    curso = models.ForeignKey(Course,on_delete=models.CASCADE,default='')
    nombre_unidad = models.CharField(max_length=40,default='')
    numero_unidad = models.IntegerField(default='')
    descripcion = models.TextField(max_length=240,default='')

    def __str__(self):
        return self.nombre_unidad

class Tema(models.Model):
    unidad = models.ForeignKey(Unidad,on_delete=models.CASCADE,default='')
    nombre_tema = models.CharField(max_length=50,default='')
    slug = models.SlugField(null=False,default='')  
    texto = models.TextField(max_length=500,default='')
    video = EmbedVideoField(default='')

    def __str__(self):
        return self.nombre_tema
    
class Anuncios(models.Model):
    curso = models.ForeignKey(Course,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=250)

    def __str__(self):
        return self.titulo

class CartaCompromiso(models.Model):
    titulo = models.CharField(max_length=40)
    cuerpo = models.TextField()

    def __str__(self):
        return self.titulo

    
class Preguntas(models.Model):
    curso = models.ForeignKey(Course,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200,default='')
    cuerpo = models.TextField(max_length=300,default='')
    respuesta = models.TextField(max_length=500,default='')


    def __str__(self):
        return self.titulo

