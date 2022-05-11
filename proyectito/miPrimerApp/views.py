from django.shortcuts import render
#agrgamos esta linea
from django.http import HttpResponse
#importamos modelos para usarlos
from .models import *

# Create your views here.
def index(request):
	consulta_Estudiante = Estudiante.objects.filter(grupo=5)
	grupo_id  =  Grupo.objects.get(id_grupo=5)
	grupo_idSeis  =  Grupo.objects.get(id_grupo=6)
	grupo_idSiete  =  Grupo.objects.get(id_grupo=7)

	return render(request, "index.html", {'consulta_Estudiante':consulta_Estudiante, 'grupo_id':grupo_id, 'grupo_idSeis':grupo_idSeis, 'grupo_idSiete':grupo_idSiete})

def  grupoCinco(request, grupo_id):
	consulta_Estudiante = Estudiante.objects.filter(grupo=5)
	return  render(request, "Grupo5.html", {'grupo_id':grupo_id, 'consulta_Estudiante':consulta_Estudiante})

def grupoSeis(request, grupo_id):
	consulta_Estudiante = Estudiante.objects.filter(grupo=6)
	return  render(request, "Grupo6.html", {'consulta_Estudiante':consulta_Estudiante})

def grupoSiete(request, grupo_id):
	consulta_Estudiante = Estudiante.objects.filter(grupo=7)
	return  render(request, "Grupo7.html", {'consulta_Estudiante':consulta_Estudiante})