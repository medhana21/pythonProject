from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.spicejet.com/")
driver.maximize_window()

login_ele = driver.find_element(By.ID,'ctl00_HyperLinkLogin')
driver.implicitly_wait(5)

act_chains=ActionChains(driver)
act_chains.move_to_element(login_ele).perform()

#SpiceClub_ele=driver.find_element(By.LINK_TEXT,'SpiceClub Members')
#act_chains.move_to_element(SpiceClub_ele).perform()

Member_ele=driver.find_element(By.LINK_TEXT,'Travel Agent Login')
Member_ele.click()

driver.quit()