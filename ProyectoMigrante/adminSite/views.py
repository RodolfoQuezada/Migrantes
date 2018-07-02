from django.shortcuts import render
from .forms import *

def home(request):
	return render(request,'adminSite/home.html')


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
