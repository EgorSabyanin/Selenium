from selenium import webdriver
import os, time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element_by_name("firstname")
    lastname = browser.find_element_by_name("lastname")
    email = browser.find_element_by_name("email")

    firstname.send_keys("Egor")
    lastname.send_keys("Sabyanin")
    email.send_keys("test@gmail.com")

    file = browser.find_element_by_id('file')

    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_path = os.path.join(current_dir, 'test.txt')
    file.send_keys(file_path)

    submit = browser.find_element_by_css_selector('[type="submit"]')
    submit.click()

finally:
    time.sleep(30)
    browser.quit()
    print("Finesh of test")