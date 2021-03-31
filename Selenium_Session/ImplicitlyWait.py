from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://app.hubspot.com/login/")
driver.implicitly_wait(10)
driver.find_element(By.ID,'username').send_keys('ash@ghkal.com')
#max time out 10sec
#dynamic wait
#apply for all web element
#also called global wait
#apply for find_element & find_elements
# for changing time if it is not required for nxt element then we have to writeit for many times
# can't apply for browser/alert/any non web Element
# only apply on webelement
