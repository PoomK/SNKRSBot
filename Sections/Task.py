# This Python file uses the following encoding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

#Setup drivers
#Path to chromedriver for windows
PATH = "C:\Program Files (x86)\chromedriver.exe"
#Path to chromedriver on mac
#PATH = "/applications/chromedriver"
driver = webdriver.Chrome(PATH)

sizeIn = "EU 39"
emailIn = "pittawas.kijoran@gmail.com"
passwordIn = "ItsPoom123"

#Set window size for mac
#driver.set_window_size(900, 1080)

#Open the website from user input
driver.get("https://www.nike.com/th/launch/t/air-max-90-orange-duck-camo")

time.sleep(3)

#Log in into nike website
menu = driver.find_element_by_xpath("//button[@aria-label='เมนู']")
driver.implicitly_wait(3)
menu.click()

login = driver.find_element_by_xpath("//button[@data-qa='join-login-button']")
login.click()

try:
    email = driver.find_element_by_xpath("//input[@placeholder='ที่อยู่อีเมล']")
except:
    driver.quit()
    print("Could not login")
else:
    email.click()
    for character in emailIn:
        email.send_keys(character)
        print(character)
        time.sleep(random.uniform(0,0.000001))
# email.send_keys("nikeprofil4@gmail.com")

# time.sleep(1)

password = driver.find_element_by_xpath("//input[@placeholder='รหัสผ่าน']")
password.click()
for char in passwordIn:
    password.send_keys(char)
    print(char)
    time.sleep(random.uniform(0,0.000001))
# password.send_keys("ItsPoom123")

# time.sleep(1)

login = driver.find_element_by_xpath("//input[@value='ลงชื่อเข้าใช้']").submit()

driver.implicitly_wait(5)

# #Select size from input
if sizeIn == "EU 39":
    #size41 = driver.find_element_by_xpath("//button[contains(text(),'EU 41')]").tag_name
    #print(size41)
    #driver.execute_script("arguments[0].click();", size41)
    #driver.implicitly_wait(3)
    #driver.find_element_by_xpath("//button[contains(text(),'EU 41')]").click()
    try:
        size41But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 39")]')))
    except:
        driver.quit()
        print("Could not select size")
    else:
        size41But.click()
elif sizeIn == "EU 42":
    #driver.find_element_by_xpath("//*[contains(text(),'EU 42')]").click()
    size42But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 42")]')))
    size42But.click()
elif sizeIn == "EU 42.5":
    #driver.find_element_by_xpath("//*[contains(text(),'EU 42.5')]").click()
    size425But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 42.5")]')))
    size425But.click()
elif sizeIn == "EU 43":
    #driver.find_element_by_xpath("//*[contains(text(),'EU 43')]").click()
    size43But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 43")]')))
    size43But.click()

#Confirms size and proceed to checkout
#confirmSizeButton = driver.find_element_by_xpath("//button[@data-qa='feed-buy-cta']")

try:
    confirmSizeButton = driver.find_element_by_xpath("//button[@data-qa='feed-buy-cta']")
    #confirmSizeButton = driver.find_element_by_xpath("//button[@data-qa='add-to-cart']")
except:
    driver.quit()
    print("Could not checkout size")
else:
    confirmSizeButton.click()

expandButton = driver.find_elements_by_xpath("//div[@class='expand-collapse']")
expandButton[1].click()

try:
    expandButton = WebDriverWait(driver, 10).until(EC.elements_to_be_clickable((By.XPATH, "//div[@class='expand-collapse']")))
except:

else:
    expandButton[1].click()



#=== Card details ===#
#Card no
cardNoInput = driver.find_element_by_xpath("//input[@id='cardNumber-input'")
cardNoInput.click()
for cardNoChar in cardNoValue:
    cardNoInput.send_keys(cardNoChar)
    time.sleep(random.uniform(0,0.0001))

#Exp date
expDateInput = driver.find_element_by_xpath("//input[@id='cardExpiry-input']")
expDateInput.click()
for expDateChar in cardExpDates:
    expDateInput.send_keys(expDateChar)
    time.sleep(random.uniform(0,0.0001))

#CVV
CVVInput = driver.find_element_by_xpath("//input[@id='cardCvc-input']")
CVVInput.click()
for CVVChar in CVVValue:
    CVVInput.send_keys(CVVChar)
    time.sleep(random.uniform(0,0.0001))

confirmCardBtn = driver.find_element_by_xpath("//button[contains(text(),'ดำเนินการต่อ')]")
confirmCardBtn.submit()

#=== Confirm checkout ===#

confirmCheckoutBtn = driver.find_element_by_xpath("//button[contains(text(),'ส่งคำสั่งซื้อ')]")
confirmCheckoutBtn.click()

#=== Checkout ===#