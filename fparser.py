from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time

driver = webdriver.Firefox()  # or another

# USE ONLY TECHNICAL\UNNECESSARY ACCOUNT

driver.get('https://www.instagram.com/accounts/login/')
time.sleep(2)
psw = driver.find_element_by_name('password')
psw.send_keys('TECH_ACCOUNT_PASSWORD')
time.sleep(1)
user = driver.find_element_by_name('username')
user.send_keys('TECH_ACCOUNT_NAME')
time.sleep(1)
user.submit()
time.sleep(5)

time.sleep(2)
driver.get('URL of account, where to get subscribers')
time.sleep(2)
a = ''

number_of_followers = driver.find_element_by_css_selector(
    'li.Y8-fY:nth-child(2) > a:nth-child(1) > span:nth-child(1)').get_attribute('title')
nof = int(number_of_followers.replace(" ", '')) - 1

open_followers_panel = driver.find_element_by_css_selector('li.Y8-fY:nth-child(2) > a:nth-child(1)').click()
fpanel = driver.find_element_by_css_selector('.isgrP')
time.sleep(1)
fpanel.send_keys(Keys.PAGE_DOWN)

followers = ''

while len(followers) < 500: # HOW MUCH TO PARSE
    followers = driver.find_elements_by_class_name('wo9IH')
    fpanel.send_keys(Keys.END)
    time.sleep(1)

html = fpanel.get_attribute('innerHTML')
soup = bs(html, 'html.parser')
divs = soup.find_all('li', {'class': 'wo9IH'})
accs = open('accs.txt', 'w')

for div in divs:
    href = div.find('a').get('href')
    accs.write('https://www.instagram.com' + href + '\n')

driver.close()
accs.close()
