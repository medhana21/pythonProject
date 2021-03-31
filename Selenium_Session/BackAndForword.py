from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT,'Best Sellers').click()
time.sleep(2)
driver.back()
driver.forward()
driver.back()
driver.refresh()
driver.quit()