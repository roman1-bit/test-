from selenium import webdriver
from pages.CalcPage import CalcPage


def test_calc():
    browser = webdriver.Chrome()

    calc_page = CalcPage(browser)
    calc_page.open()
    calc_page.input_field()
    calc_page.calculator_buttons()
    calc_page.output_field_result()
    calc_page.check_result()

    browser.quit()
