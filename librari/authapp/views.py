from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()  # Мы работаем с моделью Author, со всеми её записями.
    serializer_class = UserModelSerializer  # Указываем сереализатор.


# API для ДЗ к 4у уроку
""" 
Модель User: есть возможность просмотра списка и каждого пользователя в
отдельности, можно вносить изменения, нельзя удалять и создавать
"""


class MyListAPIViewForLesson4(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class MyRetrieveAPIViewForLesson4(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class MyUpdateAPIViewForLesson4(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
