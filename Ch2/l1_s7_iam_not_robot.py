from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.CSS_SELECTOR, "img")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, "input").send_keys(y)

    browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()

    browser.find_element(By.CSS_SELECTOR, "input#robotsRule").click()

    browser.find_element(By.CSS_SELECTOR,"button.btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла