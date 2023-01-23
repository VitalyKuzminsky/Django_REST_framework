from rest_framework.serializers import ModelSerializer
from .models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        # fields = ['id', 'email', 'username', 'first_name', 'last_name']
        fields = ['id', 'first_name', 'last_name', 'username']
