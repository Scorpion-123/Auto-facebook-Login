import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Initilizing the chrome driver.
driver=webdriver.Chrome("chromedriver.exe")
#Opening the webpage.
driver.get("https://www.facebook.com/")
driver.implicitly_wait(10)
username=driver.find_element_by_id("email")
username.send_keys("enter your facebook's username here")
# This implicit waits are used for the connection delay caused sue to network issues.
driver.implicitly_wait(5)
password=driver.find_element_by_id("pass")
password.send_keys("enter your facebook's password here")
driver.implicitly_wait(10)
button = driver.find_element_by_name("login")
button.click()
driver.implicitly_wait(15)
