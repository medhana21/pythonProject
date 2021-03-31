from selenium import webdriver


class title():
    def test(self):
        driver = webdriver.Chrome(executable_path="F:\\Selenium\\chromedriver1.exe")
        url = "https://www.amazon.in/"
        driver.get(url)

        title = driver.title
        print("Title of the web page is: " + title)
        # print(driver.title)


ff = title()
ff.test()