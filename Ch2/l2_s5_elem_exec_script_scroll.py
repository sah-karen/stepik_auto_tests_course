from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    #browser.execute_script("alert('Robots at work');")
    #browser.execute_script('document.title="Script executing";')

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(10)
    browser.quit()

