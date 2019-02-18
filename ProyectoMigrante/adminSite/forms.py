from django import forms
from Cursos.models import *
import datetime
from django.utils import timezone
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.forms.widgets import PasswordInput, TextInput

class AgregarCurso(forms.ModelForm):
	class Meta:
		model = Course
		fields = ('titulo','slug','imagen','descripcion')
		labels = {
		'titulo': ('Nombre del curso'),
		'slug': ('Dirección del curso'),
		'imagen': ('Imagen descriptiva del curso'),
		'descripcion': ('Descripción del curso'),
		}
		widgets = {
		'titulo': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre del curso*'}),
		'slug': forms.TextInput(attrs={'class':'form-control','placeholder':'Dirección del curso*'}),
		'descripcion': forms.Textarea(attrs={'class':'form-control','placeholder':'Descripción del curso*'}),
		}

class AgregarUnidad(forms.ModelForm):
	class Meta:
		model = Unidad
		fields = ('curso','nombre_unidad','numero_unidad','descripcion')
		labels = {
			'curso': ('Nombre del curso'),
			'nombre_unidad': ('Nombre de la unidad'),
			'numero_unidad': ('Número de la unidad'),
			'descripcion': ('Descripción de la unidad'),
		}
		widgets = {
			'nombre_unidad': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre la unidad*'}),
			'numero_unidad': forms.NumberInput(attrs={'class':'form-control','placeholder':'Número la unidad*'}),
			'descripcion': forms.Textarea(attrs={'class':'form-control','placeholder':'Descripción del curso*'}),
		}

#class AgregarTema(forms.ModelForm):
#	class Meta:
#		model = Tema
#		fields =
#		labels = 
#		widgets = 


