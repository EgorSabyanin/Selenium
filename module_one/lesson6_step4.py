from selenium import webdriver
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"
# driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")  # <- Путь до файла хромдрайвера

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Egor")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Sabyanin")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # driver.close()
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    # driver.quit()

# не забываем оставить пустую строку в конце файла