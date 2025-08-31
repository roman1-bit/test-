from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, browser):
        self.driver = browser
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def fill_in_the_fields(self):
        self.driver.find_element(
            By.NAME, "first-name").send_keys("Иван")
        self.driver.find_element(
            By.NAME, "last-name").send_keys("Петров")
        self.driver.find_element(
            By.NAME, "address").send_keys("Ленина, 55-3")
        self.driver.find_element(
            By.NAME, "city").send_keys("Москва")
        self.driver.find_element(
            By.NAME, "country").send_keys("Россия")
        self.driver.find_element(
            By.NAME, "e-mail").send_keys("test@skypro.com")
        self.driver.find_element(
            By.NAME, "phone").send_keys("+7985899998787")
        self.driver.find_element(
            By.NAME, "job-position").send_keys("QA")
        self.driver.find_element(
            By.NAME, "company").send_keys("SkyPro")

    def submit(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "button[type=submit]").click()
        WebDriverWait(self.driver, 10).until_not(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, "btn.btn-outline-primar.mt-3")))

    def get_zip_code_class(self):
        return self.driver.find_element(By.ID, "zip-code").get_attribute(
            "class")

    def get_fields_classes(self):
        poles = [
            "#first-name", "#last-name", "#address", "#city",
            "#country", "#e-mail", "#job-position", "#phone", "#company"]
        field_classes = []
        for pole in poles:
            pole_class = self.driver.find_element(
                By.CSS_SELECTOR, pole).get_attribute("class")
            field_classes.append(pole_class)
        return field_classes
