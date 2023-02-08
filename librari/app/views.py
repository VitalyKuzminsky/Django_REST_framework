from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import Author, Biography, Book, Article
from .serializers import AuthorModelSerializer, BiographyModelSerializer, BookModelSerializer, ArticleModelSerializer, \
    BookSerializerBase, AuthorModelSerializer2
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination


# # Создам пагинатор для авторов
# class AuthorPaginator(LimitOffsetPagination):
#     default_limit = 10


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()  # Мы работаем с моделью Author, со всеми её записями.
    # permission_classes = [IsAuthenticated]
    serializer_class = AuthorModelSerializer  # Указываем сереализатор.

    # Переопределяем get_queryset для получения данных - Hardcore
    # def get_queryset(self):
    #     return Author.objects.filter(first_name__contains='Александр')  # __contains - разбирает этот аргумент и
    #     # понимает, что мы хотим, чтобы first_name содержал 'Александр'

    # Переопределяем get_queryset - передаём запрос через параметры
    # def get_queryset(self):
    #     param = self.request.query_params.get('name')
    #     print(self.request.query_params)
    #     if param:
    #         return Author.objects.filter(first_name__contains=param[0])  # <QueryDict: {}> - приходит пустой,
    #         # поэтому, когда вводим параметры http://127.0.0.1:8000/api/authors/?name=Will, то берётся первый [0]
    #         # индекс: <QueryDict: {'name': ['Will']}>
    #         # Можно указывать через & несколько параметров ?name=Will&?name=Babayka
    #         # => <QueryDict: {'name': ['Will'], '?name': ['Babayka']}>
    #         # ?name=Will&name=Babayka
    #         # => <QueryDict: {'name': ['Will', 'Babayka']}>
    #     return super().get_queryset()  # super'ом вызываем родительский get_queryset

    # Переопределяем get_queryset - передаём запрос через Headers
    # def get_queryset(self):
    #     param = self.request.headers.get('filter')
    #     print(self.headers)
    #     if param:
    #         return Author.objects.filter(first_name__contains=param)
    #     return super().get_queryset()

    # # Фильтрация ч/з django_filters
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name', 'birthday_year']
    # pagination_class = AuthorPaginator


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


class BookModelViewSet(ModelViewSet):
    permission_classes = [AllowAny]   # На книги с AllowAny могут заходить все, кто угодно. Задаём разрешения
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    # def get_serializer_class(self):
    #     if self.request.method in ['GET']:
    #         return BookModelSerializer
    #     return BookSerializerBase


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


# Создаём класс для 4-го урока
# 1. На базе APIView
# class MyAPIView(APIView):
#
#     # переопределяем get запрос
#     def get(self, request):
#         print(request.headers)
#         print(request.data)
#         print(request.query_params)
#         return Response({'data': 'GET SUCCESS'})
#
#     # переопределяем post запрос
#     def post(self, request):
#         return Response({'data': 'POST SUCCESS'})


# 2. На базе Generic APIView
# class MyCreateAPIView(CreateAPIView):  # Создание
#
#     # настройки похожи на ModelViewSet, но будет работать только 1 вид запросов
#     renderer_classes = [JSONRenderer]
#     queryset = Author.objects.all()  # Мы работаем с моделью Author, со всеми её записями.
#     serializer_class = AuthorModelSerializer  # Указываем сереализатор.
#
# class MyListAPIView(ListAPIView):  # Получение всех данных
#
#     renderer_classes = [JSONRenderer]
#     queryset = Author.objects.all()
#     serializer_class = AuthorModelSerializer
# class MyAPIView(CreateAPIView, ListAPIView):  # Создание и Получение всех данных в одном флаконе
#
#     # настройки похожи на ModelViewSet, но будет работать только 1 вид запросов
#     # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]  # как рендерим - по умолчанию так и работает
#     queryset = Author.objects.all()
#     serializer_class = AuthorModelSerializer


# # 3. На базе ViewSet - можно использовать модуль, можно руками. ViewSet интегрирован в экосистему Django (роутинг,
# # пагинация и т.п.).
# class MyAPIView(ViewSet):  # ViewSet является базовым классом всего рассмотреного ранее. Можно определять методы.
#
#     # Например переопределим метод list проссмотра всего
#     def list(self, request):
#         authors = Author.objects.all()
#         serializer = AuthorModelSerializer(authors, many=True)
#
#         return Response(serializer.data)
#
#     # Если нужно написать особенные условия, то использовать декоратор
#     @action(detail=False, methods=['get'])  # detail - говорит, будем работать со многими объектами или одним
#     def my_special_url(self, request):  # my_special_url - будет url'ом:
#         # http://127.0.0.1:8000/api/my/espacial_condition/
#         return Response({'data': 'Ra-ta-ta, Ra Ta-ta-ta'})


# Фильтры.
# Везде, где есть get_queryset - он возвращает queryset
# Если его переопределить, то можно получить выборку нужных данных


# Урок 9 Версионирование
# Отображение версий вар.1
# class MyAPIView(ViewSet):
#
#     def list(self, request, version):
#         print(f'запрашиваемая версия: {version}')
#         print(f'ещё одно отображение версии через request: {request.version}')
#         authors = Author.objects.all()
#         serializer = AuthorModelSerializer(authors, many=True)
#
#         return Response(serializer.data)
#
#     @action(detail=False, methods=['get'])
#     def my_special_url(self, request):
#         return Response({'data': 'Ra-ta-ta, Ra Ta-ta-ta'})


# Отображение версий вар.2
# class MyAPIView(ListAPIView):
#     queryset = Author.objects.all()
#     serializer = AuthorModelSerializer
#
#     def get_serializer_class(self):
#         if self.request.version == '1':
#             return AuthorModelSerializer
#         return AuthorModelSerializer2


# Отображение версий вар.3
class MyAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer = AuthorModelSerializer

    def get_serializer_class(self):
        if self.request.version == '1':
            return AuthorModelSerializer
        return AuthorModelSerializer2
