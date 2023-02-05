import json
from django.test import TestCase
from rest_framework import status  # все коды ответов
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase

from authapp.models import User
# from mixer.backend.django import mixer
# from django.contrib.auth.models import User
from .views import AuthorModelViewSet, BookModelViewSet
from .models import Author, Book


class TestAuthorViewSet(TestCase):  # TestCase - встроеный в Django класс для тестирования
    def test_get_list(self):
        factory = APIRequestFactory()  # Нужен, чтобы создать запрос (фейковый запрос к самим себе -
        # по факту вызывается Вьюха, котороя идёт ниже по коду). Задача APIRequestFactory создать фабрику,
        # которая будет формировать объект request'а
        request = factory.get('/api/authors/')  # куда мы хотим сходить. request - формирует объект для сервера
        # со всеми полями
        view = AuthorModelViewSet.as_view({'get': 'list'})  # Формируем view, в котором get-запрос формируется на list
        # (потому, что там mixin)
        response = view(request)  # берём нашу view и передаём её объект request'а
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # проверка

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post(
            '/api/authors/',
            {
                'first_name': 'Владимир',
                'last_name': 'Маяковский',
                'birthday_year': 1893
            },
            # format='json'  # это было в методичке, не было на уроке
        )
        view = AuthorModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post(
            '/api/authors/',
            {
                'first_name': 'Владимир',
                'last_name': 'Маяковский',
                'birthday_year': 1893
            },
            # format='json'  # это было в методичке, не было на уроке
        )
        admin = User.objects.create_superuser(
            'admin',
            'admin@local.com',
            'admin123456'
        )
        force_authenticate(request, admin)  # метод умеет авторизовывать пользователя, он получит токен по факту
        view = AuthorModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        author = Author.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)
        client = APIClient()  # Имитирует клиента, не нужно создавать вьюху, отдельно генерировать factory, request
        response = client.get(f'/api/authors/{author.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        author = Author.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)
        client = APIClient()
        response = client.put(
            f'/api/authors/{author.id}/',
            {
                'first_name': 'Говард',
                'last_name': 'Лавкрафт',
                'birthday_year': 1880
            }
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        author = Author.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)
        client = APIClient()
        admin = User.objects.create_superuser(
            'admin',
            'admin@admin.com',
            'admin123456'
        )
        client.login(username='admin', password='admin123456')
        response = client.put(
            f'/api/authors/{author.id}/',
            {
                'first_name': 'Говард',
                'last_name': 'Лавкрафт',
                'birthday_year': 1880
            }
        )
        # author = Author.objects.get(id=author.id)  # это было в методичке
        author = Author.objects.get(pk=author.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(author.first_name, 'Говард')
        self.assertEqual(author.birthday_year, 1880)
        client.logout()


class TestMath(APISimpleTestCase):  # Тут не будет создаваться БД. Тут тестируются внутренние функции
    def test_sqrt(self):
        import math
        self.assertEqual(math.sqrt(4), 2)


class TestBookModelViewSet(APITestCase):  # внутри сделан клиент

    def test_get_list(self):
        responce = self.client.get('/api/books/')
        self.assertEqual(responce.status_code, status.HTTP_200_OK)

    # def test_edit_book_admin(self):  # Мой вариант - так всё работало
    #     author = Author.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)
    #     print('\n1 ', 100 * '*')
    #     print(author.id)
    #     print(author.first_name)
    #     print(author.last_name)
    #     book = Book.objects.create(name='Руслан и Людмила')
    #     book.author.add(author)
    #     book.save()
    #     print(book.name)
    #     print('2 ', 100 * '*')
    #     print(book.id)
    #     print('3 ', 100 * '*')
    #     print(book.author)
    #     print('4 ', 100 * '*')
    #     admin = User.objects.create_superuser(
    #         'admin',
    #         'admin@admin.com',
    #         'admin123456'
    #     )
    #     self.client.login(username='admin', password='admin123456')
    #     response = self.client.patch(
    #         f'/api/books/{book.id}/',
    #         {
    #             'name': 'Лукоморье',
    #             # 'author': book.author
    #         }
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     book = Book.objects.get(pk=book.id)
    #     self.assertEqual(book.name, 'Лукоморье')
    #     self.client.logout()

    def test_edit_book_admin(self):  # Вариант преподавателя
        author = Author.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)
        book = Book.objects.create(name='Руслан и Людмила')
        book.author.add(author)
        book.save()

        admin = User.objects.create_superuser(
            'admin',
            'admin@admin.com',
            'admin123456'
        )
        self.client.login(username='admin', password='admin123456')
        response = self.client.put(
            f'/api/books/{book.id}/',
            {
                'name': 'Лукоморье',
                'author': author.id
            }
        )
        book = Book.objects.get(pk=book.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(book.name, 'Лукоморье')
        self.client.logout()
