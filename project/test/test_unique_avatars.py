import requests
from project.config.endpoints import USERS_ENDPOINT
from project.dto.resource_dto import ResourceDto

"""
Тест проверяет, что аватары пользователей на странице 2 являются уникальными.

Шаги:
- Выполняется GET-запрос на получение пользователей второй страницы.
- Проверяется, что статус ответа равен 200.
- Извлекаются ID аватаров из ссылок и проверяется их уникальность.

Ожидаемый результат:
- Все аватары должны быть уникальны, иначе тест упадёт.

Автор: Колтыгин Сергей 
"""
def test_avatars_Should_Be_Uniquee():
    response = requests.get(f"{USERS_ENDPOINT}?page=2")
    assert response.status_code == 200, f"Ожидался статус 200, но получен {response.status_code}"
    resource = ResourceDto(**response.json())
    avatars = [user.avatar.split("/")[-1] for user in resource.data if user.avatar]
    unique_avatars = set(avatars)
    assert len(avatars) == len(unique_avatars), f"Найдены дубликаты аватаров: {avatars}"