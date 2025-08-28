from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/ajax")

blue_button = driver.find_element(By.ID, "ajaxButton")
blue_button.click()

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "content"))
    )

    WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element
                                    ((By.ID, "content"),
                                     "Data loaded with AJAX get request."))
    text = element.text
    print(text)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()
