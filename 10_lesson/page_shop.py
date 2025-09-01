from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:
    def __init__(self, driver):
        """
        Конструктор класса LoginPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_buttom = (By.ID, "login-button")

    @allure.step("Авторизация. Вводится имя и пароль пользователя.")
    def login(self, username, password):
        """
        Авторизируется на сайте магазина.

        :param username: str — имя пользователя
        :param password: str — пароль пользователя.
        """
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_buttom).click()


class ProductAdd:
    def __init__(self, driver):
        """
        Конструктор класса ProductAdd.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_button = (By.ID, "shopping_cart_container")

    @allure.step("Добавление товара в корзину")
    def add(self):
        """
        Добавляет товар в корзину.
        """
        self.driver.find_element(*self.backpack).click()
        self.driver.find_element(*self.tshirt).click()
        self.driver.find_element(*self.onesie).click()

    @allure.step("Переход в корзину")
    def go_cart(self):
        """
        Переходит в корзину.
        """
        self.driver.find_element(*self.cart_button).click()


class Checkout:
    def __init__(self, driver):
        """
        Конструктор класса Checkout.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.checkout = (By.ID, "checkout")

    @allure.step("Подверждение товаров и переход в форму доставки")
    def gocheck(self):
        """
        Подверждает товары и переходит в форму доставки.
        """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.checkout)).click()


class DeliveryForm:
    def __init__(self, driver):
        """
        Конструктор класса DeliveryForm.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.first = (By.ID, "first-name")
        self.last = (By.ID, "last-name")
        self.zip = (By.ID, "postal-code")
        self.conbutton = (By.ID, "continue")
        self.total = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнение формы доставки")
    def inputform(self, first_name, last_name, zip_code):
        """
        Вводит данные для заполнения формы доставки.

        :param first_name: str — Имя
        :param last_name: str — Фамилия
        :param zip_code: int — ZIP код
        """
        self.driver.find_element(*self.first).send_keys(first_name)
        self.driver.find_element(*self.last).send_keys(last_name)
        self.driver.find_element(*self.zip).send_keys(zip_code)

    @allure.step("Подтверждение формы доставки")
    def contin(self):
        """
        Подтверждает введенные данные для формы доставки.

        Переходит на траницу с финальной ценой.
        """
        self.driver.find_element(*self.conbutton).click()

    @allure.step("Получение финальной цены")
    def pricetotal(self) -> str:
        """
        Получает финальную цену.
        """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.total))
        price = self.driver.find_element(*self.total)
        return price.text
