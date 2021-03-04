from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button").click()


    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]

    browser.switch_to.window(new_window)

    x = browser.find_element_by_id("input_value")
    answer = math.log(abs(12 * math.sin(int(x.text))))

    input = browser.find_element_by_id("answer")
    input.send_keys(str(answer))

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла