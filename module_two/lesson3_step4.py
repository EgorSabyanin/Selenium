from selenium import webdriver
import time
import math

from calc import calc

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    submit = browser.find_element_by_css_selector('[type="submit"]')
    submit.click()

    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element_by_id("input_value")
    y = calc((int(x.text)))

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    submit = browser.find_element_by_css_selector('[type="submit"]')
    submit.click()

finally:
    time.sleep(30)
    print("Finesh of test")
    browser.quit()