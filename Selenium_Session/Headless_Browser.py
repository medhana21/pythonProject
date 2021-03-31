from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

option=webdriver.ChromeOptions()
option.headless=True
driver=webdriver.Chrome(ChromeDriverManager().install(),options=option)
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")
print(driver.title)
