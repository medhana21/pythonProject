from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://the-internet.herokuapp.com/upload")
driver.find_element(By.ID,'file-upload').send_keys('C:/Users/Medhana Harihar/Desktop/Selenium/Feautures.docx')
driver.find_element(By.ID,'file-submit').click()
time.sleep(3)
