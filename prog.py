from graphene import ObjectType, String, Schema


class Query(ObjectType):  # Создаём класс и объявлем поля
    hello = String(name=String(default_value='stranger'))
    goodbye = String()

    def resolve_hello(self, info, name):  # поиск осуществляется по resolve и имени поля
        return f'Hello {name}'

    def resolve_goodbye(self, info):
        return 'See ya!'


# Создаём схему
schema = Schema(query=Query)