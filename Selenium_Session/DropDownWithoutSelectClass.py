from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.indiapassport.org/new-passport")
print(driver.title)


#not using select class by using  Xpath
State_option=driver.find_elements(By.XPATH,"//select[@id='contact_2_state']/option")


#generic Method
def select_values_bydropdown(dropdownOptionList,value):
    for ele in dropdownOptionList:
        print(ele.text)
        if (ele.text == value):
            ele.click()
            break


select_values_bydropdown(State_option,'Karnataka')
select_values_bydropdown(State_option,'Maharashtra')