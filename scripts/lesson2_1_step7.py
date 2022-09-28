from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    y = log(abs(12 * sin(int(x))))

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(10)
    browser.quit()