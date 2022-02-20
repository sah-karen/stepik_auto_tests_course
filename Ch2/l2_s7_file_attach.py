from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR,'input[name="firstname"]').send_keys("Petros")
    browser.find_element(By.CSS_SELECTOR,'input[name="lastname"]').send_keys("Petrosyan")
    browser.find_element(By.CSS_SELECTOR,'input[name="email"]').send_keys("pp.@invest.am")
    

    curr_dir = os.path.abspath(os.path.dirname(__file__))
    file_path =  os.path.join(curr_dir, "file.txt")
    # create file.txt in current python script directory
    file = open(file_path, "w")
    file.write("automationbypython") 
    file.close()

    browser.find_element(By.CSS_SELECTOR,'form > input[type="file"]').send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR,"button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
