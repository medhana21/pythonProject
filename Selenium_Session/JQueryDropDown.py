from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

driver.find_element(By.ID,'justAnInputBox').click()

time.sleep(3)


def Drop_Down_Element(DropDown_List,value):#Generic method
    if not value[0]=='all':
        for ele in DropDown_List:
            print(ele.text)
            for k in range(len(value)): # using Array of list
                if(ele.text == value[k]):
                    ele.click()
                    break
    else:
        try:
            for ele in DropDown_List:
                ele.click()
        except Exception as e:
            print(e)
DropDown_List=driver.find_elements(By.CSS_SELECTOR,'span.comboTreeItemTitle')

#for passing the list
values_list=['choice 2 3', 'choice 5', 'choice 1', 'choice 3']#multi select
#values_list=['choice 2']#single select
#values_list=['all']#select all

Drop_Down_Element(DropDown_List,values_list)
#Drop_Down_Element(DropDown_List,'choice 3') Instead of writting these value many times we use array of list
#Drop_Down_Element(DropDown_List,'choice 1')
#Drop_Down_Element(DropDown_List,'choice 5')
