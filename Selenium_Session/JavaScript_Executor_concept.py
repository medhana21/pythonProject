from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
#Bestseller_link=driver.find_element(By.LINK_TEXT,'Best Sellers')
#driver.execute_script("arguments[0].click();",Bestseller_link)#clicking on BestSellerLink
#title=driver.execute_script("return document.title;")#getting title
#print(title)
#driver.execute_script("history.go(0);")#clear the history
#driver.execute_script("alert('hello selenium');")# create alert msg
#inner_Text=driver.execute_script("return document.documentElement.innerText")#getting innertext from page
#print(inner_Text)
#image=driver.find_element(By.CSS_SELECTOR,'#zg_left_col1 > div.zg_homeWidget > div:nth-child(3) > div > div.a-section.a-spacing-none.p13n-asin > a > div.a-section.a-spacing-mini > img')
#creating border for a specific element
#driver.execute_script("arguments[0].style.border='3px solid red'",image)
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight")#scroll to bottom of page
#driver.execute_script("window.scrollTo(document.body.scrollHeight,0")#scroll to top of page
#text=driver.find_element(By.CSS_SELECTOR,"#zg_learnMore")
#driver.execute_script("arguments[0].scrollIntoView(true);",text)#stop scrolling when i get this text
#print(driver.execute_script("return navigator.userAgent;"))
driver.execute_script("document.getElementById('ap_email'),value='medhana@gmail.com';")