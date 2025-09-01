import pytest
from selenium import webdriver
from page_calc import PageCalc
import allure


@pytest.fixture()
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.

    Открытия сайта калькулятора.
    """
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
    yield driver
    driver.quit()


@allure.title("Тестирование калькулятора: 7 + 8 = 15")
@allure.description("Тест проверяет корректную работу калькулятора")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc(driver):
    """
    Тест проверяет работу калькулятора с различными операциями.
    """
    with allure.step("Открытие страницы калькулятора"):
        page = PageCalc(driver)
    with allure.step("Установка задержки в секундах"):
        page.calcwait("45")
    with allure.step("Ввод значений для кнопки button"):
        page.calcinput("7")
        page.calcinput("+")
        page.calcinput("8")
        page.calcinput("=")
    with allure.step("Получение результата после задржки в 45 секунд"):
        result = page.getresult()
    with allure.step("Проверка результата"):
        assert result == "15"
