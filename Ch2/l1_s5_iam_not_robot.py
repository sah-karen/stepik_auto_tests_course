from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.CSS_SELECTOR, ".form-group input") #  "nput#answer"
    input.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, ".form-check-custom input")
    checkbox.click()

    robot = browser.find_element(By.CSS_SELECTOR, ".form-radio-custom input")
    robot.click()

    time.sleep(3)

    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла