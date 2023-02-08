from django.urls import path
from .views import MyAPIView

# Отображение версий вар.2
app_name='authors'
urlpatterns = [
    path('', MyAPIView.as_view())  # get запрос проксируем на list.
]
