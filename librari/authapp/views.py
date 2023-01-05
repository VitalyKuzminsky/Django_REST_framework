from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()  # Мы работаем с моделью Author, со всеми её записями.
    serializer_class = UserModelSerializer  # Указываем сереализатор.
