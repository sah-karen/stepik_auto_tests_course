from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element(By.CSS_SELECTOR, "span#input_value").text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, "input").send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    # execute js to scroll a view, to get access to button
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()

    browser.find_element(By.CSS_SELECTOR, "input#robotsRule").click()

    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    browser.quit()

