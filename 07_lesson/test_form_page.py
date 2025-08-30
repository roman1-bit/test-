from selenium import webdriver
from pages.FormPage import FormPage


def test_fill_form():
    browser = webdriver.Firefox()

    form_page = FormPage(browser)
    form_page.open()
    form_page.fill_in_the_fields()
    form_page.submit()

    form_page.check_zip_code_error()
    form_page.check_fileds_success()

    browser.quit()
