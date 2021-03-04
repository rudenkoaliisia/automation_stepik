from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element_by_tag_name("img")
    x = treasure.get_attribute("valuex")

    answer = math.log(abs(12 * math.sin(int(x))))

    input = browser.find_element_by_id("answer")
    input.send_keys(str(answer))

    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robot_checkbox.click()

    radio_button = browser.find_element_by_id("robotsRule")
    radio_button.click()


    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла