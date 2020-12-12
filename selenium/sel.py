import time
from selenium import webdriver

driver = webdriver.Chrome('chromedriver86.exe')  # Optional argument, if not specified will search path.
driver.get('https://www.fedex.com/en-us/home.html')
time.sleep(3) # Let the user actually see something!
search_box = driver.find_element_by_class_name('fxg-user-options__sign-in-text')
search_box.click()
username = driver.find_element_by_name('user')
pswd = driver.find_element_by_name('pwd')
subButt = driver.find_element_by_class_name('fxg-button--orange')

time.sleep(2.5) # Let the user actually see something!
username.send_keys("uname")
time.sleep(2)
pswd.send_keys("pwrd")

time.sleep(2.4) # Let the user actually see something!
subButt.click()

time.sleep(66) # Let the user actually see something!
driver.quit()