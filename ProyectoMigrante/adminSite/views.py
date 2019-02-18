from django.shortcuts import render, redirect
from .forms import *
from Migrantes.models import PerfilesDeUsuario
from django.contrib.auth.decorators import login_required
from Migrantes.forms import *
from Cursos.models import *

@login_required(login_url="migrantes:iniciar")
def home(request):
	return render(request,'adminSite/home.html')

@login_required(login_url="migrantes:iniciar")
def vista_agregar(request):
	if request.method=="POST":
		curso = AgregarCurso(data=request.POST)
		unidad = AgregarUnidad(data=request.POST)
		if curso.is_valid():
			if unidad.is_valid():
				unidad = unidad.save(commit=False)
				curso = curso.save()

				return redirect('adminSite:home')

	else:
		cursoForm = AgregarCurso()
		unidadForm = AgregarUnidad()
	return render(request,'adminSite/agregarCurso.html',{'AgregarCurso':AgregarCurso,'AgregarUnidad':AgregarUnidad})

@login_required(login_url="migrantes:iniciar")
def vista_usuarios(request):
	usuarios = PerfilesDeUsuario.objects.all()
	return render(request,'adminSite/editarUsuarios.html',{'usuarios':usuarios})

@login_required(login_url="migrantes:iniciar")
def vista_cursos(request):
	cursos = Course.objects.all()
	return render(request,'adminSite/editarCursos.html',{'cursos':cursos})

@login_required(login_url="migrantes:iniciar")
def vista_editar_curso(request,id):
	curso = Course.objects.get(id=id)
	return render(request,'adminSite/editarDatosCurso.html',{'curso':curso})

def guardar_cambios_usuario(request):
	if request.method=="POST":
		datos_usuario = request.POST.getlist('userData[]')
		userId = request.POST.get('userId')
		usuario = PerfilesDeUsuario.objects.get(id=userId)

		PerfilesDeUsuario.objects.filter(id=userId).update(**datos_usuario)

		return redirect('admin:usuarios')

@login_required(login_url="migrantes:iniciar")
def vista_editar_usuarios(request,id):
	usuario = PerfilesDeUsuario.objects.get(id=id)


	return render(request,'adminSite/editarDatosUsuario.html',{'usuario':usuario})
