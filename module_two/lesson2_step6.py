from selenium import webdriver
import math, time

link="http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value")
    y = calc((int(x.text)))

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    robotCheckbox = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    robotCheckbox.click()
    
    browser.execute_script("window.scrollBy(0, 150);")
    
    robotRule = browser.find_element_by_css_selector('[for="robotsRule"]')
    robotRule.click()

    submit = browser.find_element_by_css_selector('[type="submit"]')
    submit.click()


finally:
    time.sleep(30)
    browser.quit()
    print("Test pass")