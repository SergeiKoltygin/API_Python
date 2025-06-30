# testdata.py

#: Список валидных пользователей (email, password), используется для позитивных тестов авторизации.
#: Автор: Колтыгин Сергей
valid_users = [("eve.holt@reqres.in", "cityslicka")]

#: Список невалидных пользователей (email, password=None), используется для негативных тестов авторизации.
#: Автор: Колтыгин Сергей
invalid_users = [("peter@klaven", None)]

#: Заголовок с API-ключом, необходимый для всех запросов к API.
#: Автор: Колтыгин Сергей
API_KEY_HEADER = {"x-api-key": "reqres-free-v1"}
