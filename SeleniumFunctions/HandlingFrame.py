from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.londonfreelance.org/courses/frames/index.html")


#driver.switch_to.frame(2)#by index #Method1.
#driver.switch_to.frame('main')#by name #Method2.

frame_element=driver.find_element(By.NAME,'main')#3.But creating webelement
driver.switch_to.frame(frame_element)

header=driver.find_element(By.CSS_SELECTOR,"body > h2")
print(header.text)

# if we have frame under frame
#driver.switch_to.parent_frame('main')
driver.switch_to.default_content()#back to page
