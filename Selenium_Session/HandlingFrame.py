from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://login.salesforce.com/?locale=in")

get_ele=driver.find_element(By.XPATH,"//label[contains(text(),'Username')]")
get_element1=get_ele.text
print("text on element is :"+get_element1)

#Method1driver.switch_to.frame(2)#by index
#2.driver.switch_to.frame('main')#by name
'''
frame_element=driver.find_element(By.NAME,'main')#3.Bt create webelement
driver.switch_to.frame(frame_element)

header=driver.find_element(By.CSS_SELECTOR,"body > h2")
print(header.text)
# if we have frame under frame
#driver.switch_to.parent_frame('main')
driver.switch_to.default_content()#back to page
'''