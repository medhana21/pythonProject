from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.amazon.in/mobile-phones/b/?ie=UTF8&node=1389401031&ref_=nav_cs_mobiles")
driver.maximize_window()
driver.implicitly_wait(10)

# self.driver.execute_script("window.scrollBy(0,120)","")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

#driver.get_screenshot_as_file('file.png')
driver.get_screenshot_as_file('C:\\Users\\Medhana Harihar\\PycharmProjects\\pythonProject\\SeleniumFunctions\\screenshot.png')

print("Scrolling down and captured screenshot suceesfully")

driver.close()