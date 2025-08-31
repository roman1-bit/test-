import pytest
from selenium import webdriver
from page_shop import LoginPage
from page_shop import ProductAdd
from page_shop import Checkout
from page_shop import DeliveryForm
import allure


@pytest.fixture()
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.

    Открытия сайта магазина.
    """
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@allure.title("Тестирование магазина")
@allure.description("Тест проверяет корректную работу магазина. Авторизация."
                    "Добавление товаров в корзину. Переход в корзину."
                    "Заполенение формы доставки. Подтверждение формы доставки."
                    "Получение финальной цены.")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.BLOCKER)
def test_shop(driver):
    """
    Тест проверяет работу магазина.
    """
    with allure.step("Авторизация"):
        LoginPage(driver).login("standard_user", "secret_sauce")
    with allure.step("Добавление товара"):
        ProductAdd(driver).add()
    with allure.step("Переход в корзину"):
        ProductAdd(driver).go_cart()
    with allure.step("Подтверждение товара"):
        Checkout(driver).gocheck()
    with allure.step("Заполнение формы доставки"):
        DeliveryForm(driver).inputform("Ivan", "Ivanov", "123456")
    with allure.step("Подтверждение формы доставки"):
        DeliveryForm(driver).contin()
    with allure.step("Получение финальной цены"):
        DeliveryForm(driver).pricetotal()

    with allure.step("Проверка полученной цены"):
        assert DeliveryForm(driver).pricetotal() == "Total: $58.29"
