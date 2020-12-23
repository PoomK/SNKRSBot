from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

emailIn = "pittawas.kijoran@gmail.com"
passwordIn = "ItsPoom123"

driver.get("https://www.nike.com/th/launch")

time.sleep(3)

#Log in into nike website
menu = driver.find_element_by_xpath("//button[@aria-label='เมนู']")
driver.implicitly_wait(3)
menu.click()

login = driver.find_element_by_xpath("//button[@data-qa='join-login-button']")
login.click()

email = driver.find_element_by_xpath("//input[@placeholder='ที่อยู่อีเมล']")
email.click()
for character in emailIn:
    email.send_keys(character)
    time.sleep(random.uniform(0,0.000001))
# email.send_keys("nikeprofil4@gmail.com")

# time.sleep(1)

password = driver.find_element_by_xpath("//input[@placeholder='รหัสผ่าน']")
password.click()
for char in passwordIn:
    password.send_keys(char)
    time.sleep(random.uniform(0,0.000001))
# password.send_keys("ItsPoom123")

#time.sleep(1)

login = driver.find_element_by_xpath("//input[@value='ลงชื่อเข้าใช้']").submit()

print("Login complete")

time.sleep(3)
driver.implicitly_wait(5)

#Go to account settings
menuButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='mobile-nav-menu-button'][@class='d-sm-ib va-sm-m cart-button']")))
menuButton.click()
accountSettingsButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='settings-button'][@class='ncss-brand text-color-grey pt6-sm pb6-sm d-sm-b u-uppercase fs19-sm fs22-md fs16-lg bg-transparent']")))
accountSettingsButton.click()

time.sleep(3)
accountSettingsButton2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'บัญชี')]")))
accountSettingsButton2.click()