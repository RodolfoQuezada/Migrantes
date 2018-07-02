from . import views
from django.urls import path


app_name='migrantes'

urlpatterns = [
	path('registro/', views.registro, name='registrar'),
	path('inicio/', views.inicio, name='iniciar'),
	path('salir/', views.salir, name='salir'),
 ]