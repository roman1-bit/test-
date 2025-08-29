from selenium import webdriver
from pages.AutorizPage import AutorizPage
from pages.MainPage import MainPage
from pages.CartPage import CartPage
from pages.DesignPage import DesingPage


def test_shop():
    browser = webdriver.Firefox()

    autoriz_page = AutorizPage(browser)
    autoriz_page.open()
    autoriz_page.authorization_fields()
    autoriz_page.button_login()

    main_page = MainPage(browser)
    main_page.add_product()
    main_page.icon_cart()

    cart_page = CartPage(browser)
    cart_page.button_checkout()

    desing_page = DesingPage(browser)
    desing_page.user_fields()
    desing_page.button_continue()
    desing_page.check_total

    browser.quit()
