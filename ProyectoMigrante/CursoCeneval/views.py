from django.shortcuts import render
from Cursos.models import *
from django.views.generic import ListView


def home(request):
	return render(request,'home.html')

class NuestrosCursos(ListView):
	template_name = 'nuestros_cursos.html' 
	model = Course
	paginate_by = 3

