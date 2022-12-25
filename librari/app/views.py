from rest_framework.viewsets import ModelViewSet
from .models import Author
from .serializers import AuthorModelSerializer


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()  # Мы работаем с моделью Author, со всеми её записями.
    serializer_class = AuthorModelSerializer  # Указываем сереализатор.
