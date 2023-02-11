from graphene.types.objecttype import ObjectType
from graphene.types.schema import Schema
from graphene.types.structures import List
from graphene.types.scalars import String, Int, ID
from graphene.types.field import Field
from graphene.types.mutation import Mutation
from graphene_django.types import DjangoObjectType
from app.models import Book, Author
from todoapp.models import Project, TODO
from authapp.models import User


class BookType(DjangoObjectType):  # создали тип данных для описания, который создаёт схемы на основе полей в БД
    class Meta:
        model = Book
        fields = '__all__'


class AuthorType(DjangoObjectType):  # создали тип данных для описания, который создаёт схемы на основе полей в БД
    class Meta:
        model = Author
        fields = '__all__'


class ProjectType(DjangoObjectType):  # создали тип данных для описания Project
    class Meta:
        model = Project
        fields = '__all__'


class TODOType(DjangoObjectType):  # создали тип данных для описания TODO
    class Meta:
        model = TODO
        fields = '__all__'


class UserType(DjangoObjectType):  # создали тип данных для описания User
    class Meta:
        model = User
        fields = '__all__'


class Query(ObjectType):  # создаём тип Query, который будет возвращать все книжки запросом all_books
    all_books = List(BookType)  # обработчик на книги
    all_authors = List(AuthorType)  # обработчик на авторов
    # author_by_id = Field(AuthorType, id=Int(required=True))  # в этой схеме новое поле Field, это AuthorType. Так
    # было у преподавателя, т.к. у него id был цифрой
    author_by_id = Field(AuthorType, id=String(required=True))  # в этой схеме новое поле Field, это AuthorType,
    # передаём сюда обязательный id. Так сделал я, потому что у меня сложный id.
    book_by_author_name = List(BookType, name=String(required=False))
    all_project = List(ProjectType)  # обработчик на все проекты
    user_by_id = Field(UserType, id=String(required=True))  # проекты по id юзера
    project_by_id = Field(ProjectType, id=Int(required=True))  # проекты по id юзера

    def resolve_all_project(self, info):
        return Project.objects.all()

    # Запрос по проектам:
    # {
    #   allProject {
    #     name
    #     todoSet {
    #       text
    #       project {
    #         id
    #       }
    #       user {
    #         firstName
    #         lastName
    #       }
    #     }
    #   }
    # }

    def resolve_user_by_id(self, info, id):
        try:
            return User.objects.get(pk=id)  # По этому id пытаемся получить данные из БД
        except User.DoesNotExist:
            return None

    # Запрос проектов по id юзера
    # {
    #   projectById(id: "9b14f3f0-c8de-4eb9-9434-65bde5e6c809") {
    #     username
    #     firstName
    #     lastName
    #     todoSet {
    #       id
    #       active
    #       text
    #     }
    #   }
    # }

    def resolve_project_by_id(self, info, id):
        try:
            return Project.objects.get(pk=id)  # По этому id пытаемся получить данные из БД
        except Project.DoesNotExist:
            return None

    # Схема, которая позволяет по id проекта получить имя проекта и связанные с проектом ТуДу, пользователй
    # {
    #   projectById(id: 1) {
    #     name
    #     todoSet{
    #       text
    #       active
    #     }
    #     users {
    #       firstName
    #       lastName
    #     }
    #   }
    # }

    def resolve_all_books(self, info):
        return Book.objects.all()  # запрос в БД

    def resolve_all_authors(self, info):
        return Author.objects.all()  # запрос в БД

    # Пример запроса для двух предыдущих функции:
    # {
    #   allBooks {
    #     # id
    #     name
    #     # author {
    #     #   id
    #     #   firstName
    #     #   lastName
    #     # }
    #   }
    #   allAuthors {
    #     # id
    #     firstName
    #     lastName
    #     birthdayYear
    #  }
    # }

    # {
    #   aaa: allAuthors {
    #     firstName
    #   }
    #   BBB: allAuthors {
    #     lastName
    #   }
    # }

    # {
    #   allBooks {
    #     name
    #     author {
    #       firstName
    #     }
    #   }
    # }

    def resolve_author_by_id(self, info, id):
        try:
            return Author.objects.get(pk=id)  # По этому id пытаемся получить данные из БД
        except Author.DoesNotExist:
            return None

    # Пример запроса:
    # {
    #   authorById(id: "ca2b6fc8-542c-4404-be7f-33dd5a35ba9c"){
    #     firstName
    #     lastName
    #     birthdayYear
    #     bookSet {
    #       name
    #     }
    #   }
    # }

    def resolve_book_by_author_name(self, info, name=None):  # name по умолчанию не обязательно
        # print(dir(info))  # рабочая инфа
        books = Book.objects.all()  # получаем все книги
        if name:  # если получено name
            books = books.filter(author__first_name=name)  # то books присваиваем фильтр по имени
        return books

    # Пример запроса:
    # {
    #     bookByAuthorName(name: "Лев") {
    #     name
    # }
    # }


class AuthorMutation(Mutation):  # создаём класс для изменений
    class Arguments:  # указываем параметры для изменения
        id = ID()
        first_name = String()
        last_name = String()
        birthday_year = Int()

    author = Field(AuthorType)  # св-во author будет содержать в себе объект после изменения

    @classmethod
    def mutate(cls, root, info, id, first_name, last_name, birthday_year):  # описываем логику изменений
        author = Author.objects.get(pk=id)  # Через id получаем для изменения конкретнго автора
        author.first_name = first_name
        author.last_name = last_name
        author.birthday_year = birthday_year
        author.save()
        return AuthorMutation(author=author)  # возвращаем объект мутации с изменённым автором


class Mutation(ObjectType):  # создаём класс Mutation, который отвечает за все изменения - он содержит в себе классы
    # определяющие изменение
    update_author = AuthorMutation.Field()

    # Пример
    # mutation updateAuthor {
    #   updateAuthor(id: "653f409f-bf05-45e3-8985-bc0f6847924a", firstName: "Эксперементальный",
    #   lastName: "НоваяФамилия", birthdayYear: 2000) {
    #     author {
    #       firstName
    #       lastName
    #       birthdayYear
    #     }
    #   }
    # }


# schema = Schema(query=Query)  # Схема для первых запросов до мутации
schema = Schema(query=Query, mutation=Mutation)  # Схема изменений
