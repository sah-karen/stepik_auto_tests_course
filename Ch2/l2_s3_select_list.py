from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(By.CSS_SELECTOR,"span#num1").text
    num2 = browser.find_element(By.CSS_SELECTOR,"span#num2").text
    sum = str(int(num1) + int(num2))
    
    #variant 1
    select = Select(browser.find_element(By.TAG_NAME,"select"))
    select.select_by_value(sum)
    
    #variant 2
    # 3browser.find_element(By.TAG_NAME,"select").click()
##    browser.find_element(By.CSS_SELECTOR,"[value='1']").click()
    # browser.find_element(By.CSS_SELECTOR,f'[value="{sum}"]').click()
    # browser.find_element(By.CSS_SELECTOR,'[value="'+ sum + '"]').click()

    browser.find_element(By.CSS_SELECTOR,"button.btn").click()

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(10)
    browser.quit()
