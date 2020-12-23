# This Python file uses the following encoding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PROXY = ""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=https://%s' % PROXY)

#Setup drivers
#Path to chromedriver for windows
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, options=chrome_options)

email = "pittawas.kijoran@gmail.com"
password = "ItsPoom123"

#Open the website from user input
driver.get("https://www.nike.com/th/launch/t/air-max-90-orange-duck-camo")

#Log in into nike website
menu = driver.find_element_by_xpath("//button[@aria-label='เมนู']")
driver.implicitly_wait(1)
menu.click()
login = driver.find_element_by_xpath("//button[@data-qa='join-login-button']")
login.click()
email = driver.find_element_by_xpath("//input[@placeholder='ที่อยู่อีเมล']")
email.send_keys("pittawas.kijoran@gmail.com")
password = driver.find_element_by_xpath("//input[@placeholder='รหัสผ่าน']")
password.send_keys("ItsPoom123")
login = driver.find_element_by_xpath("//input[@value='ลงชื่อเข้าใช้']").click()