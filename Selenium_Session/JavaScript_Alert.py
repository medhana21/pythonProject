from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[3]/button").click()
alert_v=driver.switch_to.alert
time.sleep(4)
alert_v.send_keys('hi Medhana')
#alert_v.accept()
alert_v.dismiss()
driver.switch_to.default_content()#switch back to page
time.sleep(4)
driver.quit()


