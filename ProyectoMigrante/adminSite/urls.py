from django.urls import path, re_path
from . import views

app_name='admin'

urlpatterns = [

	path('', views.home, name='home'),
	path('agregar/', views.vista_agregar, name='agregar'),
	path('editarCurso/', views.vista_cursos, name="cursos"),
	path('editarUsuario/', views.vista_usuarios, name='usuarios'),
	path('guardarCambiosUsuario/', views.guardar_cambios_usuario, name="guardar_usuario"),
	re_path('editar/usuario/(?P<id>[\w-]+)/$', views.vista_editar_usuarios, name='usuario'),
	re_path('editar/curso/(?P<id>[\w-]+)/$', views.vista_editar_curso,name="curso"),

]