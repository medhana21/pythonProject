from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.add_cookie({"name":"dsafdds","domain":"amazon.com"})

cookies=driver.get_cookies()#return one dictionary
for cook in cookies:
    print(cook)

print(len(cookies))
driver.quit()