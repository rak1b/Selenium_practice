email = 'www.rakib767676@gmail.com'
passw = 'likeit'

from selenium import webdriver
import time

browser = webdriver.Chrome('C:/chromedriver/chromedriver.exe')

browser.get('https://www.facebook.com')
time.sleep(3)

email_inp = browser.find_element_by_xpath('//*[@id="email"]')
email_inp.send_keys(email)
pass_inp = browser.find_element_by_xpath('//*[@id="pass"]')
pass_inp.send_keys(passw)

time.sleep(1)


# submit_btn = browser.find_element_by_xpath('//*[@id="u_0_k_rt"]')
submit_btn = browser.find_element_by_css_selector("button[name='login']").click()

time.sleep(3)


# search_btn = browser.find_element_by_xpath('//*[@id="mount_0_0_aK"]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/label/input').click()

# search_input = browser.find_element_by_xpath('//*[@id="mount_0_0_BF"]/div/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/label/input')



# search_input.send_keys('Prapty Chowdhury')

msg = browser.find_elements_by_css_selector("[aria-label=Messenger]")
print(msg)