from selenium import webdriver

# Good - http://suninjuly.github.io/registration1.html
# Bad - http://suninjuly.github.io/registration2.html # ERROR HERE: No such element exception

# Измени ссылку (link), чтобы проверить 

link = "http://suninjuly.github.io/registration1.html"  


browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_css_selector ('div.first_block div.first_class input[placeholder="Input your first name"].first')
input1.send_keys("No name")

input2 = browser.find_element_by_css_selector ('div.first_block div.second_class input[placeholder="Input your last name"].second')
input2.send_keys("No last name")

input3 = browser.find_element_by_css_selector('div.first_block div.third_class input[placeholder="Input your email"].third')
input3.send_keys("No email")

input4 = browser.find_element_by_css_selector('div.second_block div.first_class input[placeholder="Input your phone:"].first')
input4.send_keys("No phone number")

input4 = browser.find_element_by_css_selector('div.second_block div.second_class input[placeholder="Input your address:"].second')
input4.send_keys("No address")

button = browser.find_element_by_xpath('//button[text()="Submit"]')
button.click()

