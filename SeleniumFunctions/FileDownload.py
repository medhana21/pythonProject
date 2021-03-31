from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

chromeOptions=Options()
chromeOptions.add_experimental_option("prefs", {"download.default_directory": "C:\\Users\\Medhana Harihar\\PycharmProjects\\pythonProject\\SeleniumFunctions"})


driver=webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chromeOptions)

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
driver.implicitly_wait(10)

#download Text File
driver.find_element_by_id('textbox').send_keys("Hi Medhana This is World File")

driver.find_element_by_id('createTxt').click() #clicking generate button

driver.find_element_by_id('link-to-download').click() #click on download button

#download PDF File
driver.find_element_by_id('pdfbox').send_keys("Hi Medhana This is PDF File")

driver.find_element_by_id('createPdf').click()

driver.find_element_by_id('pdf-link-to-download').click()

time.sleep(5)
driver.close()


