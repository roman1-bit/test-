from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, browser):
        self.driver = browser
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
            )

    def input_field(self):
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

    def calculator_buttons(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

    def output_field_result(self):
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".screen")))
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, ".screen"), "15"))

    def check_result(self):
        res = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert res == "15"
