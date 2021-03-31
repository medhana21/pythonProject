from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.switch_to.frame(driver.find_element_by_css_selector(".demo-frame"))

source = driver.find_element(By.ID,'draggable')
target = driver.find_element(By.ID,'droppable')

act_chains=ActionChains(driver)
#act_chains.drag_and_drop(source,target).perform() #directMethod
act_chains.click_and_hold(source).move_to_element(target).release().perform()

#driver.get_screenshot_as_file('droppable.png')

driver.get_screenshot_as_file('file.png')