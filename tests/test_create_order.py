import allure
import requests


from conftest import create_user
from data.handlers import Urls, Handlers
from data.ingredients_data import Ingredient


@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.description("Создание заказа с авторизацией и ингридиентами")
    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_with_auth(self, create_user):
      with allure.step("токен авторизации"):  
        token = {'Authorization': create_user[3]}
      with allure.step("создание заказа с авторизацией с ингидиентами"):  
        r = requests.post(f"{Urls.MAIN_URL}{Handlers.MAKE_ORDER}", headers=token, data=Ingredient.correct_ingredients_data)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.description("Создание заказа без авторизации")
    @allure.title("Создание заказа не авторизованным пользователем")
    def test_create_order_not_auth(self):
       with allure.step("создание заказа без авторизации с ингридиентами"): 
        r = requests.post(f"{Urls.MAIN_URL}{Handlers.MAKE_ORDER}", data=Ingredient.correct_ingredients_data)
        assert r.status_code == 200 and r.json().get("success") is True


    @allure.description("Создание заказа без ингредиентов и с авторизаци")
    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_with_out_ingridient(self, create_user):
       with allure.step("токен авторизации"):  
        token = {'Authorization': create_user[3]}
       with allure.step("создание заказа без ингридиентов и с авторизации"): 
        r = requests.post(f"{Urls.MAIN_URL}{Handlers.MAKE_ORDER}", headers=token, )
        assert r.status_code == 400 and r.json()['message'] == "Ingredient ids must be provided"




    @allure.description("Создание заказа без ингредиентов ")
    @allure.title("Создание заказа без ингредиентами")
    def test_create_order_with_ingredients(self):
     with allure.step('Создание заказа без ингредиентов и регистрации'): 
      response = requests.post(Urls.MAIN_URL + Handlers.MAKE_ORDER)
      assert response.status_code == 400 and response.json()['message'] == "Ingredient ids must be provided"
     



    @allure.description("Создание с невалидным хешем ингредиента")
    @allure.title("Создание с невалидным хешем ингредиента")
    def test_create_order_invalid_hash_ingridient(self):
       with allure.step("Создание с невалидным хешем ингредиента"): 
        response = requests.post(Urls.MAIN_URL + Handlers.MAKE_ORDER, headers=Handlers.headers,
                                 json=Ingredient.incorrect_ingredients_data)
        assert response.status_code == 500 and 'Internal Server Error' in response.text
