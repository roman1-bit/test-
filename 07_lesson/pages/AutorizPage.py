from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AutorizPage:
    def __init__(self, browser):
        self.driver = browser
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def authorization_fields(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys("secret_sauce")

    def button_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        WebDriverWait(self.driver, 5).until_not(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, "#login-button")))
