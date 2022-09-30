import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.XPATH, "//input [@name='firstname']").send_keys("Ivan")
    browser.find_element(By.XPATH, "//input [@name='lastname']").send_keys("Petrov")
    browser.find_element(By.XPATH, "//input [@name='email']").send_keys("test@test.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'lesson2_2_step8.txt')
    browser.find_element(By.ID, "file").send_keys(file_path)

    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(10)
    browser.quit()
