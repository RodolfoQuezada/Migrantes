from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *


@login_required(login_url="migrantes:iniciar")
def index(request):
  usuario = request.user
  context = {
    "courses": Course.objects.exclude(estudiante__exact=usuario),
    "carta": CartaCompromiso.objects.get(),
    }
  return render(request, 'Cursos/home.html', context)

@login_required(login_url="migrantes:iniciar")
def course_detail(request,slug):
    curso = Course.objects.get(slug=slug)
    unidades = Unidad.objects.filter(curso=curso).order_by('numero_unidad')
    anuncios = Anuncios.objects.filter(curso=curso)
    temas = Tema.objects.filter(unidad__in=unidades)
    preguntas = Preguntas.objects.filter(curso=curso)
    return render(request,'Cursos/curso.html',{'curso':curso,'unidades':unidades,
      'anuncios':anuncios,'temas':temas, 'preguntas':preguntas})

@login_required(login_url="migrantes:iniciar")
def tema_detalle(request,slug):
  video = Tema.objects.get(slug=slug)
  return render(request,'Cursos/contenido.html',{'video':video})

@login_required(login_url="migrantes:iniciar")
def profile(request):
  return render(request, 'Cursos/profile.html')

@login_required(login_url="migrantes:iniciar")
def courses(request):
  usuario = request.user
  cursos = Course.objects.filter(estudiante__exact=usuario)
  return render(request, 'Cursos/courses.html', {'cursos':cursos})

@login_required(login_url="migrantes:iniciar")
def registrarUsuario(request):
  if request.method == 'POST':
    cursoID = request.POST.get('cursoid', '')
    usuario = request.user
    curso = Course.objects.get(id=cursoID)
    curso.estudiante.add(usuario)
    
    return redirect('cursos:courses')

@login_required(login_url="migrantes:iniciar")
def aceptarTerminos(request):
  if request.method=='POST':
    usuario = request.user
    perfil = PerfilesDeUsuario.objects.get(username=usuario)
    perfil.terminos = True
    perfil.save()

    return redirect('cursos:homepage')

def tipo_usuario(request):
  usuario = request.user
  tipo = PerfilesDeUsuario.objects.get(username=usuario)
  return render(request,'Cursos/navbar.html',{'tipo':tipo})