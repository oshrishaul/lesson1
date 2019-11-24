import time

from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path="C:\\Users\\shaulo2\\Desktop\\Python Stuff\\chromedriver_win32\\chromedriver.exe")
# driver.get("https://gofile.io/?t=uploadFiles")
# driver.find_element_by_id("btnChooseFiles").send_keys("C:/Temp/1.txt")
# driver_2 = webdriver.Firefox(executable_path="C:\\Users\\shaulo2\\Desktop\\Python Stuff\\geckodriver-v0.26.0-win64\\geckodriver.exe")
# driver_2.get("http://www.ynet.co.il")
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
browser = webdriver.Chrome(executable_path="C:\\Users\\shaulo2\\Desktop\\Python Stuff\\chromedriver_win32\\chromedriver.exe", options=chrome_options).get("https://github.com")
time.sleep(10)
# browser.get("https://github.com")