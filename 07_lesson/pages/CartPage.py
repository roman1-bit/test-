from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, browser):
        self.driver = browser

    def button_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
        WebDriverWait(self.driver, 5).until_not(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, "#checkout")))
