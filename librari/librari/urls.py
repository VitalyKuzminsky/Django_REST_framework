"""librari URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from app.views import AuthorModelViewSet, BiographyModelViewSet, BookModelViewSet, ArticleModelViewSet, MyAPIView
from authapp.views import UserModelViewSet, MyListAPIViewForLesson4, MyRetrieveAPIViewForLesson4, \
    MyUpdateAPIViewForLesson4
from todoapp.views import ProjectModelViewSet, TODOModelViewSet


router = DefaultRouter()  # router - это сущность, которая генерит urls. DefaultRouter создаёт точку входа
# router = SimpleRouter()  # router - без точек входа
router.register('authors', AuthorModelViewSet)  # authors - это end-point
router.register('biographies', BiographyModelViewSet)
router.register('books', BookModelViewSet)
router.register('articles', ArticleModelViewSet)
router.register('users', UserModelViewSet)  # users - это end-point
router.register('project', ProjectModelViewSet)
router.register('todo', TODOModelViewSet)
router.register('my', MyAPIView, basename='myapiview')  # демонстрация, как ViewSet интегрирован. basename -
# внутренняя переменная для DRF, он нигде не отображается


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # это было в методичке, на уроке не было
    path('api/', include(router.urls)),
    # path('myapi/', MyAPIView.as_view()),  # Для примеров с 1 по 2 4го урока
    # path('myapi/', MyAPIView.as_view({'get': 'list'})),  # Для примера 3 4го урока
    path('api/my_list_api_hw_lesson4/', MyListAPIViewForLesson4.as_view()),
    path('api/my_retrieve_api_hw_lesson4/<pk>/', MyRetrieveAPIViewForLesson4.as_view()),
    path('api/my_update_api_hw_lesson4/<pk>/', MyUpdateAPIViewForLesson4.as_view()),  # ДЗ к 4 уроку
]
