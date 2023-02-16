"""
from rest_framework import serializers


class Author:  # Создаём модель автор

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __str__(self):  # Переопределяем отображение автора
        return f'{self.name} {self.year}'


class AuthorSerializer(serializers.Serializer):  # Создаём сериализатор - он создаёт из объекта Python словарь
    name = serializers.CharField(max_length=128)
    year = serializers.IntegerField()

    # Делаем кастомную валидацию
    def validate_year(self, value):  # Формирование названия: validate_ После название, что проверяем: year
        if value < 0:  # Делаем проверку, чтобы год не был отрицательным
            raise serializers.ValidationError('Год не должен быть отрицательным!')
        return value
"""

    # def validate(self, attrs):
    #     """
    #     Позволяет валидировать все вместе данные.
    #     :param attrs: это будет словарик со всеми атрибутам
    #     :return:
    #     """
    #     if attrs['name'] == 'Alex' and attrs['year'] != 1799:  # Проверяем условия, если ..., то:
    #         raise serializers.ValidationError('Год рождения Пушкина Не верны!!')
    #     return attrs  # возвращаем attrs, иначе ничего не вернётся

"""
    # Настроим сериалайзер
    def create(self, validated_data):  # Переопределим метод создания
        return Author(**validated_data)

    def update(self, instance, validated_data):  # Переопределим метод обновления
        instance.name = validated_data.get('name', instance.name)
        instance.year = validated_data.get('year', instance.year)
        return instance


author1 = Author('Грин', 1880)  # Создаём объект автор
serializer1 = AuthorSerializer(author1)  # Создаём объект сериализатор


# Создаём рендер, чтобы получить инфу из сериализатора к юзеру (Рендер приобразует питоновский словарь в данные - байты)
from rest_framework.renderers import JSONRenderer

render1 = JSONRenderer()  # Создаём объект рендера
# Создаём json в байтах
json_bytes = render1.render(serializer1.data)

# Для преобразования из байтов обратно в словарь - нужен Парсер. Сериализатор из словаря делает объект Python
from rest_framework.parsers import JSONParser
import io

stream = io.BytesIO(json_bytes)  # Создаём поток из байтов
data = JSONParser().parse(stream)  # Создаём словарь из потока байтов


print(author1)
print(50*'-')
# print(dir(author1))
# print(50*'-')
# print(author1.__dict__)
# print(50*'-')
# print(serializer)
# print(50*'-')
print(serializer1.data)
print(50*'-')
print(json_bytes)
print(50*'-')
print(data)
print(50*'+')


# Создание новго автора
new_data = {
    'name': 'Alex',
    'year': 1799
}
serializer2 = AuthorSerializer(data=new_data)
serializer2.is_valid()
# так сделал сам:
# serializer2.save()
# print(serializer2.data)
# так сделал преподаватель:
author2 = serializer2.save()
print(author2)
# print(author2.name, author2.year)  # Так сделал преподаватель, у него метод str не был переопределён

# Обновление автора полностью, в т.ч. с проверкой даты, если поставить отрицательное
print(50*'+')
new_name = {
    'name': 'Babayka',
    'year': 888
}
serializer2 = AuthorSerializer(author2, data=new_name)
serializer2.is_valid()
author2 = serializer2.save()
print(author2)

# Обновление автора частично
print(50*'+')
new_name = {
    'year': 1888
}
serializer2 = AuthorSerializer(author2, data=new_name, partial=True)
serializer2.is_valid()
author2 = serializer2.save()
print(author2)
"""

# урок 9
from abc import ABC, abstractmethod


class RateService(ABC):
    @abstractmethod
    def det_rate(self):
        pass


class CentralBank(RateService):
    def get_rate(self):
        return 67


class Proxy(RateService):
    def __init__(self):
        self.bank = CentralBank()
        self.rates = {}

    def gat_rate(self, currency):
        if currency in self.rates.keys():
            print(f'{currency} получена из кеша')
            return self.rates[currency]
        else:
            print(f'{currency} получена путём запроса из ЦБ')
            rate = self.bank.get_rate()
            self.rates[currency] = rate
            return rate


bank = Proxy()
bank.gat_rate('dollar')
bank.gat_rate('dollar')
bank.gat_rate('dollar')
bank.gat_rate('dollar')
bank.gat_rate('dollar')




















