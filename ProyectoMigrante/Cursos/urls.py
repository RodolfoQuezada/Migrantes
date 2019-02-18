from django.urls import path, re_path
from . import views

app_name='cursos'

urlpatterns = [
    path('', views.index, name='homepage'),
    path('profile/', views.profile, name='profile'),
    path('courses/', views.courses, name='courses'),
    path('aceptar/', views.aceptarTerminos, name='aceptar'),
    path('registro/', views.registrarUsuario ,name='registro'),
	re_path('curso/(?P<slug>[\w-]+)/$', views.course_detail, name='detalle'),
	re_path('(?P<slug>[-\w]+)/$', views.tema_detalle, name='detalleTema'),

]