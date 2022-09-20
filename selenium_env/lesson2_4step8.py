import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

try:
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button_book = browser.find_element(By.ID, 'book')
    button_book.click()
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    x = str(math.log(abs(12*math.sin(int(x)))))

    input_1 = browser.find_element(By.ID, 'answer')
    input_1.send_keys(x)

    button_submit = browser.find_element(By.ID, 'solve')
    button_submit.click()

finally:
    time.sleep(20)
    browser.quit()

