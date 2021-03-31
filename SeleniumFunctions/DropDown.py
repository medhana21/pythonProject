from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.indiapassport.org/new-passport")
print(driver.title)

def select_values(element,value): #crating method
    select=Select(element)
    select.select_by_index("2")
    #select.select_by_value(6)
ele_state=driver.find_element(By.XPATH,"//select[@id='contact_2_state']")
#ele_district=driver.find_element(By.XPATH,"//select[@id='contact_2_district']")
#ele_employement=driver.find_element(By.CSS_SELECTOR,"select[id='sel_emp_type']")

driver.implicitly_wait(5)
select_values(ele_state,'3')
#select_values(ele_district,'6') #calling method by value
#select_values(ele_employement,'6')


#Choose the State karnataka and click
select=Select(ele_district)
dist_list=select.options

for ele in dist_list:
    print(ele.text)
    if(ele.text == 'Gadag'):
        ele.click()
        break