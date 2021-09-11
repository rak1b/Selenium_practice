url = 'https://www.okgrassrootsproject.com/'
email = 'mysterious2798@gmail.com'
passw = 'Rakibrk11'
from selenium import webdriver
import time

browser = webdriver.Chrome('C:/chromedriver/chromedriver.exe')

browser.get(url)
#openning landing page

time.sleep(3)

login_page_btn = browser.find_element_by_xpath('//*[@id="middle"]/div/div/div[2]/ul/li[3]/a').click()#clicking the Sign in with login option


time.sleep(3)

#inserting the login credentials
email_inp = browser.find_element_by_xpath('//*[@id="user_session_email"]')
email_inp.send_keys(email)

pass_inp = browser.find_element_by_xpath('//*[@id="user_session_password"]')
pass_inp.send_keys(passw)

login_btn = browser.find_element_by_xpath('//*[@id="middle"]/div/div/div[2]/div/div[2]/div/div/div[1]/form/div[4]/div/input').click()
time.sleep(3)


#openning the homepage after login

#going to the event page
def go_to_event():
    event_btn = browser.find_element_by_xpath('//*[@id="topnav"]/li[6]/a').click()
    time.sleep(3)


# Clicking host your own event link
def host_event():
    own_event_btn = browser.find_element_by_xpath('//*[@id="content"]/div[3]/a').click()
    time.sleep(3)

    #Fiiling up the form

    headline_input = browser.find_element_by_xpath('//*[@id="event_page_page_headline"]')
    headline_input.send_keys('Heres the headline')

    venue_input = browser.find_element_by_xpath('//*[@id="event_page_venue_name"]')
    venue_input.send_keys('Heres the venue')
    address_input = browser.find_element_by_xpath('//*[@id="event_page_venue_address_address1"]')
    address_input.send_keys('Heres the address')

    city_input = browser.find_element_by_xpath('//*[@id="event_page_venue_address_city"]')
    city_input.send_keys('Heres the city')

    time.sleep(3)

    # description_input = browser.find_element_by_xpath('//*[@id="tinymce"]"]')
    description_input = browser.find_element_by_xpath('//*[@id="event_page_content_editable_ifr"]')
    # description_input =  browser.find_element_by_id("tinymce").sendKeys("Dummy text");
    description_input.send_keys('New Heres the Description')

    submit_event = browser.find_element_by_xpath('//*[@id="calendar_page_new_event_page_form"]/div[2]/div/div[20]/input').click()
    time.sleep(5)

    
go_to_event()
host_event()
go_to_event()
host_event()
go_to_event()



