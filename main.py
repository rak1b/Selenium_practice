from selenium import webdriver
import time

browser = webdriver.Chrome('C:/chromedriver/chromedriver.exe')

browser.get('https://www.google.com')
time.sleep(2)

input = browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
input.send_keys("Find selenium")

submit = browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')

submit.click()
