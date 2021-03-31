from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(executable_path="C:\\Users\\Medhana Harihar\\PycharmProjects\\pythonProject\\driver\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.google.com")
print(driver.title)
driver.find_element(By.NAME,'q').send_keys("Selenium")
optionsList=driver.find_elements(By.CSS_SELECTOR,'ul.erkvQe li span')
print(len(optionsList))
for ele in optionsList:
    print(ele.text)
    if(ele.text == 'selenium webdriver'):
        driver.click()
        print('I got selenium webdriver so stop further iteration')
        break
time.sleep(5)
driver.quit()