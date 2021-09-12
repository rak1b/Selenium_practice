from selenium import webdriver
import time

# url = 'https://online2pdf.com/doc-to-pdf'
url = 'https://www.filemail.com/share/upload-file'

browser = webdriver.Chrome('C:/chromedriver/chromedriver.exe')

browser.get(url+'/login')
browser.maximize_window()
#openning landing page

time.sleep(3)

file_input = browser.find_element_by_xpath("//input[@type='file']")
# file_input = browser.find_element_by_xpath('//div[@class="input_field"]/input')
file_input.send_keys('G:\\MyPracticesHere\\Python\\Selenium\\test.docx')

# change_btn = browser.find_element_by_xpath('//button[@class="convert_button"]').click()