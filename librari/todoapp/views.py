from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Project, TODO
from .serializers import ProjectModelSerializer, TODOModelSerializer
from rest_framework.pagination import LimitOffsetPagination


# # Создаём пагинатор для Проектов
# class ProjectPaginator(LimitOffsetPagination):
#     default_limit = 10
#
#
# # Создаём пагинатор для заметок
# class TODOPaginator(LimitOffsetPagination):
#     default_limit = 20


class ProjectModelViewSet(ModelViewSet):
    # """
    # Модель Project: доступны все варианты запросов; для постраничного вывода
    # установить размер страницы 10 записей; добавить фильтрацию по совпадению части
    # названия проекта;
    # """
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    # pagination_class = ProjectPaginator


class TODOModelViewSet(ModelViewSet):
    # """
    # Модель ToDo: доступны все варианты запросов; при удалении не удалять ToDo, а
    # выставлять признак, что оно закрыто; добавить фильтрацию по проекту; для
    # постраничного вывода установить размер страницы 20.
    # """
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['project']
    # pagination_class = TODOPaginator
    #
    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = TODOModelSerializer(
    #         instance, data={'active': False},
    #         context={'request': request},
    #         partial=True
    #     )
    #     serializer.is_valid()
    #     serializer.save()
    #
    #     return Response(serializer.data)

