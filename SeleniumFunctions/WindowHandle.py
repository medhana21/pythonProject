from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()
driver.implicitly_wait(10)


driver.find_element(By.XPATH,"//*[@id='Tabbed']/a/button").click() #click on button it will open new window

print(driver.current_window_handle)#get the value of current window #CDwindow-3E47322A156C0724991DA6701646E81B

handles=driver.window_handles# return value of all window #['CDwindow-FB421DF8F061298806622F0F23823489', 'CDwindow-98B068A0DFD6CBA2C42E9DADE24DB19E']

print(handles)

for handle in handles:
    driver.switch_to.window(handle) # It will switch to perticular window
    print(driver.title)
    #close perticular browser
    if(driver.title=='Frames & windows'):
        driver.close()#close only parent window

driver.quit()#close all window