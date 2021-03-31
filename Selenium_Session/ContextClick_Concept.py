from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

cont_ciick=driver.find_element(By.XPATH,"//span[text()='right click me']")
action_chain=ActionChains(driver)
action_chain.context_click().perform()

RightClick_Options=driver.find_elements(By.CSS_SELECTOR,"li.context-menu-icon span")
for ele in RightClick_Options:
    print(ele.text)
    if ele.text == 'copy':
        ele.click()
        break