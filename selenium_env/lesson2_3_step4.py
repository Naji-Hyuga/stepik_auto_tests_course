import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

try:
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element(By.ID, 'input_value')
    x = str(math.log(abs(12*math.sin(int(x.text)))))
    input_1 = browser.find_element(By.ID, 'answer')
    input_1.send_keys(x)
    button_submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button_submit.click()
finally:
    time.sleep(30)
    browser.quit()
