from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value")
    answer = math.log(abs(12 * math.sin(int(x.text))))

    input = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(str(answer))

    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robot_checkbox.click()

    radio_button = browser.find_element_by_css_selector("[for='robotsRule']")
    radio_button.click()


    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла