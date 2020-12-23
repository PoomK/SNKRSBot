from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

id = 1
arr1 = []
arr2 = []
arr3 = []

check = True

while check == True:
    userStop = input("Continue?")
    if userStop == "n":
        check = False
        break
    elif userStop == "y":
        linkInput = input("Input link:")
        arrayNo = (int(id))%3
        if arrayNo == 1:
            arr1.append(linkInput)
        if arrayNo == 2:
            arr2.append(linkInput)
        if arrayNo == 0:
            arr3.append(linkInput)
        id = id + 1

print("Tasks has ended")
print(arr1)
print(arr2)
print(arr3)

startTask = input("Start?")

if startTask == "y":

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver1 = webdriver.Chrome(PATH)
    driver2 = webdriver.Chrome(PATH)
    driver3 = webdriver.Chrome(PATH)

    for i in range(len(arr1)):
        driver1.get(arr1[i])

        try:
            time.sleep(15)
            menu = WebDriverWait(driver1, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='เมนู']")))
        except:
            driver1.quit()
        else:
            menu.click()

        driver2.get(arr1[i])

        try:
            time.sleep(15)
            menu = WebDriverWait(driver2, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='เมนู']")))
        except:
            driver2.quit()
        else:
            menu.click()

        driver3.get(arr1[i])

        try:
            time.sleep(15)
            menu = WebDriverWait(driver3, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='เมนู']")))
        except:
            driver3.quit()
        else:
            menu.click()