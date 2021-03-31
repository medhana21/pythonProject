from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
browserName ="chrome"

if browserName=="chrome":
    driver=webdriver.Chrome(ChromeDriverManager().install())
elif browserName=="firefox":
        driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName=="safari":
         driver =webdriver.safari()
else:
    print("please pass the correct rowser name:"+browserName)
    raise Exception('driver not found') #opera
driver.implicitly_wait(10)
driver.get("https://osmarket.in/members/index.php?mod=login")
driver.find_element(By.ID,'mlmuid').send_keys("medhana.21@gmail.com")
driver.find_element(By.ID,'passw').send_keys("Med@12345")
driver.find_element(By.NAME,'sb').click()
print(driver.title)
time.sleep(4)
driver.quit()