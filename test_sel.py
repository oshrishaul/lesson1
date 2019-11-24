from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\shaulo2\\Desktop\\Python Stuff\\chromedriver_win32\\chromedriver.exe")
driver.get("http://mako.co.il")
driver.quit()