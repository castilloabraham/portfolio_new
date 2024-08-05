#este archivo hara la conversion de mis campos en queryset

from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        #campos que desea convertir
        #fields = ('nombre del campo')
        fields = '__all__'