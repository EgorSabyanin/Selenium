from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time

from calc import calc

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    if text:
        button = browser.find_element_by_id('book')
        button.click()

        x = browser.find_element_by_id('input_value')
        y = calc(int(x.text))

        answer = browser.find_element_by_id('answer')
        answer.send_keys(y)

        submit = browser.find_element_by_id('solve')
        submit.click()

finally:
    time.sleep(30)
    browser.quit()
    print("Finesh of test")