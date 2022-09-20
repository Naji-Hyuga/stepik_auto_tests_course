from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

try:
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")

    x = str(math.log(abs(12*math.sin(int(x.text)))))
    input_1 = browser.find_element(By.ID, 'answer')
    input_1.send_keys(x)
    button_submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button_submit.click()
    
finally:
    time.sleep(30)
    browser.quit()

