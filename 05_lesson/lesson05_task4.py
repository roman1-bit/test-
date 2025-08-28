from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://the-internet.herokuapp.com/login')

username_field = browser.find_element(By.ID, "username")
username_field.send_keys('tomsmith')

password_field = browser.find_element(By.ID, 'password')
password_field.send_keys('SuperSecretPassword!')

login_button = browser.find_element(By.CSS_SELECTOR, '.fa-sign-in')
login_button.click()

success_message = browser.find_element(By.CSS_SELECTOR, '.flash.success')
print(success_message.text)
browser.quit()
