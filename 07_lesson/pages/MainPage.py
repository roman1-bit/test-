from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, browser):
        self.driver = browser

    def add_product(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    def icon_cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#shopping_cart_container").click()
