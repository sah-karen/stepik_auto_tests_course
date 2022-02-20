from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR,"button.btn").click()
    # switch focus to redirected window
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x = browser.find_element(By.XPATH,"/html/body/form/div/div/div//span[@id]").text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, "input").send_keys(y)

    browser.find_element(By.CSS_SELECTOR,"button.btn").click()


finally:
    time.sleep(10)
    browser.quit()
