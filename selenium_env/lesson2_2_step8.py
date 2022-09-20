import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

try:
    first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    first_name.send_keys('Fltk')
    last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last_name.send_keys('Ffff')
    email = browser.find_element(By.NAME, "email")
    email.send_keys('qweeqwewq12312@ngngn.rw')

    select_file = browser.find_element(By.ID, 'file')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    select_file.send_keys(file_path)
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(30)
    browser.quit()