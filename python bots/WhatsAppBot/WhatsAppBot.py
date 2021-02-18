from selenium import webdriver
import time

edge_browser = webdriver.Edge(executable_path= 'C:/Users/ahmad/Desktop/msedgedriver')
edge_browser.get('https://web.whatsapp.com/')

time.sleep(10)

user_name = "Mama"

user = edge_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name)) #by injection
user.click()

message_box = edge_browser.find_element_by_xpath('//div[@class="DuUXI"]') 
message_box.send_keys("كيفك ")

send_box = edge_browser.find_element_by_xpath('//button[@class="_2Ujuu"]')
send_box.click()
