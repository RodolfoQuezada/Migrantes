from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django_countries.fields import CountryField

class Pais(models.Model):
    nombre_pais = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_pais


class Estado(models.Model):
    pais = models.ForeignKey(Pais,on_delete=models.CASCADE)
    nombre_estado = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_estado

class PaisDeportado(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Tipo_Usuario(models.Model):
    tipo = models.CharField(max_length=20,default='')

    def __str__(self):
        return self.tipo


class PerfilesDeUsuario(User):

    #auto fields
    fecha_registro = models.DateField(auto_now_add=True)
    referencia = models.AutoField(primary_key=True)

    #datos personales
    nombre = models.CharField(max_length=40)
    apellido_Paterno = models.CharField(max_length=40)
    apellido_Materno = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField(default='')
    pais_origen = models.ForeignKey(Pais,on_delete=models.CASCADE)
    estado_origen = models.ForeignKey(Estado,on_delete=models.CASCADE)
    escolaridad = models.CharField(max_length=100) 
    estado_civil = models.CharField(max_length=100) 
    terminos = models.BooleanField(default=False)

    #deportaciones
    
    fecha_ultima_deportacion = models.DateField(null=True,blank=True,default="") 
    pais_ultima_deportacion = models.ForeignKey(PaisDeportado,on_delete=models.CASCADE)
    pais_actual = models.ForeignKey(Pais,on_delete=models.CASCADE,related_name='pais_actual')
    estado_actual = models.ForeignKey(Estado,on_delete=models.CASCADE,related_name='estado_actual')
    ciudad_actual = models.CharField(max_length=100)

    #preguntas variadas
    
    fecha_llegada = models.DateField(max_length=40,default='')
    solo_acomp = models.CharField(max_length=40,default='')
    familia_ciudad = models.CharField(max_length=40,default='')
    com_familia = models.CharField(max_length=40,default='')
    fam_OCiudad = models.CharField(max_length=40,default='')
    com_Ofamilia = models.CharField(max_length=40,default='')
    ciudad_permanente = models.CharField(max_length=40,default='')
    asiste_agrupacion = models.CharField(max_length=40,default='')
    salir_origen = models.CharField(max_length=40,default='')
    interes_CESFOM = models.CharField(max_length=40,default='')

    #categoria
    tipo = models.CharField(max_length=40, default='Estudiante')

    def __str__(self):
        return '%s %s' % (self.referencia, self.nombre)
