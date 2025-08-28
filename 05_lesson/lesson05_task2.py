from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/dynamicid")

button = driver.find_element(By.CLASS_NAME, "btn-primary")
button.click()
