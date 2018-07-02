from django.urls import path, re_path
from . import views

app_name='admin'

urlpatterns = [

	path('', views.home, name='home'),
	path('agregar/', views.vista_agregar, name='agregar'),

]