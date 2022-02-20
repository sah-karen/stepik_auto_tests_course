from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pyperclip

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = " http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH,"//body/div/div/div//h5[@id]"),"100"))
    
    browser.find_element(By.XPATH,"//body/div/div/div/button").click()

    x = browser.find_element(By.XPATH,"//form/div/div/div//span[@id]").text
    y = calc(x)
    browser.find_element(By.XPATH,"//form/div/div/div/input").send_keys(y)

    browser.find_element(By.XPATH,"//form/div/div/button").click()

    # we want copy the alert answer to buffer
    alert = browser.switch_to.alert
    alert_text = alert.text
    add_to_clip_board = alert_text.split(': ')[-1]
    pyperclip.copy(add_to_clip_board)


finally:
    time.sleep(8)
    browser.quit()
