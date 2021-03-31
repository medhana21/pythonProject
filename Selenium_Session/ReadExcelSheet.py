from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import xlrd
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

urlval=driver.find_element(By.ID,'Form_submitForm_subdomain')
fnm=driver.find_element(By.ID,'Form_submitForm_FirstName')
lnm=driver.find_element(By.ID,'Form_submitForm_LastName')
email=driver.find_element(By.ID,'Form_submitForm_Email')
jtitle=driver.find_element(By.ID,'Form_submitForm_JobTitle')
cmny=driver.find_element(By.ID,'Form_submitForm_CompanyName')
phoneNo=driver.find_element(By.ID,'Form_submitForm_Contact')
temp=driver.find_element(By.ID,'Form_submitForm_NoOfEmployees')
indus=driver.find_element(By.ID,'Form_submitForm_Industry')
cntry=driver.find_element(By.ID,'Form_submitForm_Country')



workbook=xlrd.open_workbook("DataFile.xlsx")
sheet=workbook.sheet_by_name("registration")

#total no of rows & Colmn
rowCount=sheet.nrows
print("Rows"+rowCount)
clmCount=sheet.ncols
print("Column"+clmCount)

for curr_row in range(1,rowCount):
    url=sheet.cell_value(curr_row,0)#url
    firstname=sheet.cell_value(curr_row,1)#username
    lastname= sheet.cell_value(curr_row, 2)  #lastname
    emailid= sheet.cell_value(curr_row, 3)  # emailid
    jobtitle = sheet.cell_value(curr_row, 4)  # username
    company = sheet.cell_value(curr_row, 5)  # username
    phone=sheet.cell_value(curr_row,6)#username
    totalemp = sheet.cell_value(curr_row, 7)  # username
    industry = sheet.cell_value(curr_row, 8)  # username
    country = sheet.cell_value(curr_row, 9)  # username


    print(url+""+firstname+""+lastname+""+emailid)

    url.clear()
    urlval.send_keys(url)
    fnm.send_keys(firstname)
    firstname.clear()
    lnm.send_keys(lastname)
    lastname.clear()

    time.sleep(4)