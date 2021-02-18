from selenium import webdriver
import time
import sys

edge_driver = webdriver.Edge(executable_path='C:/Users/ahmad/Desktop/msedgedriver.exe')
edge_driver.get('https://moodle.uni-luebeck.de/login/index.php')

time.sleep(10)

user_name = input("your mtr: ")
user = edge_driver.find_element_by_xpath(".//*[@id='username']")
user.send_keys(user_name)

time.sleep(1)

user_password = input("your password: ")
password = edge_driver.find_element_by_xpath(".//*[@id='password']")
password.send_keys(user_password)

time.sleep(1)

login = edge_driver.find_element_by_xpath(".//*[@id='loginbtn']")
login.click()

sys.exit()