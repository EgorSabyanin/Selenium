from selenium import webdriver
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id('num1')
    num2 = browser.find_element_by_id('num2')

    summa = int(num1.text) + int(num2.text)

    options = browser.find_elements_by_css_selector("option[value]")

    for i in options:
        if summa == int(i.get_attribute('value')) and i.text != '--':
            i.click()

    submit = browser.find_element_by_css_selector("button[type='submit']")
    submit.click()

finally:
    time.sleep(30)
    browser.quit()
    print("Finish of test")