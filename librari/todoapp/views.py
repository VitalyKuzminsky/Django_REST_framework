from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Project, TODO
from .serializers import ProjectModelSerializer, TODOModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
