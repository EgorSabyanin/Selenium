from selenium import webdriver
import math 
import time

from calc import calc

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    submit = browser.find_element_by_css_selector('[type="submit"')
    submit.click()

    browser.switch_to.window(browser.window_handles[1])
    
    x = browser.find_element_by_id("input_value")
    y = calc((int(x.text)))

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    submit = browser.find_element_by_css_selector('[type="submit"]')
    submit.click()

finally:
    time.sleep(30)
    print("Test passed")
    browser.quit()