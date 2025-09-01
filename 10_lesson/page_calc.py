from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class PageCalc:
    def __init__(self, driver):
        """
        Конструктор класса CalcMainPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = (By.CSS_SELECTOR, "#delay")
        self.num7 = (
            By.XPATH, "//span[@class='btn btn-outline-primary' and text()='7']"
            )
        self.num8 = (
            By.XPATH, "//span[@class='btn btn-outline-primary' and text()='8']"
            )
        self.numsum = (
            By.XPATH, "//span[@class='operator btn btn-outline-success' and "
            "text()='+']")
        self.numres = (
            By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']"
            )
        self.result = (By.CLASS_NAME, "screen")

    @allure.step("Установка задержки {query} секунд")
    def calcwait(self, query):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param query: int — время задержки в секундах.
        """
        calcwaitelement = self.driver.find_element(*self.wait)
        calcwaitelement.clear()
        calcwaitelement.send_keys(query)

    @allure.step("Нажатие кнопки button")
    def calcinput(self, button_text):
        """
        Нажимает на кнопку калькулятора.

        :param button_text: str — текст на кнопке, которую нужно нажать.
        """
        # Маппинг кнопок к их селекторам
        button_mapping = {
            "7": self.num7,
            "8": self.num8,
            "+": self.numsum,
            "=": self.numres
        }

        # Если есть предопределенный селектор, используем его
        if button_text in button_mapping:
            selector = button_mapping[button_text]
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(selector))
        else:
            # Для других кнопок используем универсальный селектор
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//span[text()='{button_text}']")))

        button.click()
        # Небольшая пауза между нажатиями для стабильности
        import time
        time.sleep(0.5)

    @allure.step("Получение результата после ожидания")
    def getresult(self, timeout=60) -> str:
        """
        Ожидает появления результата и получает его.
        """

        try:
            # Сначала ждем, когда элемент станет видимым
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.result))

            # Ждем, когда результат вычислится (не содержит операторы + - * /)
            def is_result_calculated(driver):
                try:
                    element = driver.find_element(*self.result)
                    text = element.text.strip()
                    # Результат готов, если он не пустой, не содержит
                    # операторы и является числом
                    if (text and not any(op in text for op in
                                         ['+', '-', '*', '/', '='])):
                        # Проверяем, что это число
                        try:
                            float(text)
                            return True
                        except ValueError:
                            return False
                    return False
                except Exception:
                    return False

            WebDriverWait(self.driver, timeout).until(is_result_calculated)

            result = self.driver.find_element(*self.result)
            return result.text.strip()

        except Exception as e:
            # Если основной селектор не работает, пробуем альтернативные
            alternative_selectors = [
                (By.ID, "result"),
                (By.CSS_SELECTOR, ".screen"),
                (By.CSS_SELECTOR, "#result"),
                (By.XPATH, "//div[contains(@class, 'screen')]")
            ]

            for selector in alternative_selectors:
                try:
                    element = WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located(selector))
                    text = element.text.strip()
                    # Проверяем, что это результат вычисления
                    if (text and not any(op in text for op in
                                         ['+', '-', '*', '/', '='])):
                        try:
                            float(text)
                            return text
                        except ValueError:
                            continue
                except Exception:
                    continue

            raise e
