from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element(By.ID, "book").click()

    x = browser.find_element(By.ID, "input_value").text
    y = log(abs(12 * sin(int(x))))

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "solve").click()

finally:
    print(browser.switch_to.alert.text)
    browser.quit()