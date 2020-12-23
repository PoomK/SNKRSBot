import os, sys
import tkinter as tk
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import random
import discord

class Sneaker:
    def __init__(self, root):
        self.root=root
        self.root.title("SNKRS Bot")
        self.root.geometry("1300x845")
        self.root.configure(bg = 'black')
        self.root.resizable(width=0, height=0)

#======= Styles =======#
        style = ttk.Style()

        style.theme_create( "HypeBot", parent="alt", settings={
                "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
                "TNotebook.Tab": {
                    "configure": {"padding": [116, 1], "background": 'gray24', "foreground": 'red'},
                    "map":       {"background": [("selected", 'black')],
                                "expand": [("selected", [1, 1, 1, 0])] } } } )

        style.theme_use("HypeBot")

        style.configure('TNotebook.Tab', font=('URW Gothic L', '20','bold'))
        style.configure('TNotebook', background='black')
        style.configure('TFrame', background='black')
        style.configure("Treeview.Heading", background='gray24', foreground='white', font=('URW Gothic L', '13', 'bold'))
        style.configure("Treeview", background='gray90', font=('URW Gothic L', '10', 'normal') )

#======= Tabs =======#
        tabControl = ttk.Notebook(root)
        TasksTab = ttk.Frame(tabControl)
        ProfilesTab = ttk.Frame(tabControl)
        ProxiesTab = ttk.Frame(tabControl)
        SettingsTab = ttk.Frame(tabControl)
        tabControl.add(TasksTab, text="Tasks")
        tabControl.add(ProfilesTab, text="Profile")
        tabControl.add(ProxiesTab, text="Proxy")
        tabControl.add(SettingsTab, text="Settings")
        tabControl.pack(expand=1, fill="both")

        TitleBarFrame = Frame(root, bd=1, bg='black')
        TitleBarFrame.place(x=0, y=40, width=1300, height=75)

        lbl_TaskTabTitle = Label(TitleBarFrame, text="SNKRS Bot", font=('FixedSYS', '50','bold'), fg='deep sky blue', bg='Black')
        lbl_TaskTabTitle.grid(row=1, column=1, padx=5)

#======= Images =======#
        startButtonIcon = PhotoImage(file = r"C:/Users/User\Desktop/Hype-Bot/Images/PlayButton.png")
        checkIcon = PhotoImage(file = r"C:/Users/User\Desktop/Hype-Bot/Images/CheckIcon.png")
        crossIcon = PhotoImage(file = r"C:/Users/User\Desktop/Hype-Bot/Images/CrossIcon.png")
        DiscordLogo = PhotoImage(file = r"C:/Users/User\Desktop/Hype-Bot/Images/DiscordIcon.png")

#======= Tasks =======#

    #======= Task Arrays =======#
        taskNameArray = []
        siteNameArray = []
        linkArray = []
        sizeChoiceArray = []
        proxyArray = []
        profileArray = []

    #======= Task Variables =======#
        self.taskNameVar = StringVar()
        self.siteNameVar = StringVar()
        self.linkVar = StringVar()
        self.sizeChoiceVar = StringVar()
        self.proxyVar = StringVar()
        self.profileVar = StringVar()
        self.taskQuantityVar = StringVar()

    #===== Task Frames =====#

        #Frame for inputs, create task, logging
        CreateActionTaskFrame = Frame(TasksTab, bd=1, bg='black')
        CreateActionTaskFrame.place(x=0, y=75, width=375, height=725)

        btnFrame = Frame(CreateActionTaskFrame, bd=1, bg="black")
        btnFrame.place(x=0, y=275, width=400, height=50)

        loggingTitleFrame = Frame(CreateActionTaskFrame, bd=1, bg="black")
        loggingTitleFrame.place(x=0, y=325, width=320, height=45)

        loggingFrame = Frame(CreateActionTaskFrame, bd=1, bg="black")
        loggingFrame.place(x=10, y=360, width=350, height=355)

        #Frame for treeview and Start task actions
        DisplayTaskFrame = Frame(TasksTab, bd=1, bg='black')
        DisplayTaskFrame.place(x=370, y=75, width=980, height=725)

        TaskTableFrame = Frame(DisplayTaskFrame, bg="black")
        TaskTableFrame.place(x=7, y=10, width=910, height=645)

        TaskButtonActionFrame = Frame(DisplayTaskFrame, bg="black")
        TaskButtonActionFrame.place(x=7, y=670, width=910, height=50)

    #===== Task input =====#
        createTaskTitle = Label(CreateActionTaskFrame, text="Create task", font=("URW Gothic L", 20, "bold"), fg='red', bg="black")
        createTaskTitle.grid(row=0, columnspan=2)

        lbl_taskName = Label(CreateActionTaskFrame, text="Task Name", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_taskName.grid(row=1, column=0, pady=2, padx=10, sticky="W")
        entry_taskName = Entry(CreateActionTaskFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=21)
        entry_taskName.grid(row=1, column=1, pady=2, padx=10, sticky="w")

        lbl_siteName = Label(CreateActionTaskFrame, text="Site Name", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_siteName.grid(row=2, column=0, pady=2, padx=10, sticky="W")
        combo_siteName = ttk.Combobox(CreateActionTaskFrame, font=("URW Gothic L", 12, "normal"), width=15)
        combo_siteName['values']=('Nike_TH')
        combo_siteName.grid(row=2, column=1, pady=2, padx=10, sticky="w")

        lbl_link = Label(CreateActionTaskFrame, text="Link", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_link.grid(row=3, column=0, pady=2, padx=10, sticky="w")
        entry_link = Entry(CreateActionTaskFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=21)
        entry_link.grid(row=3, column=1, pady=2, padx=10)

        lbl_sizeChoice = Label(CreateActionTaskFrame, text="Size", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_sizeChoice.grid(row=4, column=0, pady=2, padx=10, sticky="w")
        combo_sizeChoice = ttk.Combobox(CreateActionTaskFrame, font=("URW Gothic L", 12, "normal"), textvariable="", width=10)
        combo_sizeChoice['values']=('EU 37.5','EU 38', 'EU 38.5', 'EU 39','EU 40', 'EU 40.5', 'EU 41', 'EU 42', 'EU 42.5', 'EU 43', 'EU 44')
        combo_sizeChoice.grid(row=4, column=1, pady=2, padx=10, sticky="w")

        lbl_proxy = Label(CreateActionTaskFrame, text="Proxy", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_proxy.grid(row=5, column=0, pady=2, padx=10, sticky="w")
        #Need to add tab for user to enter profiles to save to file
        combo_proxy = ttk.Combobox(CreateActionTaskFrame, font=("URW Gothic L", 12, "normal"), textvariable="", width=10)
        combo_proxy['values']=('none','proxy1')
        combo_proxy.grid(row=5, column=1, pady=2, padx=10, sticky="w")

        lbl_profile = Label(CreateActionTaskFrame, text="Profile", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_profile.grid(row=6, column=0, pady=2, padx=10, sticky="w")
        entry_profile = Entry(CreateActionTaskFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=21)
        entry_profile.grid(row=6, column=1, pady=2, padx=10, sticky="w")
        #Need to add tab for user to enter profiles to save to file
        # combo_profile = ttk.Combobox(CreateActionTaskFrame, font=("URW Gothic L", 12, "normal"), textvariable="", width=10)
        # #combo_profile['values']=(profileArray)
        # # combo_profile['values']=('Profile1', 'Profile2', 'Profile3', 'Profile4')
        # combo_profile.grid(row=6, column=1, pady=2, padx=10, sticky="w")

        lbl_taskQuantity = Label(CreateActionTaskFrame, text="Task Quantity", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_taskQuantity.grid(row=7, column=0, pady=2, padx=10, sticky="W")
        entry_taskQuantity = Entry(CreateActionTaskFrame, textvariable="", font=("URW Gothic L", 12, "normal"), fg='black', width=21)
        entry_taskQuantity.grid(row=7, column=1, pady=2, padx=10, sticky="w")
    
    #===== Check buttons =====#

        # checkButtonAddressVar = IntVar()

        # checkbtn_savedAddress = Checkbutton(
        #     checkButtonFrame, text="Saved address", variable=checkButtonAddressVar, bg="black", activebackground="black", activeforeground="red", fg="red", font=("URW Gothic L", 15, "bold")
        # )
        # checkbtn_savedAddress.grid(row=1, column=1)

    #===== Task Logging =====#
        loggingTitle = Label(loggingTitleFrame, text="Log", font=('URW Gothic L', '20','bold'), fg='Red', bg='black')
        loggingTitle.grid(row=0, column=0, padx=7)

        scroll_y = Scrollbar(loggingFrame, orient=VERTICAL)
        logging_table = ttk.Treeview(loggingFrame, columns=("Action"), yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=logging_table.yview)

        logging_table.heading("Action", text="Log")
        logging_table['show']='headings'
        logging_table.column("Action")
        logging_table.pack(fill=BOTH, expand=1)

    #===== Bot initiate time =====#
        bot_start_now = datetime.now()
        bot_start_time = bot_start_now.strftime("[%H:%M:%S]")
        logging_table.insert('', 'end', values=[bot_start_time + " - Bot initiated"])

    #===== Task table =====#

        scroll_y = Scrollbar(TaskTableFrame, orient=VERTICAL, troughcolor='black')
        task_table = ttk.Treeview(TaskTableFrame, columns=("ID", "SiteName", "TaskName", "Profile", "Link", "Size", "Proxy"), yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=task_table.yview)

        #Treeview headings
        task_table.heading("ID", text="ID")
        task_table.heading("SiteName", text="Site")
        task_table.heading("TaskName", text="Task name")
        task_table.heading("Profile", text="Profile")
        task_table.heading("Link", text="Link")
        task_table.heading("Size", text="Size")
        task_table.heading("Proxy", text="Proxy")
        task_table['show']='headings'

        #Treeview columns
        task_table.column("ID", width=30, anchor='center')
        task_table.column("SiteName", width=90, anchor='center')
        task_table.column("TaskName", width=90, anchor='center')
        task_table.column("Profile", width=100, anchor='center')
        task_table.column("Link", width=325, anchor='center')
        task_table.column("Size", width=60, anchor='center')
        task_table.column("Proxy", width=90, anchor='center')
        task_table.pack(fill=BOTH, expand=1, anchor='center')

    #===== Create task frame Buttons =====#
        self.i=1

        def CreateTaskCommand():
            CreateTaskConfirmMsgBox = tkinter.messagebox.askquestion("Create task", "Are you sure all entry is correct?")

            if CreateTaskConfirmMsgBox == "yes":
                # print("Task created")

                #Returns user the value of amount of tasks user wants to create
                taskQuantityVar = int(entry_taskQuantity.get())

                for b in range(taskQuantityVar):
                    taskNameVar = entry_taskName.get()
                    siteNameVar = combo_siteName.get()
                    linkVar = entry_link.get()
                    sizeVar = combo_sizeChoice.get()
                    proxyVar = combo_proxy.get()
                    profileVar = entry_profile.get()

                    taskNameArray.append(taskNameVar)
                    siteNameArray.append(siteNameVar)
                    linkArray.append(linkVar)
                    sizeChoiceArray.append(sizeVar)
                    proxyArray.append(proxyVar)
                    profileArray.append(profileVar)

                    # print("#==========#")
                    # print(taskNameArray)
                    # print(siteNameArray)
                    # print(linkArray)
                    # print(sizeChoiceArray)
                    # print(proxyArray)
                    # print(profileArray)
                    # print(savedAddressCheckArray)

                    task_table.insert('', 'end', values=(self.i, siteNameVar, taskNameVar, profileVar, linkVar, sizeVar, proxyVar))

                    task_create_now = datetime.now()
                    task_create_time = task_create_now.strftime("[%H:%M:%S]")

                    logging_table.insert('', 'end', values=[task_create_time + " - Task " + str(self.i) + " created"])

                    self.i = self.i + 1

        createTaskBtn = Button(btnFrame, text="Create", command=CreateTaskCommand, font=('URW Gothic L', '10','bold'), bg="IndianRed2", activebackground="IndianRed1", width=9, height=2)
        createTaskBtn.grid(row=0, column=0, padx=10)

    #===== Task action frame (start, clear)=====#
    
        def startAllTask():

            task_start_now = datetime.now()
            task_start_time = task_start_now.strftime("[%H:%M:%S]")
            logging_table.insert('', 'end', values=[task_start_time + " - Tasks completed "])

            for index in range(len(taskNameArray)):

                # task_start_now = datetime.now()
                # task_start_time = task_start_now.strftime("[%H:%M:%S]")
                # taskid = index+1
                # logging_table.insert('', 'end', values=[task_start_time + " - Task " + taskid + " started"])
                
            #=== Set up chromedriver ===#
                PATH = "C:\Program Files (x86)\chromedriver.exe"
                driver = webdriver.Chrome(PATH)

            #=== Create profile index to retrieve profile info ===#
                profileIndex = profieNameArray.index(profileArray[index])

            #=== Get details ===#
                emailInValue = emailArray[profileIndex]
                passwordInValue = passwordArray[profileIndex]

                sizeInValue = sizeChoiceArray[index]

                cardNoValue = cardNoArray[profileIndex]
                expMonthValue = expMonthArray[profileIndex]
                expYearValue = expYearArray[profileIndex]
                cardExpDates = expMonthValue + expYearValue
                CVVValue = CVVArray[profileIndex]
                
                savedAddressYesNo = savedAddressCheckArray[profileIndex]
                firstNameValue = firstNameArray[profileIndex]
                lastNameValue = lastNameArray[profileIndex]
                address1Value = address1Array[profileIndex]
                address2Value = address2Array[profileIndex]
                cityValue = cityArray[profileIndex]
                zipCodeValue = zipCodeArray[profileIndex]
                provinceValue = provinceArray[profileIndex]
                countryValue = countryArray[profileIndex]
                phoneNoValue = phoneNoArray[profileIndex]

            #=== Get link ===#
                driver.get(linkArray[index])
                time.sleep(3)

            #=== Log in into nike website ===#
                menu = driver.find_element_by_xpath("//button[@aria-label='เมนู']")
                driver.implicitly_wait(3)
                menu.click()
                loginInput = driver.find_element_by_xpath("//button[@data-qa='join-login-button']")
                loginInput.click()
                emailInput = driver.find_element_by_xpath("//input[@placeholder='ที่อยู่อีเมล']")
                emailInput.click()
                for character in emailInValue:
                    emailInput.send_keys(character)
                    #print(character)
                    time.sleep(random.uniform(0,0.0001))
                passwordInput = driver.find_element_by_xpath("//input[@placeholder='รหัสผ่าน']")
                passwordInput.click()
                for char in passwordInValue:
                    passwordInput.send_keys(char)
                    # print(char)
                    time.sleep(random.uniform(0,0.0001))
                login = driver.find_element_by_xpath("//input[@value='ลงชื่อเข้าใช้']").submit()

                time.sleep(1)

            #=== Select sizes ===#
                driver.implicitly_wait(5)
                if sizeInValue == "EU 37.5":
                    size375But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 37.5")]')))
                    size375But.click()
                elif sizeInValue == "EU 38":
                    size38But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 38")]')))
                    size38But.click()
                elif sizeInValue == "EU 38.5":
                    size385But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 38.5")]')))
                    size385But.click()
                elif sizeInValue == "EU 39":
                    size39But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 39")]')))
                    size39But.click()
                elif sizeInValue == "EU 40":
                    size40But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 40")]')))
                    size40But.click()
                elif sizeInValue == "EU 40.5":
                    size405But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 40.5")]')))
                    size405But.click()
                elif sizeInValue == "EU 41":
                    size41But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 41")]')))
                    size41But.click()
                elif sizeInValue == "EU 42":
                    size42But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 42")]')))
                    size42But.click()
                elif sizeInValue == "EU 42.5":
                    size425But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 42.5")]')))
                    size425But.click()
                elif sizeInValue == "EU 43":
                    size43But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 43")]')))
                    size43But.click()
                elif sizeInValue == "EU 44":
                    size44But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 44")]')))
                    size44But.click()

            #=== Confirms size and proceed to checkout ===#
                time.sleep(0.5)
                #confirmSizeButton = driver.find_element_by_xpath("//button[@data-qa='feed-buy-cta']")
                confirmSizeButton = driver.find_element_by_xpath("//button[@data-qa='add-to-cart']")
                confirmSizeButton.click()

            #=== X click on all expand buttons ===#

                # expandButtons = driver.find_elements_by_xpath("//div[@class='expand-collapse']")
                # expandButtons[1].click()

                # for buttonExpand in expandButtons:
                #     expandButtons.click()
            
            #=== Address ===#  
                if savedAddressYesNo == "1":
                    print("saved")
                elif savedAddressYesNo == "0":
                    print("Not saved")

                    newAddressBtn = driver.find_element_by_xpath("//div[contains(text(),'เพิ่มที่อยู่ฬหม่')]")
                    newAddressBtn.click()

                    #First name
                    addressFirstNameInput = driver.find_element_by_xpath("//input[@id='firstName']")
                    addressFirstNameInput.click()
                    for firstNameChar in firstNameValue:
                        addressFirstNameInput.send_keys(firstNameChar)
                        time.sleep(random.uniform(0,0.0001))

                    #Last name
                    addressLastNameInput = driver.find_element_by_xpath("//input[@id='lastName']")
                    addressLastNameInput.click()
                    for lastNameChar in lastNameValue:
                        addressLastNameInput.send_keys(lastNameChar)
                        time.sleep(random.uniform(0,0.0001))

                    #Address line 1
                    addressAddressLine1Input = driver.find_element_by_xpath("//input[@id='addressLine1']")
                    addressAddressLine1Input.click()
                    for addressLine1Char in address1Value:
                        addressAddressLine1Input.send_keys(addressLine1Char)
                        time.sleep(random.uniform(0,0.0001))

                    #Address line 2 (add city to address line 2)
                    addressAddressLine2Input = driver.find_element_by_xpath("//input[@id='addressLine2']")
                    addressAddressLine2Input.click()
                    for addressLine2Char in address2Value:
                        addressAddressLine2Input.send_keys(addressLine2Char)
                        time.sleep(random.uniform(0,0.0001))

                    #City (เขต)
                    addressCityInput = driver.find_element_by_xpath("//input[@id='district']")
                    addressCityInput.click()
                    for addressCityChar in cityValue:
                        addressCityInput.send_keys(addressCityChar)
                        time.sleep(random.uniform(0,0.0001))

                    #Province (Have to select, try typing)
                    addressProvinceSelect = driver.find_element_by_xpath("//select[@id='province']")

                    #Zipcode
                    addressZipCodeInput = driver.find_element_by_xpath("//input[@id='postCode']")
                    addressZipCodeInput.click()
                    for addressZipCodeChar in zipCodeValue:
                        addressZipCodeInput.send_keys(addressZipCodeChar)
                        time.sleep(random.uniform(0,0.0001))

                    #Phone number (Maybe have to remove the zero)
                    addressPhoneNumberInput = driver.find_element_by_xpath("//input[@placeholder='หมายเลขโทรศัพท์']")
                    addressPhoneNumberInput.click()
                    #need to remove the zero

                    #Email
                    addressEmailInput = driver.find_element_by_xpath("//input[@placeholder='อีเมล']")
                    addressEmailInput.click()
                    for addressEmailChar in emailInValue:
                        addressEmailInput.send_keys(addressEmailChar)
                        time.sleep(random.uniform(0,0.0001))

                    #Confirm address
                    confirmAddressButton = driver.find_element_by_xpath("//button[contains(text(),'บันทึกและดำเนินการต่อ')]")
                    confirmAddressButton.click()
 
            #=== Card details ===#
                # expandButtons[1].click()

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

            #=== Wait in queue ===#

        StartAllTaskBtn = Button(TaskButtonActionFrame, text="Start all", command = startAllTask, font=('URW Gothic L', '10','bold'), bg="IndianRed2", activebackground="IndianRed1", width=20, height=2)
        StartAllTaskBtn.grid(row=0, column=0, padx=0)

        # def startTask():
        #     print("Task started")

        # StartTaskBtn = Button(TaskButtonActionFrame, text="Start", command = startTask, font=('URW Gothic L', '10','bold'), bg="IndianRed2", activebackground="IndianRed1", width=20, height=2)
        # StartTaskBtn.grid(row=0, column=1, padx=24)

        def ClearTaskCommand():
            #Message box to confirm is user really wants to delete tasks
            clearTaskMsgBox = tkinter.messagebox.askquestion("Confirm","Are you sure you want to delete all tasks?")

            if clearTaskMsgBox == 'yes':

                #===== clear task time =====#
                clear_tasks_now = datetime.now()
                clear_tasks_time = clear_tasks_now.strftime("[%H:%M:%S]")
                logging_table.insert('', 'end', values=[clear_tasks_time + " - Tasks cleared"])

                #Removes all elements in array
                del taskNameArray[:]
                del siteNameArray[:]
                del linkArray[:]
                del sizeChoiceArray[:]
                del proxyArray[:]
                del profileArray[:]

                for a in task_table.get_children():
                    task_table.delete(a)
                self.i = 1

        clearTaskBtn = Button(TaskButtonActionFrame, text="Clear", command=ClearTaskCommand, font=('URW Gothic L', '10','bold'), bg="IndianRed2", activebackground="IndianRed1", width=20, height=2)
        clearTaskBtn.grid(row=0, column=3, padx=24)

#======= Profiles =======#

    #======= Main profile frames =======#
        CreateProfileFrame = Frame(ProfilesTab, bd=1, bg="black")
        CreateProfileFrame.place(x=0, y=75, width=1300, height=400)

        DisplayProfileFrame = Frame(ProfilesTab,bg="black")
        DisplayProfileFrame.place(x=10, y=435, width=1280, height=355)

    #======= Profile Arrays =======#
        profieNameArray = []
        emailArray = []
        passwordArray = []
        cardNoArray = []
        expMonthArray = []
        expYearArray = []
        CVVArray = []
        firstNameArray = []
        lastNameArray = []
        address1Array = []
        address2Array = []
        cityArray = []
        zipCodeArray = []
        provinceArray = []
        countryArray = []
        phoneNoArray = []
        savedAddressCheckArray = []

    #======= Profile Variables =======#
        profileNameVar = StringVar()
        emailVar = StringVar()
        passwordVar = StringVar()
        cardNoVar = StringVar()
        expMonthVar = StringVar()
        expYearVar = StringVar()
        CVVVar = StringVar()
        firstNameVar = StringVar()
        lastNameVar = StringVar()
        address1Var = StringVar()
        address2Var = StringVar()
        cityVar = StringVar()
        zipCodeVar = StringVar()
        provinceVar = StringVar()
        countryVar = StringVar()
        phoneNoVar = StringVar()

    #======= Smaller Frames =======#
        nameLogInFrame = Frame(CreateProfileFrame, bd=1, bg="black")
        nameLogInFrame.place(x=10, y=10, width=350, height=180)

        cardInfoFrame = Frame(CreateProfileFrame, bd=1, bg="black")
        cardInfoFrame.place(x=10, y=190, width=300, height=170)

        addressFrame = Frame(CreateProfileFrame, bd=1, bg="black")
        addressFrame.place(x=375, y=10, width=875, height=400)

        buttonFrame = Frame(CreateProfileFrame, bd=1, bg="black")
        buttonFrame.place(x=375, y=295, width=300, height=60)

        warningFrame = Frame(CreateProfileFrame, bg="black")
        warningFrame.place(x=700, y=295, width=500, height=60)

        profileDisTitle = Label(nameLogInFrame, text="Profile name", font=("URW Gothic L", 20, "bold"), fg='red', bg="black")
        profileDisTitle.grid(row=1, column=0, columnspan=2, pady=3, sticky='W')

        #Profile name
        lbl_profileName = Label(nameLogInFrame, text="Profile name", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_profileName.grid(row=2, column=0, sticky="W")
        entry_profileName = Entry(nameLogInFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=30)
        entry_profileName.grid(row=2, column=1, padx=10, sticky="w")

    #======= Log in details =======#
        logInTitle = Label(nameLogInFrame, text="Log-in details", font=("URW Gothic L", 20, "bold"), fg='red', bg="black")
        logInTitle.grid(row=3, column=0, columnspan=2, pady=3, sticky='W')

        #Email
        lbl_email = Label(nameLogInFrame, text="Email", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_email.grid(row=4, column=0, sticky="W")
        entry_email = Entry(nameLogInFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=30)
        entry_email.grid(row=4, column=1, padx=10, sticky="w")

        #Password
        lbl_password = Label(nameLogInFrame, text="Password", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_password.grid(row=5, column=0, sticky="W")
        entry_password = Entry(nameLogInFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=30)
        entry_password.grid(row=5, column=1, padx=10, sticky="w")

    #======= Shipping details =======#
        shippingTitle = Label(addressFrame, text="Shipping details", font=("URW Gothic L", 20, "bold"), fg='red', bg="black")
        shippingTitle.grid(row=1, column=0, columnspan=2, pady=2, padx=10, sticky='W')

        # #First name
        lbl_firstName = Label(addressFrame, text="First name", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_firstName.grid(row=2, column=0, pady=3, padx=10, sticky="W")
        entry_firstName = Entry(addressFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=21)
        entry_firstName.grid(row=2, column=1, pady=3, padx=10, sticky="w")

        # #Last name
        lbl_lastName = Label(addressFrame, text="Last name", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_lastName.grid(row=2, column=2, pady=5, padx=10, sticky="W")
        entry_lastName = Entry(addressFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=21)
        entry_lastName.grid(row=2, column=3, pady=5, padx=10, sticky="w")

        # #Address 1
        lbl_address1 = Label(addressFrame, text="Address 1", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_address1.grid(row=3, column=0, pady=3, padx=10, sticky="W")
        entry_address1 = Entry(addressFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=80)
        entry_address1.grid(row=3, column=1, columnspan=4, pady=3, padx=10, sticky="w")

        # #Address 2
        lbl_address2 = Label(addressFrame, text="Address 2", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_address2.grid(row=4, column=0, pady=5, padx=10, sticky="W")
        entry_address2 = Entry(addressFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=80)
        entry_address2.grid(row=4, column=1, columnspan=4, pady=5, padx=10, sticky="w")

        # #City
        lbl_city = Label(addressFrame, text="City", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_city.grid(row=5, column=0, pady=5, padx=10, sticky="W")
        entry_city = Entry(addressFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=21)
        entry_city.grid(row=5, column=1, pady=5, padx=10, sticky="w")

        # #Zipcode
        lbl_zipcode = Label(addressFrame, text="Zipcode", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_zipcode.grid(row=5, column=2, pady=5, padx=10, sticky="W")
        entry_zipcode = Entry(addressFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=21)
        entry_zipcode.grid(row=5, column=3, pady=5, padx=10, sticky="w")

        # #Province
        lbl_province = Label(addressFrame, text="Province", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_province.grid(row=6, column=0, pady=5, padx=10, sticky="W")
        combo_province = ttk.Combobox(addressFrame, width=18, font=("URW Gothic L", 12, "normal"))
        combo_province['values']=('Bangkok', 'Chiang mai', 'Chiang rai', 'Pattaya')
        combo_province.grid(row=6, column=1, pady=5, padx=10, sticky="w")

        # #Country
        lbl_country = Label(addressFrame, text="Country", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_country.grid(row=6, column=2, pady=5, padx=10, sticky="W")
        combo_country = ttk.Combobox(addressFrame, width=18, font=("URW Gothic L", 12, "normal"))
        combo_country['values']=('Thailand')
        combo_country.grid(row=6, column=3, pady=5, padx=10, sticky="w")

        # #Phone number
        lbl_phoneNumber = Label(addressFrame, text="Phone No.", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_phoneNumber.grid(row=7, column=0, pady=5, padx=10, sticky="W")
        entry_phoneNumber = Entry(addressFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=21)
        entry_phoneNumber.grid(row=7, column=1, pady=5, padx=10, sticky="w")

        #Check button
        checkButtonAddressVar = IntVar()

        checkbtn_savedAddress = Checkbutton(
            addressFrame, text="Saved address", variable=checkButtonAddressVar, bg="black", activebackground="black", activeforeground="red", fg="red", font=("URW Gothic L", 15, "bold")
        )
        checkbtn_savedAddress.grid(row=7, column=2)

    #======= Card details =======#
        shippingTitle = Label(cardInfoFrame, text="Card details", font=("URW Gothic L", 20, "bold"), fg='red', bg="black")
        shippingTitle.grid(row=1, column=0, columnspan=2, pady=2, sticky='W')

        lbl_cardNumber = Label(cardInfoFrame, text="Card No.", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_cardNumber.grid(row=2, column=0, sticky="W")
        entry_cardNumber = Entry(cardInfoFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=21)
        entry_cardNumber.grid(row=2, column=1, padx=10, sticky="w")

        lbl_expMonth = Label(cardInfoFrame, text="Exp. month", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_expMonth.grid(row=3, column=0, sticky="W")
        combo_expMonth = ttk.Combobox(cardInfoFrame, width=5, font=("URW Gothic L", 12, "normal"))
        combo_expMonth['values']=('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
        combo_expMonth.grid(row=3, column=1, padx=10, sticky="w")

        lbl_expYear = Label(cardInfoFrame, text="Exp. year", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_expYear.grid(row=4, column=0, sticky="W")
        combo_expYear = ttk.Combobox(cardInfoFrame, width=10, font=("URW Gothic L", 12, "normal"))
        combo_expYear['values']=('2021', '2022', '2023', '2024', '2025', '2026')
        combo_expYear.grid(row=4, column=1, padx=10, sticky="w")

        lbl_CVV = Label(cardInfoFrame, text="CVV", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_CVV.grid(row=5, column=0, sticky="W")
        entry_CVV = Entry(cardInfoFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=5)
        entry_CVV.grid(row=5, column=1, padx=10, sticky="w")

    #======= Table to display profiles =======#
        style = ttk.Style()

        scroll_x = Scrollbar(DisplayProfileFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(DisplayProfileFrame, orient=VERTICAL)
        profile_table = ttk.Treeview(DisplayProfileFrame, columns=("ProfileName", "Email", "Password", "CardNo", "ExpMonth", "ExpYear", "CVV", "SavedAddress", "FirstName", "LastName", "Address1", "Address2", "City", "ZipCode", "Province", "Country", "PhoneNo"), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=profile_table.xview)
        scroll_y.config(command=profile_table.yview)

        #Treeview headings
        profile_table.heading("ProfileName", text="Profile name")
        profile_table.heading("Email", text="Email")
        profile_table.heading("Password", text="Password")
        profile_table.heading("CardNo", text="Card no.")
        profile_table.heading("ExpMonth", text="Exp. month")
        profile_table.heading("ExpYear", text="Exp. year")
        profile_table.heading("CVV", text="CVV")
        profile_table.heading("SavedAddress", text="Saved")
        profile_table.heading("FirstName", text="First name")
        profile_table.heading("LastName", text="Last name")
        profile_table.heading("Address1", text="Address 1")
        profile_table.heading("Address2", text="Address 2")
        profile_table.heading("City", text="City")
        profile_table.heading("ZipCode", text="Zipcode")
        profile_table.heading("Province", text="Province")
        profile_table.heading("Country", text="Country")
        profile_table.heading("PhoneNo", text="Phone no.")
        profile_table['show']='headings'

        #Treeview columns
        profile_table.column("ProfileName", width=110, anchor='center')
        profile_table.column("Email", width=200, anchor='center')
        profile_table.column("Password", width=90, anchor='center')
        profile_table.column("CardNo", width=120, anchor='center')
        profile_table.column("ExpMonth", width=100, anchor='center')
        profile_table.column("ExpYear", width=90, anchor='center')
        profile_table.column("CVV", width=45, anchor='center')
        profile_table.column("SavedAddress", width=60, anchor='center')
        profile_table.column("FirstName", width=120, anchor='center')
        profile_table.column("LastName", width=120, anchor='center')
        profile_table.column("Address1", width=200, anchor='center')
        profile_table.column("Address2", width=150, anchor='center')
        profile_table.column("City", width=80, anchor='center')
        profile_table.column("ZipCode", width=70, anchor='center')
        profile_table.column("Province", width=80, anchor='center')
        profile_table.column("Country", width=80, anchor='center')
        profile_table.column("PhoneNo", width=100, anchor='center')
        profile_table.pack(fill=BOTH, expand=1)

    #======= Warning frame =======#
        lbl_exclamationMark = Label(warningFrame, text="!", font=("URW Gothic L", 35, "bold"), bg="black", fg="red")
        lbl_exclamationMark.grid(row=0, column=0, rowspan=2)

        lbl_warningMessage = Label(warningFrame, text="Please make sure you saved your address and verified your", font=("URW Gothic L", 13, "bold"), bg="black", fg="red")
        lbl_warningMessage.grid(row=0, column=1)

        lbl_warningMessage2 = Label(warningFrame, text="phone number in your accounts", font=("URW Gothic L", 13, "bold"), bg="black", fg="red")
        lbl_warningMessage2.grid(row=1, column=1, sticky="W")

    #======= Buttons to create and delete and update profile =======#

        #Create button

        def createProfileTask():
            #print("Profile created")

            #Makes sure user enters detail right
            CreateProfileConfirmMsgBox = tkinter.messagebox.askquestion("Create task", "Are you sure all entry is correct?")

            if CreateProfileConfirmMsgBox == "yes":

                #Gets all values
                profileNameVar = entry_profileName.get()
                emailVar = entry_email.get()
                passwordVar = entry_password.get()
                cardNoVar = entry_cardNumber.get()
                expMonthVar = combo_expMonth.get()
                expYearVar = combo_expYear.get()
                CVVVar = entry_CVV.get()
                firstNameVar = entry_firstName.get()
                lastNameVar = entry_lastName.get()
                address1Var = entry_address1.get()
                address2Var = entry_address2.get()
                cityVar = entry_city.get()
                zipCodeVar = entry_zipcode.get()
                provinceVar = combo_province.get()
                countryVar = combo_country.get()
                phoneNoVar = entry_phoneNumber.get()
                savedAddressCheckVar = checkButtonAddressVar.get()

                #Writes values to csv file
                with open('profiles.csv', 'a') as csvfile:
                    writer = csv.writer(csvfile, lineterminator = '\r')
                    writer.writerow([profileNameVar, emailVar, passwordVar, cardNoVar, expMonthVar, expYearVar, CVVVar, firstNameVar, lastNameVar, address1Var, address2Var, cityVar, zipCodeVar, provinceVar, countryVar, phoneNoVar, savedAddressCheckVar])

                if savedAddressCheckVar == 1:
                    print("Yes")
                    #savedAddressImg
                    savedAddressDis = "✔"
                elif savedAddressCheckVar == 0:
                    print("No")
                    savedAddressDis = "✘"

                profile_table.insert('', 'end', values=(profileNameVar, emailVar, passwordVar, cardNoVar, expMonthVar, expYearVar, CVVVar, savedAddressDis, firstNameVar, lastNameVar, address1Var, address2Var, cityVar, zipCodeVar, provinceVar, countryVar, phoneNoVar))
                
            #===== create profile time =====#
                create_profile_now = datetime.now()
                create_profile_time = create_profile_now.strftime("[%H:%M:%S]")
                logging_table.insert('', 'end', values=[create_profile_time + " - Profile created"])

                entry_profileName.delete(0, END)
                entry_email.delete(0, END)
                entry_password.delete(0, END)

        btn_createProf = Button(buttonFrame, text="Create", command = createProfileTask, font=('URW Gothic L', '10','bold'), bg="IndianRed2", activebackground="IndianRed1", width=15, height=2)
        btn_createProf.grid(row=0, column=0, pady=5, padx=10, sticky='W')

        def updateProfileTask():
            #print("Profiles updated")
            #===== update profile time =====#
            update_profile_now = datetime.now()
            update_profile_time = update_profile_now.strftime("[%H:%M:%S]")
            logging_table.insert('', 'end', values=[update_profile_time + " - Profiles updated"])

            #Clears table
            for b in profile_table.get_children():
                profile_table.delete(b)

            #Clears arrays
            del profieNameArray[:]
            del emailArray[:]
            del passwordArray[:]
            del cardNoArray[:]
            del expMonthArray[:]
            del expYearArray[:]
            del CVVArray[:]
            del firstNameArray[:]
            del lastNameArray[:]
            del address1Array[:]
            del address2Array[:]
            del cityArray[:]
            del zipCodeArray[:]
            del provinceArray[:]
            del countryArray[:]
            del phoneNoArray[:]
            del savedAddressCheckArray[:]

            #Open csv file to read
            with open('profiles.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)

                #Reads values, appends to arrays and insert into table
                for row in reader:
                    profileNameValue = row[0]
                    emailValue = row[1]
                    passwordValue = row[2]
                    cardNoValue = row[3]
                    expMonthValue = row[4]
                    expYearValue = row[5]
                    CVVValue = row[6]
                    firstNameValue = row[7]
                    lastNameValue = row[8]
                    address1Value = row[9]
                    address2Value = row[10]
                    cityValue = row[11]
                    zipCodeValue = row[12]
                    provinceValue = row[13]
                    countryValue = row[14]
                    phoneNoValue = row[15]
                    savedAddressCheckValue = row[16]

                    profieNameArray.append(profileNameValue)
                    emailArray.append(emailValue)
                    passwordArray.append(passwordValue)
                    cardNoArray.append(cardNoValue)
                    expMonthArray.append(expMonthValue)
                    expYearArray.append(expYearValue)
                    CVVArray.append(CVVValue)
                    firstNameArray.append(firstNameValue)
                    lastNameArray.append(lastNameValue)
                    address1Array.append(address1Value)
                    address2Array.append(address2Value)
                    cityArray.append(cityValue)
                    zipCodeArray.append(zipCodeValue)
                    provinceArray.append(provinceValue)
                    countryArray.append(countryValue)
                    phoneNoArray.append(phoneNoValue)
                    savedAddressCheckArray.append(savedAddressCheckValue)

                    if savedAddressCheckValue == "1":
                        # image = checkIcon
                        savedAddressDis = "✔"
                    elif savedAddressCheckValue == "0":
                        # image = crossIcon
                        savedAddressDis = "✘"

                    profile_table.insert('', 'end', values=(profileNameValue, emailValue, passwordValue, cardNoValue, expMonthValue, expYearValue, CVVValue, savedAddressDis, firstNameValue, lastNameValue, address1Value, address2Value, cityValue, zipCodeValue, provinceValue, countryValue, phoneNoValue))

        #Button to update values
        btn_updateProf = Button(buttonFrame, text="Update", command = updateProfileTask, font=('URW Gothic L', '10','bold'), bg="IndianRed2", activebackground="IndianRed1", width=15, height=2)
        btn_updateProf.grid(row=0, column=4, pady=5, padx=10, sticky='W')

#======= Proxies =======#
    #===== Prozy arrays =====#

    #===== Proxy variables =====#

    #===== Proxy frames =====#

#======= Settings =======#

    #===== Setting frames =====#
        accountDetailFrame = Frame(SettingsTab, bg="black", highlightcolor="white", highlightthickness=3)
        accountDetailFrame.place(x=10, y=75, width=1280, height=300)

        accountTitleFrame = Frame(accountDetailFrame, bg="black")
        accountTitleFrame.place(x=10, y=5, width=1260, height=55)

        notificationsFrame = Frame(SettingsTab, bg="black", highlightcolor="white", highlightthickness=3)
        notificationsFrame.place(x=10, y=385, width=1280, height=300)

        notificationsTitleFrame = Frame(notificationsFrame, bg="black")
        notificationsTitleFrame.place(x=10, y=5, width=1260, height=55)

        discordSettingsFrame = Frame(notificationsFrame, bg="black", highlightcolor="white", highlightthickness=3)
        discordSettingsFrame.place(x=10, y=62, width=400, height=222)

        discordButtonFrame = Frame(discordSettingsFrame, bg="black", highlightcolor="white", highlightthickness=1)
        discordButtonFrame.place(x=6, y=150, width=380, height=60)

    #===== Account frame title =====#
        lbl_accountTitle = Label(accountTitleFrame, text="Account", font=("URW Gothic L", 30, "bold"), fg='red', bg="black")
        lbl_accountTitle.grid(row=0, column=0)

    #===== Notifications frame title =====#
        lbl_notificationsTitle = Label(notificationsTitleFrame, text="Notifications", font=("URW Gothic L", 30, "bold"), fg='red', bg="black")
        lbl_notificationsTitle.grid(row=0, column=0)

    #===== Discord =====#
        discordServerIDVar = StringVar()

        lbl_discordTitle = Label(discordSettingsFrame, text="Discord", font=("URW Gothic L", 20, "bold"), fg='red', bg="black")
        lbl_discordTitle.grid(row=0, column=0)

        lbl_serverID = Label(discordSettingsFrame, text="Server ID", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_serverID.grid(row=1, column=0, pady=3)
        entry_serverID = Entry(discordSettingsFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=24)
        entry_serverID.grid(row=1, column=1, pady=3)

        serverIDArray = []

        def saveServerID():

            serverIDVar = entry_serverID.get()
            serverIDArray.append(serverIDVar)
            print(serverIDArray)

            discord_serverID_save_now = datetime.now()
            discord_serverID_save_time = discord_serverID_save_now.strftime("[%H:%M:%S]")
            logging_table.insert('', 'end', values=[discord_serverID_save_time + " - Discord server ID saved"])

        btn_saveServerID = Button(discordButtonFrame, text="save", command=saveServerID, font=('URW Gothic L', '10','bold'), bg="IndianRed2", activebackground="IndianRed1", width=12, height=2)
        btn_saveServerID.grid(row=2, column=0, padx=10, pady=7, sticky='W')

        def testDiscordBotConnection():      

            serverTestID = serverIDArray[0]
            print(serverTestID)

            discord_connection_test_now = datetime.now()
            discord_connection_test_time = discord_connection_test_now.strftime("[%H:%M:%S]")
            logging_table.insert('', 'end', values=[discord_connection_test_time + " - Discord bot connection tested"])      

        btn_testBot = Button(discordButtonFrame, text="test", command=testDiscordBotConnection, font=('URW Gothic L', '10','bold'), bg="IndianRed2", activebackground="IndianRed1", width=12, height=2)
        btn_testBot.grid(row=2, column=1, padx=10, pady=7, sticky='W')

        btn_startBot = Button(discordButtonFrame, text="start", font=('URW Gothic L', '10','bold'), bg="IndianRed2", activebackground="IndianRed1", width=12, height=2)
        btn_startBot.grid(row=2, column=2, padx=10, pady=7, sticky='W')
root = Tk()
ob = Sneaker(root)
root.mainloop()