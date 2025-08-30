from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DesingPage:
    def __init__(self, browser):
        self.driver = browser

    def user_fields(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys("Роман")
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys("Кирющенко")
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys("321543")

    def button_continue(self):
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()
        WebDriverWait(self.driver, 5).until_not(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, "#continue")))

    def check_total(self):
        res = self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text
        assert res == "Total: $58.29"
