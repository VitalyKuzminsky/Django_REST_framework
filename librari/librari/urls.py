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
from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter, SimpleRouter

from app.views import AuthorModelViewSet, BiographyModelViewSet, BookModelViewSet, ArticleModelViewSet, MyAPIView
from app.views import AuthorModelViewSet, BiographyModelViewSet, BookModelViewSet, ArticleModelViewSet
from authapp.views import UserModelViewSet, MyListAPIViewForLesson4, MyRetrieveAPIViewForLesson4, \
    MyUpdateAPIViewForLesson4, MyListAPIViewForHomeworkLesson9
from todoapp.views import ProjectModelViewSet, TODOModelViewSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='Library',
        default_version='0.1',
        description='Doc for project',
        contact=openapi.Contact(email='blabla@bla.bla'),
        license=openapi.License(name='MIT License')
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)


router = DefaultRouter()  # router - это сущность, которая генерит urls. DefaultRouter создаёт точку входа
# router = SimpleRouter()  # router - без точек входа
router.register('authors', AuthorModelViewSet)  # authors - это end-point
router.register('biographies', BiographyModelViewSet)
router.register('books', BookModelViewSet)
router.register('articles', ArticleModelViewSet)
router.register('users', UserModelViewSet)  # users - это end-point
router.register('project', ProjectModelViewSet)
router.register('todo', TODOModelViewSet)
# router.register('my', MyAPIView, basename='myapiview')  # демонстрация, как ViewSet интегрирован. basename -
# внутренняя переменная для DRF, он нигде не отображается

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # это было в методичке, на уроке не было
    path('api-token-auth/', obtain_auth_token),  # для токенов
    path('api/', include(router.urls)),
    # для настройки документации yasg:
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # re_path(r'^myapi/(?P<version>\d)/authors/$', MyAPIView.as_view({'get': 'list'})),  # Отображение версий вар.1
    # path('api/1/authors/', include('app.urls', namespace='1')),  # Отображение версий вар.2 - главное, это
    # # namespace='1', которая и передаётся в url
    # path('api/2/authors/', include('app.urls', namespace='2')),  # Отображение версий вар.2
    path('api/new_authors/', MyAPIView.as_view()),  # Отображение версий вар.3 Теперь версия меняется в адресной строке
    # при добавлении параметра: http://127.0.0.1:8000/api/authors/?version=2
    path('api/new_users/', MyListAPIViewForHomeworkLesson9.as_view()),  # ДЗ к уроку 9
    # path('myapi/', MyAPIView.as_view()),  # Для примеров с 1 по 2 4го урока
    # path('myapi/', MyAPIView.as_view({'get': 'list'})),  # Для примера 3 4го урока
    # path('api/my_list_api_hw_lesson4/', MyListAPIViewForLesson4.as_view()),
    # path('api/my_retrieve_api_hw_lesson4/<pk>/', MyRetrieveAPIViewForLesson4.as_view()),
    # path('api/my_update_api_hw_lesson4/<pk>/', MyUpdateAPIViewForLesson4.as_view()),  # ДЗ к 4 уроку
]
