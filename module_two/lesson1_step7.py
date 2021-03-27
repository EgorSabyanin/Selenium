from selenium import webdriver
from calc import calc

link = "http://suninjuly.github.io/get_attribute.html"


print(calc(5))
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(link)

treasure = browser.find_element_by_id('treasure')

    
submit = browser.find_element_by_css_selector("[type='submit']")
submit.click()

x = treasure.get_attribute('valuex')
y = calc(x)

answer = browser.find_element_by_id("answer")
answer.send_keys(y)

robot = browser.find_element_by_id("robotCheckbox")
robot.click()

checkBox = browser.find_element_by_id("robotsRule")
checkBox.click()

submit = browser.find_element_by_css_selector("[type='submit']")
submit.click()
