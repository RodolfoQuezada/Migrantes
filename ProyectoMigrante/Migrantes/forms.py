from django import forms
from .models import *
import datetime
from django.utils import timezone
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

elementos_civil = (

	('Unión Libre','Unión Libre'),
	('Casado(a)','Casado(a)'),
	('Divorciado(a)','Divorciado(a)'),
	('Viudo(a)','Viudo(a)'),
	('Soltero(a)', 'Soltero(a)'),
)

estudios = (

	('Primaria Trunca','Primaria Trunca'),
	('Primaria Terminada','Primaria Terminada'),
	('Secundaria Trunca','Secundaria Trunca'),
	('Secundaria Terminada','Secundaria Terminada'),
	('Bachillerato Trunco','Bachillerato Trunco'),
	('Bachillerato Terminado','Bachillerato Terminado'),
	('Universidad Trunca', 'Universidad Trunca'),
	('Universidad Terminada','Universidad Terminada'),

)

resp = (
		('Sí','Sí'),
		('No','No'),
	)

solo = (
		('Solo(a)','Solo(a)'),
		('Acompañado(a)','Acompañado(a)'),
	)

razon = (
	('Falta de empleo','Falta de empleo'),
	('Empleos con salarios bajos','Empleos con salarios bajos'),
	('Delincuencia o Crimen organizado','Delincuencia o Crimen organizado'),
	('Violencia intrafamiliar','Violencia intrafamiliar'),
	('Guerra','Guerra'),
	('Reunificación familiar','Reunificación familiar'),
	('Intolerancia a tu forma de pensar o identidad','Intolerancia a tu forma de pensar o identidad'),
)

cesfom = (
	('Formación escolar','Formación escolar'),
	('Cursos de oficios','Cursos de oficios'),
	('Cursos de formación de la fe','Cursos de formación de la fe'),

)

class datospersonales(forms.ModelForm):

	class Meta:
		model = PerfilesDeUsuario
		fields = ('username', 'password', 'nombre', 'apellido_Paterno','apellido_Materno',
		'fecha_nacimiento','estado_civil','fecha_ultima_deportacion','pais_ultima_deportacion',
		'pais_origen','estado_origen','escolaridad','pais_actual','estado_actual','ciudad_actual','fecha_llegada',
		'solo_acomp','familia_ciudad','com_familia','fam_OCiudad','com_Ofamilia',
		'ciudad_permanente','asiste_agrupacion','salir_origen','interes_CESFOM')
		
		labels = {

			'username': ('Correo Electronico'),
			'contraseña': ('Contraseña'),
			'nombre': ('Nombre(s)'),
			'apellido_Paterno': ('Apellido Paterno'),
			'apellido_Materno': ('Apellido Materno'),
			'fecha_nacimiento': ('Fecha de Nacimiento'),
			'escolaridad': ('Escolaridad'),
			'estado_civil': ('Estado Civil'),
			'pais_origen': ('País de Origen'),
			'estado_origen': ('Estado de Origen'),
			'escolaridad': ('Grado maximo de estudios'),
			'estado_civil': ('Estado Civil'),
			'fecha_ultima_deportacion': ('Fecha de su ultima deportación. Dejar en blanco si nunca ha sido deportado'),
			'pais_ultima_deportacion': ('¿País del que fue deportado en esa ocasión'),
			'pais_actual': ('¿En qué país se encuentra actualmente?'),
			'estado_actual':('¿En qué estado se encuentra actualmente?'),
			'ciudad_actual': ('¿En qué ciudad se encuentra actualmente?'),
			'fecha_llegada': ('Fecha en que llego a esta ciudad'),
			'solo_acomp': ('¿Llegó a esta ciudad solo o acompañado?'),
			'familia_ciudad': ('¿Tiene familia en esta ciudad?'),
			'com_familia': ('¿Mantiene comunicanión constante con esta familia?'),
			'fam_OCiudad': ('¿Tiene familia en otra ciudad?'),
			'com_Ofamilia': ('¿Mantiene comunicanión constante con esta familia?'),
			'ciudad_permanente': ('¿Piensa quedarse de forma permanente en esta ciudad?'),
			'asiste_agrupacion': ('¿Actualmente estas acudiendo de forma regular a alguna agrupación de cualquier tipo (religiosa, AA, NA, grupos de autoayuda, equipo deportivo, etcétera)?'),
			'salir_origen': ('¿Cuál de las siguientes es la razón principal por la que saliste de tu lugar de origen?'),
			'interes_CESFOM': ('¿Cuál es tu principal interés en cuanto a cursos del CESFOM?'),
		}

		help_texts = {
			'username': None,
		}

		widgets = {
			'username': forms.EmailInput(attrs={'class':'form-control','placeholder':'Introduce tu correo electronico*'}),
			'password': forms.PasswordInput(attrs={'class':'form-control','placeholder':'Crea una contraseña*'}),
			'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Introduce tu Nombre completo*'}),
			'apellido_Paterno': forms.TextInput(attrs={'class':'form-control','placeholder':'Introduce tu Apellido Paterno*'}),
			'apellido_Materno': forms.TextInput(attrs={'class':'form-control','placeholder':'Introduce tu Apellido Materno*'}),
			'fecha_nacimiento': forms.SelectDateWidget(years=range(1960,2001)),
			'escolaridad': forms.Select(choices=estudios),
			'estado_civil': forms.Select(choices=elementos_civil),
			'fecha_ultima_deportacion': forms.SelectDateWidget(years=range(1960,datetime.date.today().year + 1)),
			'ciudad_actual': forms.TextInput(attrs={'class':'form-control','placeholder':'Introduce una ciudad*'}),
			'fecha_llegada': forms.SelectDateWidget(years=range(1960,datetime.date.today().year + 1)),
			'solo_acomp': forms.Select(choices=solo),
			'familia_ciudad': forms.Select(choices=resp),
			'com_familia': forms.Select(choices=resp),
			'fam_OCiudad': forms.Select(choices=resp),
			'com_Ofamilia': forms.Select(choices=resp),
			'ciudad_permanente': forms.Select(choices=resp),
			'asiste_agrupacion': forms.Select(choices=resp),
			'salir_origen': forms.Select(choices=razon),
			'interes_CESFOM': forms.Select(choices=cesfom),
			}

		def __init__(self,*args,**kwargs):
			super().__init__(*args,**kwargs)
			self.fields['estado_origen'].queryset = Pais.objects.none()


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'form-control','placeholder': '*Introduce tu nombre de usuario'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder':'*Introduce tu contraseña'}))