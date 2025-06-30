import pytest
import requests
from project.config.endpoints import LOGIN_ENDPOINT
from project.dto.user_authorization import LoginRequest, LoginResponse, ErrorResponse
from project.test.testdata import valid_users, invalid_users, API_KEY_HEADER

"""
Тест проверяет успешную авторизацию пользователя.

Шаги:
- Формируется JSON с корректным email и паролем.
- Отправляется POST-запрос на эндпоинт авторизации.
- Проверяется статус-код 200 и наличие токена в ответе.

Ожидаемый результат:
- Статус ответа 200.
- В теле ответа присутствует токен авторизации.

Автор: Колтыгин Сергей
"""
@pytest.mark.parametrize("email,password", valid_users)
def test_successful_login(email, password):
    login_request = LoginRequest(email=email, password=password)
    response = requests.post(LOGIN_ENDPOINT, json=login_request.dict(), headers=API_KEY_HEADER)
    assert response.status_code == 200
    login_response = LoginResponse(**response.json())
    assert login_response.token is not None, "Токен не должен быть пустым"


    """
    Тест проверяет отказ в авторизации при неверных данных.

    Шаги:
    - Формируется JSON с некорректными/отсутствующими данными.
    - Отправляется POST-запрос на эндпоинт авторизации.
    - Проверяется статус-код 400 и наличие поля error в ответе.

    Ожидаемый результат:
    - Статус ответа 400.
    - В теле ответа присутствует сообщение об ошибке.

    Автор: Колтыгин Сергей
    """
@pytest.mark.parametrize("email,password", invalid_users)
def test_failed_login(email, password):
    data = {
        "email": email,
        "password": password
    }
    response = requests.post(LOGIN_ENDPOINT, json=data, headers=API_KEY_HEADER)
    assert response.status_code == 400
    error_response = ErrorResponse(**response.json())
    assert error_response.error is not None
