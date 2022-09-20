import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')
try:
    num1, num2 = browser.find_element(By.ID, 'num1').text, browser.find_element(By.ID, 'num2').text
    num = str(int(num1) + int(num2))
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_visible_text(num)
    button_submit = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(30)
    browser.quit()

