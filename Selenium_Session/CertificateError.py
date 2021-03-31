from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#Chrome one way
#options=Options()
#options.add_argument('--allow--running-insecure-content')
#options.add_argument('--ignore-certificate-errors')
#driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)
#2ndway
#desired_capabilities=DesiredCapabilities().CHROME.copy()
#desired_capabilities['acceptInsecureCerts']=  True
#driver=webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities = DesiredCapabilities)
#3rd way
options=Options()
options.set_capability('acceptInsecureCerts',True)
driver=webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)

driver.implicitly_wait(5)
driver.get("https://expired.badssl.com/")
print(driver.find_element(By.TAG_NAME,'h1').text)
