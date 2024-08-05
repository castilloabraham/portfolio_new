#from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ProjectSerializer #Ya nos dice que campos vamos a compartir y recibir
from .models import Project

# Create your views here.


# con esta clase generamos el crud de forma automatica
class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all() #Se esta trayendo todos los proyectos
    
