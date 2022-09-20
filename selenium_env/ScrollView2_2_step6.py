import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/execute_script.html')



try:
    x = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = str(math.log(abs(12*math.sin(int(x.text)))))
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(x)
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    button.click()

finally:
    time.sleep(20)
    browser.quit()

