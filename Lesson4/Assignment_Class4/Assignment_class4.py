# Write a program that does the following:
# 1. Write a script which will open the following:
# a. Chrome – http://www.walla.co.il
# b. FireFox – http://www.ynet.co.il
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chr_driver = webdriver.Chrome(executable_path="C:\\Users\\shaulo2\\Desktop\\Python Stuff\\chromedriver_win32\\chromedriver.exe")
ffx_driver = webdriver.Firefox(executable_path="C:\\Users\\shaulo2\\Desktop\\Python Stuff\\geckodriver-v0.26.0-win64\\geckodriver.exe")
chr_driver.get("http://www.walla.co.il")
ffx_driver.get("http://www.ynet.co.il")

#2. In one of the browsers you open do the following:
# a. Create a variable with the website’s title
# b. Refresh website
# c. Get website name and compare it to the variable you created in clause 1.
title = chr_driver.title
chr_driver.refresh()
if title == chr_driver.title:
    print("identical titles")

# 3. Open a few browsers, locate any element, does the element has the same locators in the other browser?
# Answer - Yes. The element has the same locator in all the browser sessions.

# 4. Create a test with the following:
# a. Open Google Translate web page
# b. Write anything in Hebrew in the text area
chr_driver.get("https://translate.google.com")
x = chr_driver.find_element_by_id("source")
x.send_keys("שלום")

# 5 a. Open Youtube web page
# b. Type a name of a song
# c. Click on search.
chr_driver.get("https://www.youtube.com/")
chr_driver.find_element_by_id("search").send_keys("rhcp", Keys.ENTER)

# 6. Open Chrome browser on Google Translate website: https://translate.google.com/
# Find translation text field (the one you send keys to) with 3 different locators and print the WebElement you created.
chr_driver.get("https://translate.google.com")
a = chr_driver.find_element_by_id("source")
b = chr_driver.find_element_by_class_name("orig")
c = chr_driver.find_element_by_xpath("//textarea[@autocomplete='off']")
print(c)

# 7 a. Open Chrome browser on Facebook website: https://www.facebook.com/
# b. Login into Facebook (No need to send me credentials).
chr_driver.get("https://www.facebook.com")
chr_driver.find_element_by_name("email").send_keys("abc@google.com")
chr_driver.find_element_by_name("pass").send_keys("password")

# 8 a. Open Chrome browser on any webpage.
# b. Delete all cookies from browser.
# c. Make sure all cookies are deleted by printing all cookies stored in the browser.
chr_driver.get("https://translate.google.com")
chr_driver.delete_all_cookies()
print(chr_driver.get_cookies())

# 9. a. Open any browser on "Github" website: https://github.com/
# b. Enter “Selenium” keyword in search textfield
# c. Press Enter to search (through code - of course).
chr_driver.get("https://github.com/")
chr_driver.find_element_by_class_name("form-control").send_keys("Selenium", Keys.ENTER)
