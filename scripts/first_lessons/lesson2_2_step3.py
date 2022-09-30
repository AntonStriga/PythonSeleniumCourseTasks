from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = browser.find_element(By.ID, "num1").text
    x2 = browser.find_element(By.ID, "num2").text

    y = int(x1) + int(x2)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(y))
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(10)
    browser.quit()