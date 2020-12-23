# This Python file uses the following encoding: utf-8
import os, sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font
import tkinter.messagebox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from time import strftime

#Set up window
root = tk.Tk()
root.title("SNKRS Bot")
root.geometry("1000x600")

#Set up tabs
tabControl = ttk.Notebook(root)
Home = ttk.Frame(tabControl)
taskDisplay = ttk.Frame(tabControl)
addTask = ttk.Frame(tabControl)
tabControl.add(Home, text="Home")
tabControl.add(taskDisplay, text="Tasks")
tabControl.add(addTask, text="Add Task")
tabControl.pack(expand=1, fill="both")

#Header
header = Label(Home, text="SNKRS Bot", font=("helvetica", 30, "bold"))
header.pack()

#Clock
def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200, tick)
clock = Label(Home, font=("times", 20, "bold"))
clock.pack()
tick()

#Scroll bar
# scrollbar = Scrollbar(taskDisplay)
# scrollbar.pack(side=RIGHT, fill=Y)

#Enter task no.
taskNoHead = Label(addTask, text="Task No. :")
taskNoHead.pack()
taskNoInput = Entry(addTask, textvariable="", width='20')
taskNoInput.pack()

#Enter link
linkHead = Label(addTask, text="Link:")
linkHead.pack()
linkInput = Entry(addTask, textvariable="", width='60')
linkInput.pack()

#Enter email
emailHead = Label(addTask, text="Email:")
emailHead.pack()
emailInput = Entry(addTask, textvariable="", width='60')
emailInput.pack()

#Enter password
PasswordHead = Label(addTask, text="Password:")
PasswordHead.pack()
passwordInput = Entry(addTask, textvariable="", width=60)
passwordInput.pack()

#Enter size
sizeHead = Label(addTask, text="Size:")
sizeHead.pack()
sizeChoice = ttk.Combobox(addTask, textvariable="")
sizeChoice['values']=('EU 41', 'EU 42', 'EU 42.5', 'EU 43')
sizeChoice.pack()

#Press button to see size chart
def showSizeCompare():
    tkinter.messagebox.showinfo("Size comparison", " EU41    = 8us \n EU42    = 8.5us \n EU42.5 = 9us \n EU43    = 9.5us")
button = tk.Button(addTask, text="Check sizes", command=showSizeCompare, pady=5, padx=5)
button.pack(pady=10)

taskNoList = []
linkList = []
emailList = []
passwordList = []
sizeList = []

startButtonIcon = PhotoImage(file = r"C:/Users/User\Desktop/Hype-Bot/Images/DiscordIcon.png")

def createTask():

    #Create variables for inputs
    taskNoInput1 = taskNoInput.get()
    linkInput1 = linkInput.get()
    emailInput1 = emailInput.get()
    passwordInput1 = passwordInput.get()
    sizeInput1 = sizeChoice.get()

    #Append to lists
    taskNoList.append(taskNoInput1)
    linkList.append(linkInput1)
    emailList.append(emailInput1)
    passwordList.append(passwordInput1)
    sizeList.append(sizeInput1)

    print("--------------------")
    print("Tasks: " + str(taskNoList))
    print("Links: " + str(linkList))
    print("Emails: " + str(emailList))
    print("Passwords: " + str(passwordList))
    print("Sizes: " + str(sizeList))

    #Clear inputs
    taskNoInput.delete(0, END)
    emailInput.delete(0, END)
    passwordInput.delete(0, END)

    #Commands for each task
    def startTask():
        #Setup drivers
        #Path to chromedriver for windows
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        #Path to chromedriver on mac
        #PATH = "/applications/chromedriver"
        driver = webdriver.Chrome(PATH)

        sizeIn = sizeChoice.get()

        #Set window size for mac
        # driver.set_window_size(500, 1080)

        #Open the website from user input
        driver.get(linkInput1)

        #Log in into nike website
        menu = driver.find_element_by_xpath("//button[@aria-label='เมนู']")
        driver.implicitly_wait(1)
        menu.click()
        login = driver.find_element_by_xpath("//button[@data-qa='join-login-button']")
        #login = driver.find_element_by_xpath("//button[@class='join-log-in text-color-grey prl3-sm pt2-sm pb2-sm fs12-sm d-sm-b']")
        login.click()
        email = driver.find_element_by_xpath("//input[@placeholder='ที่อยู่อีเมล']")
        email.send_keys(emailInput1)
        password = driver.find_element_by_xpath("//input[@placeholder='รหัสผ่าน']")
        password.send_keys(passwordInput1)
        login = driver.find_element_by_xpath("//input[@value='ลงชื่อเข้าใช้']").click()
    def stopTask():
        print("Task stopped")
    def deleteTask():
        print("Task deleted")

    #Display in task tab
    taskNo123 = Label(taskDisplay, text=taskNoInput1).pack()
    Link123 = Label(taskDisplay, text=linkInput1).pack()
    Email123 = Label(taskDisplay, text=emailInput1).pack()
    Pass123 = Label(taskDisplay, text=passwordInput1).pack()
    Size123 = Label(taskDisplay, text=sizeInput1).pack()

    #Display actions for each task
    startButton = tk.Button(taskDisplay, text="start", image = startButtonIcon, compound = LEFT, command=startTask).pack()
    stopButton = tk.Button(taskDisplay, text="stop", command=stopTask).pack()
    deleteButton = tk.Button(taskDisplay, text="delete", command=deleteTask).pack()

#Create task
create = tk.Button(addTask, text="Create task", command=createTask)
create.pack()

#Start all button
def startAll():
    for index in range(len(taskNoList)):
        #Setup drivers
        #Path to chromedriver for windows
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        #Path to chromedriver on mac
        #PATH = "/applications/chromedriver"
        driver = webdriver.Chrome(PATH)

        sizeIn = sizeChoice.get()

        #Set window size for mac
        # driver.set_window_size(500, 1080)

        #Open the website from user input
        driver.get(linkList[index])

        #Log in into nike website
        menu = driver.find_element_by_xpath("//button[@aria-label='เมนู']")
        driver.implicitly_wait(1)
        menu.click()
        login = driver.find_element_by_xpath("//button[@data-qa='join-login-button']")
        #login = driver.find_element_by_xpath("//button[@class='join-log-in text-color-grey prl3-sm pt2-sm pb2-sm fs12-sm d-sm-b']")
        login.click()
        driver.implicitly_wait(1)
        email = driver.find_element_by_xpath("//input[@placeholder='ที่อยู่อีเมล']")
        email.send_keys(emailList[index])
        driver.implicitly_wait(1)
        password = driver.find_element_by_xpath("//input[@placeholder='รหัสผ่าน']")
        password.send_keys(passwordList[index])
        driver.implicitly_wait(1)
        login = driver.find_element_by_xpath("//input[@value='ลงชื่อเข้าใช้']").click()
startAllButton = tk.Button(taskDisplay, text="Start all", command=startAll).pack()

#Stop all button - Does not work at the moment because it will make the software crash
# def stopAll(driver):
#     driver.quit()
# stopAllButton = tk.Button(taskDisplay, text="Stop all", command=stopAll).pack()

def task():
    #Setup drivers
    #Path to chromedriver for windows
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    #Path to chromedriver on mac
    #PATH = "/applications/chromedriver"
    driver = webdriver.Chrome(PATH)

    sizeIn = sizeChoice.get()

    #Set window size for mac
    #driver.set_window_size(900, 1080)

    #Open the website from user input
    driver.get(linkInput.get())

    #Log in into nike website
    menu = driver.find_element_by_xpath("//button[@aria-label='เมนู']")
    driver.implicitly_wait(1)
    menu.click()
    login = driver.find_element_by_xpath("//button[@data-qa='join-login-button']")
    #login = driver.find_element_by_xpath("//button[@class='join-log-in text-color-grey prl3-sm pt2-sm pb2-sm fs12-sm d-sm-b']")
    login.click()
    email = driver.find_element_by_xpath("//input[@placeholder='ที่อยู่อีเมล']")
    email.send_keys(emailInput.get())
    password = driver.find_element_by_xpath("//input[@placeholder='รหัสผ่าน']")
    password.send_keys(passwordInput.get())
    login = driver.find_element_by_xpath("//input[@value='ลงชื่อเข้าใช้']").click()

    #Select size from input
    if sizeIn == "EU 41":
        #size41 = driver.find_element_by_xpath("//button[contains(text(),'EU 41')]").tag_name
        #print(size41)
        #driver.execute_script("arguments[0].click();", size41)
        #driver.implicitly_wait(3)
        #driver.find_element_by_xpath("//button[contains(text(),'EU 41')]").click()
        size41But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 41")]')))
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

root.mainloop()