from selenium import webdriver
from selenium.webdriver.common.by import By
from math import *

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element(By.ID, "input_value").text
    y = log(abs(12 * sin(int(x))))

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    print(browser.switch_to.alert.text)
    browser.quit()