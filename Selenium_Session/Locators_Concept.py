from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
print(driver.title)

link_url=driver.find_element(By.LINK_TEXT,'Features')
username_url=driver.find_element(By.ID,'Form_submitForm_subdomain')#creating webelement username_url
firstName=driver.find_element(By.ID,'Form_submitForm_FirstName')
lastName=driver.find_element(By.ID,'Form_submitForm_LastName').send_keys('ana')
email=driver.find_element(By.ID,'Form_submitForm_Email').send_keys('ana@hmail.com')

link_url.click()
username_url.send_keys("Selenium lab")
firstName.send_keys('medh')
lastName.send_keys('ana')
email.send_keys('ana@hmail.com')

