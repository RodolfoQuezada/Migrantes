from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import *
from django.http import HttpResponse

def registro(request):
	register = False

	if request.method=="POST":
		usuario = datospersonales(data=request.POST)
		if usuario.is_valid():
			usuario = usuario.save()
			usuario.set_password(usuario.password)
			usuario.save()

			registered=True

			return redirect('home')

	else:
		usuarioform = datospersonales()
	return render(request,'Migrantes/registro.html',{'datospersonales': datospersonales})


def inicio(request):
	if request.method=='POST':
		form = CustomAuthForm(data=request.POST)
		if form.is_valid():
			usuario = form.get_user()
			login(request,usuario)

			return redirect('cursos:homepage')
	else:
		form = CustomAuthForm()
	return render(request,'Migrantes/login.html',{'form':form})

def salir(request):
	if request.method=='POST':
		logout(request)
		return redirect('home')