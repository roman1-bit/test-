from selenium import webdriver
from pages.FormPage import FormPage


def test_fill_form():
    browser = webdriver.Firefox()

    form_page = FormPage(browser)
    form_page.open()
    form_page.fill_in_the_fields()
    form_page.submit()

    zip_code_class = form_page.get_zip_code_class()
    assert zip_code_class == "alert py-2 alert-danger"
    
    field_classes = form_page.get_fields_classes()
    for field_class in field_classes:
        assert field_class == "alert py-2 alert-success"

    browser.quit()
