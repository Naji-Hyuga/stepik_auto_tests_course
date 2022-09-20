import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))



browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/math.html')

try:
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text

    y = calc(x)

    input_1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_1.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"')
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, '[value="robots"]')
    radiobutton.click()

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(30)
    browser.quit()

