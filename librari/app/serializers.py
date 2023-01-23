from rest_framework.serializers import ModelSerializer, StringRelatedField, HyperlinkedModelSerializer
from .models import Author, Biography, Book, Article


# class AuthorModelSerializer(HyperlinkedModelSerializer):  # Не подходит для 3 примера на базе APIViewSet 4 урок.
# Потому что HyperlinkedModelSerializer пытается сгенерить ссылку на просмотр одного автора, а такого функционала
# в примере нет.
class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'  # передавать всё
        # fields = ['first_name']  # передавать только указанные поля
        # exclude = ['id']  # передавать всё, кроме этого


# class BiographyModelSerializer(HyperlinkedModelSerializer):
class BiographyModelSerializer(ModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'


# class BookModelSerializer(HyperlinkedModelSerializer):
class BookModelSerializer(ModelSerializer):
    author = StringRelatedField(many=True)  # Указываем в книгах сериализатор для авторов, чтобы вместо id видеть имена
    # author = AuthorModelSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'


# class ArticleModelSerializer(HyperlinkedModelSerializer):
class ArticleModelSerializer(ModelSerializer):
#     author = AuthorModelSerializer()  # Указываем в книгах сериализатор для автора, чтобы вместо id видеть имя

    class Meta:
        model = Article
        fields = '__all__'
