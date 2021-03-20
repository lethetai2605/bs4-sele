from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path="chromedriver.exe")

browser.get("http://facebook.com")

txtUser = browser.find_element_by_id("email")
txtUser.send_keys("david.t7923@gmail.com")

txtPass = browser.find_element_by_id("pass")
txtPass.send_keys("12345tai")

txtPass.send_keys(Keys.ENTER)

# sleep(10)
# browser.close()