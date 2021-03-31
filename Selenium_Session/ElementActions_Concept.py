from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://classic.crmpro.com/")
time.sleep(5)
driver.maximize_window()
usernm_ele=driver.find_element(By.NAME,'username')
pwd_ele=driver.find_element(By.NAME,'password')
sub_ele=driver.find_element(By.XPATH,"//input[@type='submit']")

act_Chain=ActionChains(driver)
act_Chain.send_keys_to_element(usernm_ele,'jsncns')
act_Chain.send_keys_to_element(pwd_ele,'dvgfd')
act_Chain.click(sub_ele).perform()

