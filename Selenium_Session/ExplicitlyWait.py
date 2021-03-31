from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://app.hubspot.com/login/")
wait=WebDriverWait(driver,10)
email=wait.until(ec.presence_of_element_located(By.ID,'username'))
email.send_keys('ygygy@hbj.com')
driver.find_element(By.ID,'password').send_keys('fcguhink')
