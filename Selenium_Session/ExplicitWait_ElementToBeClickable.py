from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

wait=WebDriverWait(driver,5)
forget=wait.until(ec.element_to_be_clickable(By.LINK_TEXT,'Forgot Password?'))
print(forget.text)
forget.click()

fn=wait.until(ec.visibility_of_element_located(By.ID,'login1'))
fn.send_keys('medh')
