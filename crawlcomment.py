from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
import re

#browser = webdriver.Chrome(executable_path="chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get("http://facebook.com")

txtUser = browser.find_element_by_id("email")
txtUser.send_keys("david.t7923@gmail.com")

txtPass = browser.find_element_by_id("pass")
txtPass.send_keys("12345tai")

txtPass.send_keys(Keys.ENTER)
sleep(random.randint(5,7))
#open tab
browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
# You can use (Keys.CONTROL + 't') on other OSs

# Load a page 
browser.get('https://mbasic.facebook.com/permalink.php?story_fbid=209364637568417&id=100054846464043')
# Make the tests...
sleep(random.randint(6,9))
# browser.execute_script("window.open('https://www.facebook.com/groups/miaigroup/permalink/903113787126561/', 'new_tab')")
# #browser.get("https://www.facebook.com/groups/miaigroup/permalink/903113787126561/")
# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications" : 2}
# chrome_options.add_experimental_option("prefs",prefs)

# sleep(random.randint(7,9))
# showcomment = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div/div/div[1]/div/div[2]")
# showcomment.click()
# sleep(random.randint(7,9))

i=1
while (i<6):
    show_more = browser.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div[2]/div/div[4]/div[1]/a")
    show_more.click()

    
    i=i+1

    comments = browser.find_elements_by_class_name('df')
    for comment in comments:
        #name = comment.find_element_by_class_name
        print(comment.find_element_by_tag_name('a').text)
        print("Link:"+ comment.find_element_by_tag_name('a').get_attribute('href'))
        # com = comment.find('a',class_='bj')
        # print (name.get('href'))


print ("tai dep trai")
# sleep(random.randint(5,7))
# comments = browser.find_elements_by_xpath("//div[@aria-label='Bình luận']")
# for comment in comments:
#     poster = comment.find_element_by_class_name("pq6dq46d")
#    # content = comment.find_element_by_class_name("kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql")
#     print(poster.text)
#     #print(content.text)
#     #print("*"+poster.text+":"+content.text)
# #comment_list = browser.find_elements_by_class_name
# # browser.close()