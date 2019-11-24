# Selenium - סט כלים לאוטומציית ווב  |  Selenium Web Driver
# Every WebPage build from 3 elements:
# html, css, JavaScript
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\shaulo2\\Desktop\\Python Stuff\\chromedriver_win32\\chromedriver.exe")
# driver.get("http://www.google.com") # get
# print(driver.current_url) # current_url
# print(driver.title) # title
# print(driver.page_source) # page_source
# driver.close()
# driver.quit() # use always at the end of the test to close chrome for sure

driver.get("https://translate.google.com")
driver.implicitly_wait(10) # Will wait UNTIL 10 sec to get rusaults for find_element\s
elements = driver.find_element_by_id("source").click()
x = driver.find_element_by_id("source")
if x.is_enabled() == True:
    x.send_keys("Enabled",)
    driver.find_element_by_id("source").send_keys(Keys.ENTER)  # יקיש "אנטר" אל האלמנט
    x.send_keys("עובד")
# print(len(elements)) # ידפיס את אורך הרשימה שהתקבלה
# driver.find_element_by_id("source").send_keys("hello")
# driver.quit()