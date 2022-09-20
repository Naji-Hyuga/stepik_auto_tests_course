import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')

try:
    num1, num2 = browser.find_element(By.ID, 'num1'), browser.find_element(By.ID, 'num2')
    num = str(int(num1.text) + int(num2.text))

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_visible_text(num)

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(20)
    browser.quit()

