import allure
import requests

from data.handlers import Urls, Handlers
from data.user_data import User


@allure.suite('Авторизация пользователя')
class Testlogin:

    @allure.description('вход под существующим пользователем')
    @allure.title('Авторизация под пользователем, который есть в системе')
    def test_login_user(self):
       with allure.step('вход под существующим пользователем'): 
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.LOGIN}', data=User.data_correct)
        assert response.status_code == 200 and response.json().get('success') == True

    @allure.description('вход с некорректным логином/паролем')
    @allure.title('Авторизация с некорректным логином/паролем')
    def test_login_user_error(self):
       with allure.step('вход с некорректным логином/паролем'): 
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.LOGIN}', data=User.data_negative)
        assert response.status_code == 401 and response.json().get('success') == False
