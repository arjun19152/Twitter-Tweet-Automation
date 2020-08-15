from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains as ac
from selenium.common.exceptions import NoSuchElementException
check = 0
tweet = input("Enter your tweet")
req = input("Do you want to attach a pic(Y/N)??")
if req == 'Y' or req == 'y':
    check = 1
driver = webdriver.Chrome(executable_path=r"C:\Users\91885\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://www.twitter.com")
driver.maximize_window()
driver.implicitly_wait(3)
available=1

try:
    element=driver.find_element_by_name('session[username_or_email]')
    available=1
except NoSuchElementException:
    available=0


if available==1:
    email = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.NAME,
                                                                        'session[username_or_email]')))
    email.click()
    email.send_keys('<Enter your email ID>')
    password = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.NAME,
                                                                           'session[password]')))
    password.click()
    password.send_keys('<Enter your password>')
    password.send_keys(Keys.ENTER)
else:
    email = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH,
                                                                        '/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[1]/div/label/div/div[2]/div/input')))
    email.click()
    email.send_keys('<Enter your email ID>')
    password = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH,
                                                                           '/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[2]/div/label/div/div[2]/div/input')))
    password.click()
    password.send_keys('<Enter your password>')
    password.send_keys(Keys.ENTER)

block = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH,
                                                                    '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')))
block.click()
block.send_keys(tweet)

if check == 1:
    pic = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH,
                                                                      '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div')))
    ac(driver).move_to_element(pic).click().perform()
    time.sleep(6)

post = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,
                                                                   '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')))
post.click()

time.sleep(6)
driver.quit()
