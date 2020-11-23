import os, sys
import tkinter as tk
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import tkentrycomplete
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
                    "configure": {"padding": [82, 1], "background": 'gray24', "foreground": 'red'},
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
        ShippingTab = ttk.Frame(tabControl)
        ProxiesTab = ttk.Frame(tabControl)
        SettingsTab = ttk.Frame(tabControl)
        tabControl.add(TasksTab, text="Tasks")
        tabControl.add(ProfilesTab, text="Profile")
        tabControl.add(ShippingTab, text="Address")
        tabControl.add(ProxiesTab, text="Proxy")
        tabControl.add(SettingsTab, text="Settings")
        tabControl.pack(expand=1, fill="both")

        TitleBarFrame = Frame(root, bd=1, bg='black')
        TitleBarFrame.place(x=0, y=40, width=1300, height=75)

        lbl_TaskTabTitle = Label(TitleBarFrame, text="Pie Bot", font=('FixedSYS', '50','bold'), fg='deep sky blue', bg='Black')
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
        taskShippingArray = []

    #======= Task Variables =======#
        self.taskNameVar = StringVar()
        self.siteNameVar = StringVar()
        self.linkVar = StringVar()
        self.sizeChoiceVar = StringVar()
        self.proxyVar = StringVar()
        self.profileVar = StringVar()
        self.taskShippingVar = StringVar()
        self.taskQuantityVar = StringVar()

    #===== Task Frames =====#

        #Frame for inputs, create task, logging
        CreateActionTaskFrame = Frame(TasksTab, bg="black", highlightcolor="white", highlightthickness=3)
        CreateActionTaskFrame.place(x=10, y=75, width=380, height=720)

        btnFrame = Frame(CreateActionTaskFrame, bd=1, bg="black")
        btnFrame.place(x=10, y=310, width=100, height=60)

        loggingTitleFrame = Frame(CreateActionTaskFrame, bd=1, bg="black")
        loggingTitleFrame.place(x=0, y=355, width=320, height=45)

        loggingFrame = Frame(CreateActionTaskFrame, bd=1, bg="black")
        loggingFrame.place(x=10, y=390, width=350, height=315)

        #Frame for treeview and Start task actions
        DisplayTaskFrame = Frame(TasksTab, bd=1, bg='black')
        DisplayTaskFrame.place(x=395, y=75, width=980, height=725)

        DisplayTaskTitleFrame = Frame(DisplayTaskFrame, bg="black")
        DisplayTaskTitleFrame.place(x=7, y=0, width=882, height=45)

        TaskTableFrame = Frame(DisplayTaskFrame, bg="black")
        TaskTableFrame.place(x=7, y=40, width=882, height=605)

        TaskButtonActionFrame = Frame(DisplayTaskFrame, bg="black", highlightcolor="white", highlightthickness=3)
        TaskButtonActionFrame.place(x=248.5, y=655, width=385, height=64)

    #===== Task input =====#
        createTaskTitle = Label(CreateActionTaskFrame, text="Create task", font=("URW Gothic L", 20, "bold"), fg='red', bg="black")
        createTaskTitle.grid(row=0, columnspan=2)

        lbl_taskName = Label(CreateActionTaskFrame, text="Task Name", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_taskName.grid(row=1, column=0, pady=2, padx=10, sticky="W")
        entry_taskName = Entry(CreateActionTaskFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=21)
        entry_taskName.grid(row=1, column=1, pady=2, padx=10, sticky="w")

        lbl_siteName = Label(CreateActionTaskFrame, text="Site Name", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_siteName.grid(row=2, column=0, pady=2, padx=10, sticky="W")
        # combo_siteName = ttk.Combobox(CreateActionTaskFrame, font=("URW Gothic L", 12, "normal"), width=15)
        # combo_siteName['values']=('Nike_TH','Adidas_TH')
        combo_siteName = tkentrycomplete.AutocompleteCombobox(CreateActionTaskFrame, font=("URW Gothic L", 12, "normal"), textvariable="", width=15)
        siteName_available_list = ['Nike_TH','Adidas_TH']
        combo_siteName.set_completion_list(siteName_available_list)
        combo_siteName.grid(row=2, column=1, pady=2, padx=10, sticky="w")

        lbl_link = Label(CreateActionTaskFrame, text="Link", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_link.grid(row=3, column=0, pady=2, padx=10, sticky="w")
        entry_link = Entry(CreateActionTaskFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=21)
        entry_link.grid(row=3, column=1, pady=2, padx=10)

        lbl_sizeChoice = Label(CreateActionTaskFrame, text="Size", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_sizeChoice.grid(row=4, column=0, pady=2, padx=10, sticky="w")
        combo_sizeChoice = tkentrycomplete.AutocompleteCombobox(CreateActionTaskFrame, font=("URW Gothic L", 12, "normal"), textvariable="", width=10)
        size_available_list = ['EU 37.5','EU 38', 'EU 38.5', 'EU 39','EU 40', 'EU 40.5', 'EU 41', 'EU 42', 'EU 42.5', 'EU 43', 'EU 44', '------------------', 'XS', 'S', 'M', 'L', 'XL']
        combo_sizeChoice.set_completion_list(size_available_list)
        # combo_sizeChoice = ttk.Combobox(CreateActionTaskFrame, font=("URW Gothic L", 12, "normal"), textvariable="", width=10)
        # combo_sizeChoice['values']=('EU 37.5','EU 38', 'EU 38.5', 'EU 39','EU 40', 'EU 40.5', 'EU 41', 'EU 42', 'EU 42.5', 'EU 43', 'EU 44', '------------------', 'XS', 'S', 'M', 'L', 'XL')
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

        lbl_shipping = Label(CreateActionTaskFrame, text="Shipping", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_shipping.grid(row=7, column=0, pady=2, padx=10, sticky="W")
        entry_shipping = Entry(CreateActionTaskFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=21)
        entry_shipping.grid(row=7, column=1, pady=2, padx=10, sticky="w")

        lbl_taskQuantity = Label(CreateActionTaskFrame, text="Task Quantity", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_taskQuantity.grid(row=8, column=0, pady=2, padx=10, sticky="W")
        entry_taskQuantity = Entry(CreateActionTaskFrame, textvariable="", font=("URW Gothic L", 12, "normal"), fg='black', width=21)
        entry_taskQuantity.grid(row=8, column=1, pady=2, padx=10, sticky="w")
    
    #===== Task Logging =====#
        loggingTitle = Label(loggingTitleFrame, text="Log", font=('URW Gothic L', '17','bold'), fg='Red', bg='black')
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

        taskAmountTitle = Label(DisplayTaskTitleFrame, text="Tasks " + "(0)", font=("URW Gothic L", 20, "bold"), fg='red', bg="black")
        taskAmountTitle.grid(row=0, columnspan=1)

        scroll_y = Scrollbar(TaskTableFrame, orient=VERTICAL, troughcolor='black')
        task_table = ttk.Treeview(TaskTableFrame, columns=("ID", "SiteName", "TaskName", "Profile", "Shipping", "Link", "Size", "Proxy"), yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=task_table.yview)

        #Treeview headings
        task_table.heading("ID", text="ID", anchor='w')
        task_table.heading("SiteName", text="Site", anchor='w')
        task_table.heading("TaskName", text="Task name", anchor='w')
        task_table.heading("Profile", text="Profile", anchor='w')
        task_table.heading("Shipping", text="Shipping", anchor='w')
        task_table.heading("Link", text="Link", anchor='w')
        task_table.heading("Size", text="Size", anchor='w')
        task_table.heading("Proxy", text="Proxy", anchor='w')
        task_table['show']='headings'

        #Treeview columns
        task_table.column("ID", width=30, anchor='w')
        task_table.column("SiteName", width=90, anchor='w')
        task_table.column("TaskName", width=110, anchor='w')
        task_table.column("Profile", width=100, anchor='w')
        task_table.column("Shipping", width=100, anchor='w')
        task_table.column("Link", width=225, anchor='w')
        task_table.column("Size", width=60, anchor='w')
        task_table.column("Proxy", width=90, anchor='w')
        task_table.pack(fill=BOTH, expand=1, anchor='w')

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
                    shippingVar = entry_shipping.get()

                    taskNameArray.append(taskNameVar)
                    siteNameArray.append(siteNameVar)
                    linkArray.append(linkVar)
                    sizeChoiceArray.append(sizeVar)
                    proxyArray.append(proxyVar)
                    profileArray.append(profileVar)
                    taskShippingArray.append(shippingVar)

                    task_table.insert('', 'end', values=(self.i, siteNameVar, taskNameVar, profileVar, shippingVar, linkVar, sizeVar, proxyVar))

                    task_create_now = datetime.now()
                    task_create_time = task_create_now.strftime("[%H:%M:%S]")

                    logging_table.insert('', 'end', values=[task_create_time + " - Task " + str(self.i) + " created"])

                    taskAmountTitle['text'] = "Tasks " + "(" + str(self.i) + ")"

                    self.i = self.i + 1

                entry_taskName.delete(0, END)
                combo_siteName.delete(0, END)
                entry_link.delete(0, END)
                combo_sizeChoice.delete(0, END)
                combo_proxy.delete(0, END)
                entry_profile.delete(0, END)
                entry_shipping.delete(0, END)
                entry_taskQuantity.delete(0, END)

        createTaskBtn = Button(btnFrame, text="➕ Create", command=CreateTaskCommand, font=('URW Gothic L', '10','bold'), bg="IndianRed2", activebackground="IndianRed1", width=9, height=2)
        createTaskBtn.grid(row=0, column=0)

    #===== Task action frame (start, clear)=====#
    
        def startAllTask():

            task_start_now = datetime.now()
            task_start_time = task_start_now.strftime("[%H:%M:%S]")
            logging_table.insert('', 'end', values=[task_start_time + " - Tasks completed "])

            for index in range(len(taskNameArray)):

                #Get task id
                taskID = index + 1
                print("Task "+ str(taskID) + " started")

                #Get the site name from the array so driver can enter the correct site
                siteNameValue = siteNameArray[index]

                #=== Set up chromedriver ===#
                PATH = "C:\Program Files (x86)\chromedriver.exe"
                driver = webdriver.Chrome(PATH)

                #=== Create profile and shipping index to retrieve profile and shipping info ===#
                profileIndex = profieNameArray.index(profileArray[index])
                shippingIndex = shippingNameArray.index(taskShippingArray[index])

                if siteNameValue == "Nike_TH":

                    nikeTask = True
                    while nikeTask == True:
                        #=== Get details ===#
                        emailInValue = emailArray[profileIndex]
                        passwordInValue = passwordArray[profileIndex]

                        sizeInValue = sizeChoiceArray[index]

                        cardNoValue = cardNoArray[profileIndex]
                        expMonthValue = expMonthArray[profileIndex]
                        expYearValue = expYearArray[profileIndex]
                        cardExpDates = expMonthValue + expYearValue
                        CVVValue = CVVArray[profileIndex]

                        #=== Get link ===#
                        driver.get(linkArray[index])
                        time.sleep(3)

                        #=== Log in into nike website ===#
                        try:
                            # menu = driver.find_element_by_xpath("//button[@aria-label='เมนู']")
                            menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='เมนู']")))
                        except:
                            driver.quit()
                            task_start_openMenu_now = datetime.now()
                            task_start_openMenu_time = task_start_openMenu_now.strftime("[%H:%M:%S]")
                            logging_table.insert('', 'end', values=[task_start_openMenu_time + " - Task " + str(taskID) + " stopped (Failed to open menu)"])
                        else:
                            menu.click()
                        
                        try:
                            # loginInput = driver.find_element_by_xpath("//button[@data-qa='join-login-button']")
                            loginInput = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='join-login-button']")))
                        except:
                            driver.quit()
                            task_start_openMenu_now = datetime.now()
                            task_start_openMenu_time = task_start_openMenu_now.strftime("[%H:%M:%S]")
                            logging_table.insert('', 'end', values=[task_start_openMenu_time + " - Task " + str(taskID) + " stopped (Failed to open log-in page)"])
                        else:
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
                            try:
                                size375But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 37.5")]')))
                            except:
                                driver.quit()
                                task_start_selectSize_now = datetime.now()
                                task_start_selectSize_time = task_start_selectSize_now.strftime("[%H:%M:%S]")
                                logging_table.insert('', 'end', values=[task_start_selectSize_time + " - Task " + str(taskID) + " stopped (Size unavailable)"])
                            else:
                                size375But.click()
                        elif sizeInValue == "EU 38":
                            try:
                                size38But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 38")]')))
                            except:
                                driver.quit()
                                task_start_selectSize_now = datetime.now()
                                task_start_selectSize_time = task_start_selectSize_now.strftime("[%H:%M:%S]")
                                logging_table.insert('', 'end', values=[task_start_selectSize_time + " - Task " + str(taskID) + " stopped (Size unavailable)"])
                            else:
                                size38But.click()
                        elif sizeInValue == "EU 38.5":
                            try:
                                size385But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 38.5")]')))
                            except:
                                driver.quit()
                                task_start_selectSize_now = datetime.now()
                                task_start_selectSize_time = task_start_selectSize_now.strftime("[%H:%M:%S]")
                                logging_table.insert('', 'end', values=[task_start_selectSize_time + " - Task " + str(taskID) + " stopped (Size unavailable)"])
                            else:
                                size385But.click()
                        elif sizeInValue == "EU 39":
                            try:
                                size39But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 39")]')))
                            except:
                                driver.quit()
                                task_start_selectSize_now = datetime.now()
                                task_start_selectSize_time = task_start_selectSize_now.strftime("[%H:%M:%S]")
                                logging_table.insert('', 'end', values=[task_start_selectSize_time + " - Task " + str(taskID) + " stopped (Size unavailable)"])
                            else:
                                size39But.click()
                        elif sizeInValue == "EU 40":
                            try:
                                size40But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 40")]')))
                            except:
                                driver.quit()
                                task_start_selectSize_now = datetime.now()
                                task_start_selectSize_time = task_start_selectSize_now.strftime("[%H:%M:%S]")
                                logging_table.insert('', 'end', values=[task_start_selectSize_time + " - Task " + str(taskID) + " stopped (Size unavailable)"])
                            else:    
                                size40But.click()
                        elif sizeInValue == "EU 40.5":
                            try:
                                size405But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 40.5")]')))
                            except:
                                driver.quit()
                                task_start_selectSize_now = datetime.now()
                                task_start_selectSize_time = task_start_selectSize_now.strftime("[%H:%M:%S]")
                                logging_table.insert('', 'end', values=[task_start_selectSize_time + " - Task " + str(taskID) + " stopped (Size unavailable)"])
                            else:
                                size405But.click()
                        elif sizeInValue == "EU 41":
                            try:
                                size41But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 41")]')))
                            except:
                                driver.quit()
                                task_start_selectSize_now = datetime.now()
                                task_start_selectSize_time = task_start_selectSize_now.strftime("[%H:%M:%S]")
                                logging_table.insert('', 'end', values=[task_start_selectSize_time + " - Task " + str(taskID) + " stopped (Size unavailable)"])
                            else:
                                size41But.click()
                        elif sizeInValue == "EU 42":
                            try:
                                size42But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 42")]')))
                            except:
                                driver.quit()
                                task_start_selectSize_now = datetime.now()
                                task_start_selectSize_time = task_start_selectSize_now.strftime("[%H:%M:%S]")
                                logging_table.insert('', 'end', values=[task_start_selectSize_time + " - Task " + str(taskID) + " stopped (Size unavailable)"])
                            else:
                                size42But.click()
                        elif sizeInValue == "EU 42.5":
                            try:
                                size425But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 42.5")]')))
                            except:
                                driver.quit()
                                task_start_selectSize_now = datetime.now()
                                task_start_selectSize_time = task_start_selectSize_now.strftime("[%H:%M:%S]")
                                logging_table.insert('', 'end', values=[task_start_selectSize_time + " - Task " + str(taskID) + " stopped (Size unavailable)"])
                            else:
                                size425But.click()
                        elif sizeInValue == "EU 43":
                            try:
                                size43But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 43")]')))
                            except:
                                driver.quit()
                                task_start_selectSize_now = datetime.now()
                                task_start_selectSize_time = task_start_selectSize_now.strftime("[%H:%M:%S]")
                                logging_table.insert('', 'end', values=[task_start_selectSize_time + " - Task " + str(taskID) + " stopped (Size unavailable)"])
                            else:
                                size43But.click()
                        elif sizeInValue == "EU 44":
                            try:
                                size44But = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"EU 44")]')))
                            except:
                                driver.quit()
                                task_start_selectSize_now = datetime.now()
                                task_start_selectSize_time = task_start_selectSize_now.strftime("[%H:%M:%S]")
                                logging_table.insert('', 'end', values=[task_start_selectSize_time + " - Task " + str(taskID) + " stopped (Size unavailable)"])
                            else:
                                size44But.click()

                        #=== Confirms size and proceed to checkout ===#
                        time.sleep(0.5)
                        try:
                            confirmSizeButton = driver.find_element_by_xpath("//button[@data-qa='feed-buy-cta']")
                            #confirmSizeButton = driver.find_element_by_xpath("//button[@data-qa='add-to-cart']")
                        except:
                            driver.close()
                            task_start_confirmSize_now = datetime.now()
                            task_start_confirmSize_time = task_start_confirmSize_now.strftime("[%H:%M:%S]")
                            logging_table.insert('', 'end', values=[task_start_confirmSize_time + " - Task " + str(taskID) + " stopped (Failed to proceed to checkout)"])
                            break
                        else:
                            confirmSizeButton.click()

                        #=== Click on the second expand button ===#
                        try:
                            expandButton = WebDriverWait(driver, 10).until(EC.elements_to_be_clickable((By.XPATH, "//div[@class='expand-collapse']")))
                        except:
                            driver.close()
                            task_start_expandBut_now = datetime.now()
                            task_start_expandBut_time = task_start_expandBut_now.strftime("[%H:%M:%S]")
                            logging_table.insert('', 'end', values=[task_start_expandBut_time + " - Task " + str(taskID) + " stopped (Failed to enter card details)"])
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

                        try:
                            confirmCardBtn = driver.find_element_by_xpath("//button[contains(text(),'ดำเนินการต่อ')]")
                        except:
                            driver.close()
                            task_start_confirmCard_now = datetime.now()
                            task_start_confirmCard_time = task_start_confirmCard_now.strftime("[%H:%M:%S]")
                            logging_table.insert('', 'end', values=[task_start_confirmCard_time + " - Task " + str(taskID) + " stopped (Failed to confirm card)"])
                        else:
                            confirmCardBtn.submit()

                        #=== Confirm checkout ===#

                        try:
                            confirmCheckoutBtn = driver.find_element_by_xpath("//button[contains(text(),'ส่งคำสั่งซื้อ')]")
                        except:
                            driver.close()
                            task_start_checkout_now = datetime.now()
                            task_start_checkout_time = task_start_checkout_now.strftime("[%H:%M:%S]")
                            logging_table.insert('', 'end', values=[task_start_checkout_time + " - Task " + str(taskID) + " stopped (Failed to checkout)"])
                        else:                      
                            confirmCheckoutBtn.click()

                        #=== Wait in queue ===#

                elif siteNameValue == "Adidas_TH":

                #=== Test ===#
                    print("Adidas Test")

                #=== Set up chromedriver ===#
                    # PATH = "C:\Program Files (x86)\chromedriver.exe"
                    # driver = webdriver.Chrome(PATH)

                #=== Get link ===#
                    driver.get(linkArray[index])
                    time.sleep(3)

        StartAllTaskBtn = Button(TaskButtonActionFrame, text="► Start all", command = startAllTask, font=('URW Gothic L', '10','bold'), bg="IndianRed2", activebackground="IndianRed1", width=20, height=2)
        StartAllTaskBtn.grid(row=0, column=0, padx=10, pady=8)

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

                taskAmountTitle['text'] = "Tasks " + "(0)"

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

        clearTaskBtn = Button(TaskButtonActionFrame, text="➖ Clear", command=ClearTaskCommand, font=('URW Gothic L', '10','bold'), bg="IndianRed2", activebackground="IndianRed1", width=20, height=2)
        clearTaskBtn.grid(row=0, column=3, padx=10, pady=8)

#======= Profiles =======#

    #======= Profile Arrays =======#
        profieNameArray = []
        emailArray = []
        passwordArray = []
        profileSiteNameArray = []
        cardNoArray = []
        expMonthArray = []
        expYearArray = []
        CVVArray = []

    #======= Profile Variables =======#
        profileNameVar = StringVar()
        emailVar = StringVar()
        passwordVar = StringVar()
        profileSiteNameVar = StringVar()
        cardNoVar = StringVar()
        expMonthVar = StringVar()
        expYearVar = StringVar()
        CVVVar = StringVar()

    #======= Profile Frames =======#
        nameLogInFrame = Frame(ProfilesTab, bg="black", highlightcolor="white", highlightthickness=3)
        nameLogInFrame.place(x=10, y=75, width=430, height=715)

        buttonFrame = Frame(nameLogInFrame, bd=1, bg="black", highlightcolor="white", highlightthickness=1)
        buttonFrame.place(x=50, y=380, width=305, height=55)

        warningFrame = Frame(nameLogInFrame, bg="black", highlightcolor="white", highlightthickness=1)
        warningFrame.place(x=10, y=445, width=405, height=65)

        DisplayProfileFrame = Frame(ProfilesTab,bg="black")
        DisplayProfileFrame.place(x=460, y=75, width=820, height=715)

        profileDisTitle = Label(nameLogInFrame, text="Profile name", font=("URW Gothic L", 20, "bold"), fg='red', bg="black")
        profileDisTitle.grid(row=1, column=0, columnspan=2, pady=3, sticky='W')

    #======= Profile details =======#
        #Profile name
        lbl_profileName = Label(nameLogInFrame, text="Profile name", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_profileName.grid(row=2, column=0, sticky="W")
        entry_profileName = Entry(nameLogInFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=20)
        entry_profileName.grid(row=2, column=1, padx=10, sticky="w")

        #Profile site name
        lbl_profileSiteName = Label(nameLogInFrame, text="Site name", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_profileSiteName.grid(row=3, column=0, sticky="W")
        # combo_profileSiteName = ttk.Combobox(nameLogInFrame, font=("URW Gothic L", 12, "normal"), width=15)
        # combo_profileSiteName['values']=('Nike_TH')
        combo_profileSiteName = tkentrycomplete.AutocompleteCombobox(nameLogInFrame, font=("URW Gothic L", 12, "normal"), width=15)
        profileSiteName_available_list = ['Nike_TH','Adidas_TH']
        combo_profileSiteName.set_completion_list(profileSiteName_available_list)
        combo_profileSiteName.grid(row=3, column=1, padx=10, sticky="w")

    #======= Log in details =======#
        logInTitle = Label(nameLogInFrame, text="Log-in details", font=("URW Gothic L", 20, "bold"), fg='red', bg="black")
        logInTitle.grid(row=4, column=0, columnspan=2, pady=3, sticky='W')

        #Email
        lbl_email = Label(nameLogInFrame, text="Email", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_email.grid(row=5, column=0, sticky="W")
        entry_email = Entry(nameLogInFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=30)
        entry_email.grid(row=5, column=1, padx=10, sticky="w")

        #Password
        lbl_password = Label(nameLogInFrame, text="Password", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_password.grid(row=6, column=0, sticky="W")
        entry_password = Entry(nameLogInFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=30)
        entry_password.grid(row=6, column=1, padx=10, sticky="w")

    #======= Card details =======#
        shippingTitle = Label(nameLogInFrame, text="Card details", font=("URW Gothic L", 20, "bold"), fg='red', bg="black")
        shippingTitle.grid(row=7, column=0, columnspan=2, pady=2, sticky='W')

        lbl_cardNumber = Label(nameLogInFrame, text="Card No.", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_cardNumber.grid(row=8, column=0, sticky="W")
        entry_cardNumber = Entry(nameLogInFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=21)
        entry_cardNumber.grid(row=8, column=1, padx=10, sticky="w")

        lbl_expMonth = Label(nameLogInFrame, text="Exp. month", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_expMonth.grid(row=9, column=0, sticky="W")
        combo_expMonth = ttk.Combobox(nameLogInFrame, width=5, font=("URW Gothic L", 12, "normal"))
        combo_expMonth['values']=('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
        combo_expMonth.grid(row=9, column=1, padx=10, sticky="w")

        lbl_expYear = Label(nameLogInFrame, text="Exp. year", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_expYear.grid(row=10, column=0, sticky="W")
        combo_expYear = ttk.Combobox(nameLogInFrame, width=10, font=("URW Gothic L", 12, "normal"))
        combo_expYear['values']=('2021', '2022', '2023', '2024', '2025', '2026')
        combo_expYear.grid(row=10, column=1, padx=10, sticky="w")

        lbl_CVV = Label(nameLogInFrame, text="CVV", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_CVV.grid(row=11, column=0, sticky="W")
        entry_CVV = Entry(nameLogInFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=5)
        entry_CVV.grid(row=11, column=1, padx=10, sticky="w")

    #======= Table to display profiles =======#
        style = ttk.Style()

        scroll_x = Scrollbar(DisplayProfileFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(DisplayProfileFrame, orient=VERTICAL)
        profile_table = ttk.Treeview(DisplayProfileFrame, columns=("ProfileName", "Email", "Password", "ProfSite", "CardNo", "ExpMonth", "ExpYear", "CVV"), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=profile_table.xview)
        scroll_y.config(command=profile_table.yview)

        #Treeview headings
        profile_table.heading("ProfileName", text="Profile name", anchor='w')
        profile_table.heading("Email", text="Email", anchor='w')
        profile_table.heading("Password", text="Password", anchor='w')
        profile_table.heading("ProfSite", text="Site name", anchor='w')
        profile_table.heading("CardNo", text="Card no.", anchor='w')
        profile_table.heading("ExpMonth", text="Exp. month", anchor='w')
        profile_table.heading("ExpYear", text="Exp. year", anchor='w')
        profile_table.heading("CVV", text="CVV", anchor='w')
        profile_table['show']='headings'

        #Treeview columns
        profile_table.column("ProfileName", width=110, anchor='w')
        profile_table.column("Email", width=200, anchor='w')
        profile_table.column("Password", width=90, anchor='w')
        profile_table.column("ProfSite", width=110, anchor='w')
        profile_table.column("CardNo", width=120, anchor='w')
        profile_table.column("ExpMonth", width=100, anchor='w')
        profile_table.column("ExpYear", width=90, anchor='w')
        profile_table.column("CVV", width=45, anchor='w')
        profile_table.pack(fill=BOTH, expand=1)

    #======= Warning frame =======#
        lbl_exclamationMark = Label(warningFrame, text="!", font=("URW Gothic L", 35, "bold"), bg="black", fg="red")
        lbl_exclamationMark.grid(row=0, column=0, rowspan=2)

        lbl_warningMessage = Label(warningFrame, text="Please make sure you saved your address and", font=("URW Gothic L", 13, "bold"), bg="black", fg="red")
        lbl_warningMessage.grid(row=0, column=1)

        lbl_warningMessage2 = Label(warningFrame, text="verified your phone number in your accounts", font=("URW Gothic L", 13, "bold"), bg="black", fg="red")
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
                profileSiteNameVary = combo_profileSiteName.get()
                cardNoVar = entry_cardNumber.get()
                expMonthVar = combo_expMonth.get()
                expYearVar = combo_expYear.get()
                CVVVar = entry_CVV.get()

                #Writes values to csv file
                with open('profiles.csv', 'a') as csvfile:
                    writer = csv.writer(csvfile, lineterminator = '\r')
                    writer.writerow([profileNameVar, emailVar, passwordVar, profileSiteNameVary, cardNoVar, expMonthVar, expYearVar, CVVVar])

                profile_table.insert('', 'end', values=(profileNameVar, emailVar, passwordVar, profileSiteNameVary, cardNoVar, expMonthVar, expYearVar, CVVVar))
                
            #===== create profile time =====#
                create_profile_now = datetime.now()
                create_profile_time = create_profile_now.strftime("[%H:%M:%S]")
                logging_table.insert('', 'end', values=[create_profile_time + " - Profile created"])

            #Delete boxes
                entry_profileName.delete(0, END)
                entry_email.delete(0, END)
                entry_password.delete(0, END)
                combo_profileSiteName.delete(0, END)
                entry_cardNumber.delete(0, END)
                combo_expMonth.delete(0, END)
                combo_expYear.delete(0, END)
                entry_CVV.delete(0, END)

        btn_createProf = Button(buttonFrame, text="➕ Create", command = createProfileTask, font=('URW Gothic L', '10','bold'), bg="IndianRed2", activebackground="IndianRed1", width=15, height=2)
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
            del profileSiteNameArray[:]
            del cardNoArray[:]
            del expMonthArray[:]
            del expYearArray[:]
            del CVVArray[:]

            #Open csv file to read
            with open('profiles.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)

                #Reads values, appends to arrays and insert into table
                for row in reader:
                    profileNameValue = row[0]
                    emailValue = row[1]
                    passwordValue = row[2]
                    profileSiteNameValue = row[3]
                    cardNoValue = row[4]
                    expMonthValue = row[5]
                    expYearValue = row[6]
                    CVVValue = row[7]

                    profieNameArray.append(profileNameValue)
                    emailArray.append(emailValue)
                    passwordArray.append(passwordValue)
                    profileSiteNameArray.append(profileSiteNameValue)
                    cardNoArray.append(cardNoValue)
                    expMonthArray.append(expMonthValue)
                    expYearArray.append(expYearValue)
                    CVVArray.append(CVVValue)

                    profile_table.insert('', 'end', values=(profileNameValue, emailValue, passwordValue, profileSiteNameValue, cardNoValue, expMonthValue, expYearValue, CVVValue))

        #Button to update values
        btn_updateProf = Button(buttonFrame, text="↑ Update", command = updateProfileTask, font=('URW Gothic L', '10','bold'), bg="IndianRed2", activebackground="IndianRed1", width=15, height=2)
        btn_updateProf.grid(row=0, column=4, pady=5, padx=10, sticky='W')

#======= Shipping =======#

    #===== Shipping arrays =====#

        shippingNameArray = []
        shippingFirstNameArray = []
        shippingLastNameArray = []
        shippingAddress1Array = []
        shippingAddress2Array = []
        shippingCityArray = []
        shippingProvinceStateArray = []
        shippingZipCodeArray = []
        shippingCountryArray = []
        shippingPhoneNoArray = []
        shippingEmailArray = []

    #===== Billing arrays =====#

        billingSameShippingArray = []
        billingNameArray = []
        billingFirstNameArray = []
        billingLastNameArray = []
        billingAddress1Array = []
        billingAddress2Array = []
        billingCityArray = []
        billingProvinceStateArray = []
        billingZipCodeArray = []
        billingCountryArray = []
        billingPhoneNoArray = []
        billingEmailArray = []

    #===== Shipping variables =====#

        shippingNameVar = StringVar()
        shippingFirstNameVar = StringVar()
        shippingLastNameVar = StringVar()
        shippingAddress1Var = StringVar()
        shippingAddress2Var = StringVar()
        shippingCityVar = StringVar()
        shippingProvinceStateVar = StringVar()
        shippingZipCodeVar = StringVar()
        shippingCountryVar = StringVar()
        shippingPhoneNoVar = StringVar()
        shippingEmailVar = StringVar()

    #===== Billing variables =====#

        billingNameVar = StringVar()
        billingFirstNameVar = StringVar()
        billingLastNameVar = StringVar()
        billingAddress1Var = StringVar()
        billingAddress2Var = StringVar()
        billingCityVar = StringVar()
        billingProvinceStateVar = StringVar()
        billingZipCodeVar = StringVar()
        billingCountryVar = StringVar()
        billingPhoneNoVar = StringVar()
        billingEmailVar = StringVar()
        billingSameVar = IntVar()

    #===== Shipping frames =====#

        shippingEntryFrame = Frame(ShippingTab, bg="black", highlightcolor="white", highlightthickness=3)
        shippingEntryFrame.place(x=10, y=75, width=1280, height=285)

        shippingDetailsFrame = Frame(shippingEntryFrame, bg="black")
        shippingDetailsFrame.place(x=0, y=0, width=637, height=279)

        billingDetailsFrame = Frame(shippingEntryFrame, bg="black")
        billingDetailsFrame.place(x=637, y=0, width=637, height=279)

        shippingButtonFrame = Frame(ShippingTab, bg="black", highlightcolor="white", highlightthickness=1)
        shippingButtonFrame.place(x=497.5, y=370, width=305, height=55)

        shippingTableFrame = Frame(ShippingTab, bg="white")
        shippingTableFrame.place(x=10, y=435, width=1280, height=355)

    #===== Shipping details =====#
        lbl_shippingTitle = Label(shippingDetailsFrame, text="Shipping details", font=("URW Gothic L", 20, "bold"), fg='red', bg="black")
        lbl_shippingTitle.grid(row=0, column=0, columnspan=4, sticky="w")

        lbl_shippingName = Label(shippingDetailsFrame, text="Name", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_shippingName.grid(row=1, column=0, sticky="W")
        entry_shippingName = Entry(shippingDetailsFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=20)
        entry_shippingName.grid(row=1, column=1, padx=10, sticky="w")

        lbl_shippingFirstName = Label(shippingDetailsFrame, text="First name", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_shippingFirstName.grid(row=2, column=0, sticky="W")
        entry_shippingFirstName = Entry(shippingDetailsFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=20)
        entry_shippingFirstName.grid(row=2, column=1, padx=10, sticky="w")

        lbl_shippingLastName = Label(shippingDetailsFrame, text="Last name", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_shippingLastName.grid(row=2, column=2, sticky="W")
        entry_shippingLastName = Entry(shippingDetailsFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=20)
        entry_shippingLastName.grid(row=2, column=3, padx=10, sticky="w")

        lbl_shippingAddress1 = Label(shippingDetailsFrame, text="Address 1", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_shippingAddress1.grid(row=3, column=0, sticky="W")
        entry_shippingAddress1 = Entry(shippingDetailsFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=54)
        entry_shippingAddress1.grid(row=3, column=1, columnspan=3, padx=10, sticky="w")

        lbl_shippingAddress2 = Label(shippingDetailsFrame, text="Address 2", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_shippingAddress2.grid(row=4, column=0, sticky="W")
        entry_shippingAddress2 = Entry(shippingDetailsFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=54)
        entry_shippingAddress2.grid(row=4, column=1, columnspan=3, padx=10, sticky="w")

        lbl_shippingCity = Label(shippingDetailsFrame, text="City", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_shippingCity.grid(row=5, column=0, sticky="W")
        entry_shippingCity = Entry(shippingDetailsFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=20)
        entry_shippingCity.grid(row=5, column=1, columnspan=3, padx=10, sticky="w")

        lbl_shippingProvince = Label(shippingDetailsFrame, text="Province", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_shippingProvince.grid(row=5, column=2, sticky="W")
        combo_shippingProvince = ttk.Combobox(shippingDetailsFrame, font=("URW Gothic L", 12, "normal"), textvariable="", width=18)
        combo_shippingProvince['values']=('Bangkok', 'Chiang mai', 'Chiang rai', 'Pattaya')
        combo_shippingProvince.grid(row=5, column=3, padx=10, sticky="w")

        lbl_shippingZipCode = Label(shippingDetailsFrame, text="Zipcode", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_shippingZipCode.grid(row=6, column=0, sticky="W")
        entry_shippingZipCode = Entry(shippingDetailsFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=20)
        entry_shippingZipCode.grid(row=6, column=1, columnspan=3, padx=10, sticky="w")

        lbl_shippingCountry = Label(shippingDetailsFrame, text="Country", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_shippingCountry.grid(row=6, column=2, sticky="W")
        combo_shippingCountry = ttk.Combobox(shippingDetailsFrame, font=("URW Gothic L", 12, "normal"), textvariable="", width=18)
        combo_shippingCountry['values']=('Thailand')
        combo_shippingCountry.grid(row=6, column=3, padx=10, sticky="w")

        lbl_shippingPhoneNo = Label(shippingDetailsFrame, text="Phone no.", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_shippingPhoneNo.grid(row=7, column=0, sticky="W")
        entry_shippingPhoneNo = Entry(shippingDetailsFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=20)
        entry_shippingPhoneNo.grid(row=7, column=1, padx=10, sticky="w")

        lbl_shippingEmail = Label(shippingDetailsFrame, text="Email", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_shippingEmail.grid(row=8, column=0, sticky="W")
        entry_shippingEmail = Entry(shippingDetailsFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=54)
        entry_shippingEmail.grid(row=8, column=1, columnspan=3, padx=10, sticky="w")

    #===== Billing details =====#
        lbl_billingTitle = Label(billingDetailsFrame, text="Billing details", font=("URW Gothic L", 20, "bold"), fg='red', bg="black")
        lbl_billingTitle.grid(row=0, column=0, columnspan=4, sticky="w")

        lbl_billingFirstName = Label(billingDetailsFrame, text="First name", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_billingFirstName.grid(row=2, column=0, sticky="W")
        entry_billingFirstName = Entry(billingDetailsFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=20)
        entry_billingFirstName.grid(row=2, column=1, padx=10, sticky="w")

        lbl_billingLastName = Label(billingDetailsFrame, text="Last name", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_billingLastName.grid(row=2, column=2, sticky="W")
        entry_billingLastName = Entry(billingDetailsFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=20)
        entry_billingLastName.grid(row=2, column=3, padx=10, sticky="w")

        lbl_billingAddress1 = Label(billingDetailsFrame, text="Address 1", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_billingAddress1.grid(row=3, column=0, sticky="W")
        entry_billingAddress1 = Entry(billingDetailsFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=54)
        entry_billingAddress1.grid(row=3, column=1, columnspan=3, padx=10, sticky="w")

        lbl_billingAddress2 = Label(billingDetailsFrame, text="Address 2", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_billingAddress2.grid(row=4, column=0, sticky="W")
        entry_billingAddress2 = Entry(billingDetailsFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=54)
        entry_billingAddress2.grid(row=4, column=1, columnspan=3, padx=10, sticky="w")

        lbl_billingCity = Label(billingDetailsFrame, text="City", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_billingCity.grid(row=5, column=0, sticky="W")
        entry_billingCity = Entry(billingDetailsFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=20)
        entry_billingCity.grid(row=5, column=1, columnspan=3, padx=10, sticky="w")

        lbl_billingProvince = Label(billingDetailsFrame, text="Province", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_billingProvince.grid(row=5, column=2, sticky="W")
        combo_billingProvince = ttk.Combobox(billingDetailsFrame, font=("URW Gothic L", 12, "normal"), textvariable="", width=18)
        combo_billingProvince['values']=('Bangkok', 'Chiang mai', 'Chiang rai', 'Pattaya')
        combo_billingProvince.grid(row=5, column=3, padx=10, sticky="w")

        lbl_billingZipCode = Label(billingDetailsFrame, text="Zipcode", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_billingZipCode.grid(row=6, column=0, sticky="W")
        entry_billingZipCode = Entry(billingDetailsFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=20)
        entry_billingZipCode.grid(row=6, column=1, columnspan=3, padx=10, sticky="w")

        lbl_billingCountry = Label(billingDetailsFrame, text="Country", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_billingCountry.grid(row=6, column=2, sticky="W")
        combo_billingCountry = ttk.Combobox(billingDetailsFrame, font=("URW Gothic L", 12, "normal"), textvariable="", width=18)
        combo_billingCountry['values']=('Thailand')
        combo_billingCountry.grid(row=6, column=3, padx=10, sticky="w")

        lbl_billingPhoneNo = Label(billingDetailsFrame, text="Phone no.", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_billingPhoneNo.grid(row=7, column=0, sticky="W")
        entry_billingPhoneNo = Entry(billingDetailsFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=20)
        entry_billingPhoneNo.grid(row=7, column=1, padx=10, sticky="w")

        lbl_billingEmail = Label(billingDetailsFrame, text="Email", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_billingEmail.grid(row=8, column=0, sticky="W")
        entry_billingEmail = Entry(billingDetailsFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=54)
        entry_billingEmail.grid(row=8, column=1, columnspan=3, padx=10, sticky="w")

        radioBtn_billingSame = Checkbutton(billingDetailsFrame, text="Same as shipping", variable=billingSameVar, font=("URW Gothic L", 12, "bold"), background = "black", foreground="red", activebackground="black", activeforeground="red")
        radioBtn_billingSame.grid(row=9, columnspan=4, padx=10, sticky="w")

        def sameShippingTest():
            testState = billingSameVar.get()
            print(testState)

    #===== Shipping table =====#

        scroll_x = Scrollbar(shippingTableFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(shippingTableFrame, orient=VERTICAL)
        shipping_table = ttk.Treeview(shippingTableFrame, columns=("ShippingName", "FirstName", "LastName", "Address1", "Address2", "City", "Province", "ZipCode", "Country", "PhoneNo","Email",\
             "BillingSame?","BillingFirstName", "BillingLastName", "BillingAddress1", "BillingAddress2", "BillingCity", "BillingProvince", "BillingZipCode", "BillingCountry", "BillingPhoneNo","BillingEmail"), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=shipping_table.xview)
        scroll_y.config(command=shipping_table.yview)

        #Treeview headings
        shipping_table.heading("ShippingName", text="Name", anchor='w')
        shipping_table.heading("FirstName", text="First name", anchor='w')
        shipping_table.heading("LastName", text="Last name", anchor='w')
        shipping_table.heading("Address1", text="Address 1", anchor='w')
        shipping_table.heading("Address2", text="Address 2", anchor='w')
        shipping_table.heading("City", text="City", anchor='w')
        shipping_table.heading("Province", text="Province", anchor='w')
        shipping_table.heading("ZipCode", text="Zipcode", anchor='w')
        shipping_table.heading("Country", text="Country", anchor='w')
        shipping_table.heading("PhoneNo", text="Phone no.", anchor='w')
        shipping_table.heading("Email", text="Email", anchor='w')
        shipping_table.heading("BillingSame?",text="Billing same?", anchor="center")
        shipping_table.heading("BillingFirstName", text="Billing First name", anchor='w')
        shipping_table.heading("BillingLastName", text="Billing Last name", anchor='w')
        shipping_table.heading("BillingAddress1", text="Billing address 1", anchor='w')
        shipping_table.heading("BillingAddress2", text="Billing address 2", anchor='w')
        shipping_table.heading("BillingCity", text="Billing city", anchor='w')
        shipping_table.heading("BillingProvince", text="Billing province", anchor='w')
        shipping_table.heading("BillingZipCode", text="Billing zipcode", anchor='w')
        shipping_table.heading("BillingCountry", text="Billing country", anchor='w')
        shipping_table.heading("BillingPhoneNo", text="Billing phone no.", anchor='w')
        shipping_table.heading("BillingEmail", text="Billing email", anchor='w')
        shipping_table['show']='headings'

        #Treeview columns
        shipping_table.column("ShippingName", width=120, anchor='w')
        shipping_table.column("FirstName", width=120, anchor='w')
        shipping_table.column("LastName", width=120, anchor='w')
        shipping_table.column("Address1", width=200, anchor='w')
        shipping_table.column("Address2", width=200, anchor='w')
        shipping_table.column("City", width=80, anchor='w')
        shipping_table.column("Province", width=80, anchor='w')
        shipping_table.column("ZipCode", width=80, anchor='w')
        shipping_table.column("Country", width=80, anchor='w')
        shipping_table.column("PhoneNo", width=100, anchor='w')
        shipping_table.column("Email", width=200, anchor='w')
        shipping_table.column("BillingSame?", width=150, anchor='center')
        shipping_table.column("BillingFirstName", width=170, anchor='w')
        shipping_table.column("BillingLastName", width=170, anchor='w')
        shipping_table.column("BillingAddress1", width=200, anchor='w')
        shipping_table.column("BillingAddress2", width=200, anchor='w')
        shipping_table.column("BillingCity", width=100, anchor='w')
        shipping_table.column("BillingProvince", width=140, anchor='w')
        shipping_table.column("BillingZipCode", width=140, anchor='w')
        shipping_table.column("BillingCountry", width=140, anchor='w')
        shipping_table.column("BillingPhoneNo", width=140, anchor='w')
        shipping_table.column("BillingEmail", width=200, anchor='w')
        shipping_table.pack(fill=BOTH, expand=1)

    #==== Shipping buttons =====#

        def createShippingTask():
            # print("Shipping created")

            #Makes sure user enters detail right
            CreateShippingConfirmMsgBox = tkinter.messagebox.askquestion("Create shipping", "Are you sure all entry is correct?")

            if CreateShippingConfirmMsgBox == "yes":

                #Get all values for shipping
                ShippingNameVary = entry_shippingName.get()
                FirstNameVary = entry_shippingFirstName.get()
                LastNameVary = entry_shippingLastName.get()
                Address1Vary = entry_shippingAddress1.get()
                Address2Vary = entry_shippingAddress2.get()
                CityVary = entry_shippingCity.get()
                ProvinceVary = combo_shippingProvince.get()
                ZipCodeVary = entry_shippingZipCode.get()
                CountryVary = combo_shippingCountry.get()
                PhoneNoVary = entry_shippingPhoneNo.get()
                ShippingEmailVary = entry_shippingEmail.get()

                billingSameState = billingSameVar.get()

                if billingSameState == 0:
                    # print("Billing is not same as shipping")

                    #Assign the values for billing details from entry boxes
                    billingSameShippingVary = "X"
                    billingFirstNameVary = entry_billingFirstName.get()
                    billingLastNameVary = entry_billingLastName.get()
                    billingAddress1Vary = entry_billingAddress1.get()
                    billingAddress2Vary = entry_billingAddress2.get()
                    billingCityVary = entry_shippingCity.get()
                    billingProvinceStateVary = combo_billingProvince.get()
                    billingZipCodeVary = entry_billingZipCode.get()
                    billingCountryVary = combo_billingCountry.get()
                    billingPhoneNoVary = entry_billingPhoneNo.get()
                    billingShippingEmailVary = entry_billingEmail.get()

                elif billingSameState == 1:
                    # print("Billing is same as shipping")

                    #Assign the values for billing details from shipping values
                    billingSameShippingVary = "/"
                    billingFirstNameVary = FirstNameVary
                    billingLastNameVary = LastNameVary
                    billingAddress1Vary = Address1Vary
                    billingAddress2Vary = Address2Vary
                    billingCityVary = CityVary
                    billingProvinceStateVary = ProvinceVary
                    billingZipCodeVary = ZipCodeVary
                    billingCountryVary = CountryVary
                    billingPhoneNoVary = PhoneNoVary
                    billingShippingEmailVary = ShippingEmailVary

                #Write to CSV file
                with open('shipping.csv', 'a') as csvfile:
                    writer = csv.writer(csvfile, lineterminator = '\r')
                    writer.writerow([ShippingNameVary, FirstNameVary, LastNameVary, Address1Vary, Address2Vary, CityVary, ProvinceVary, ZipCodeVary, CountryVary, PhoneNoVary, ShippingEmailVary, billingSameShippingVary, billingFirstNameVary, billingLastNameVary, billingAddress1Vary, billingAddress2Vary, billingCityVary, billingProvinceStateVary, billingZipCodeVary, billingCountryVary, billingPhoneNoVary, billingShippingEmailVary])

                shipping_table.insert('', 'end', values=(ShippingNameVary, FirstNameVary, LastNameVary, Address1Vary, Address2Vary, CityVary, ProvinceVary, ZipCodeVary, CountryVary, PhoneNoVary, ShippingEmailVary, billingSameShippingVary, billingFirstNameVary, billingLastNameVary, billingAddress1Vary, billingAddress2Vary, billingCityVary, billingProvinceStateVary, billingZipCodeVary, billingCountryVary, billingPhoneNoVary, billingShippingEmailVary))

                #Log task
                create_shipping_now = datetime.now()
                create_shipping_time = create_shipping_now.strftime("[%H:%M:%S]")
                logging_table.insert('', 'end', values=[create_shipping_time + " - Address created"])

        btn_createProf = Button(shippingButtonFrame, text="➕ Create", command = createShippingTask, font=('URW Gothic L', '10','bold'), bg="IndianRed2", activebackground="IndianRed1", width=15, height=2)
        btn_createProf.grid(row=0, column=0, pady=5, padx=10, sticky='W')

        def updateShippingTask():
            # print("Shipping updated")
            update_shipping_now = datetime.now()
            update_shipping_time = update_shipping_now.strftime("[%H:%M:%S]")
            logging_table.insert('', 'end', values=[update_shipping_time + " - Addresses updated"])

            #Clears table
            for b in shipping_table.get_children():
                shipping_table.delete(b)

            #Clears arrays
            del shippingNameArray[:]
            del shippingFirstNameArray[:]
            del shippingLastNameArray[:]
            del shippingAddress1Array[:]
            del shippingAddress2Array[:]
            del shippingCityArray[:]
            del shippingProvinceStateArray[:]
            del shippingZipCodeArray[:]
            del shippingCountryArray[:]
            del shippingPhoneNoArray[:]
            del shippingEmailArray [:]

            del billingSameShippingArray[:]
            del billingNameArray[:]
            del billingFirstNameArray[:]
            del billingLastNameArray[:]
            del billingAddress1Array[:]
            del billingAddress2Array[:]
            del billingCityArray[:]
            del billingProvinceStateArray[:]
            del billingZipCodeArray[:]
            del billingCountryArray[:]
            del billingPhoneNoArray[:]
            del billingEmailArray [:]

            #Open csv file to read
            with open('shipping.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)

                #Reads values, appends to arrays and insert into table
                for row in reader:
                    
                #Get values from csv file
                    shippingNameValue = row[0]
                    FirstNameValue = row[1]
                    LastNameValue = row[2]
                    Address1Value = row[3]
                    Address2Value = row[4]
                    CityValue = row[5]
                    ProvinceValue = row[6]
                    ZipCodeValue = row[7]
                    CountryValue = row[8]
                    PhoneNoValue = row[9]
                    ShippingEmailValue = row[10]
                    billingSameShippingValue = row[11]
                    billingFirstNameValue = row[12]
                    billingLastNameValue = row[13]
                    billingAddress1Value = row[14]
                    billingAddress2Value = row[15]
                    billingCityValue = row[16]
                    billingProvinceStateValue = row[17]
                    billingZipCodeValue = row[18]
                    billingCountryValue = row[19]
                    billingPhoneNoValue = row[20]
                    billingShippingEmailValue = row[21]

                #Append to arrays
                    shippingNameArray.append(shippingNameValue)
                    shippingFirstNameArray.append(FirstNameValue)
                    shippingLastNameArray.append(LastNameValue)
                    shippingAddress1Array.append(Address1Value)
                    shippingAddress2Array.append(Address2Value)
                    shippingCityArray.append(CityValue)
                    shippingProvinceStateArray.append(ProvinceValue)
                    shippingZipCodeArray.append(ZipCodeValue)
                    shippingCountryArray.append(CountryValue)
                    shippingPhoneNoArray.append(PhoneNoValue)
                    shippingEmailArray.append(ShippingEmailValue)
                    billingSameShippingArray.append(billingSameShippingValue)
                    billingFirstNameArray.append(billingFirstNameValue)
                    billingLastNameArray.append(billingLastNameValue)
                    billingAddress1Array.append(billingAddress1Value)
                    billingAddress2Array.append(billingAddress2Value)
                    billingCityArray.append(billingCityValue)
                    billingProvinceStateArray.append(billingProvinceStateValue)
                    billingZipCodeArray.append(billingZipCodeValue)
                    billingCountryArray.append(billingCountryValue)
                    billingPhoneNoArray.append(billingPhoneNoValue)
                    billingEmailArray.append(billingShippingEmailValue)

                    shipping_table.insert('', 'end', values=(shippingNameValue, FirstNameValue, LastNameValue, Address1Value, Address2Value, CityValue, ProvinceValue, ZipCodeValue, CountryValue, PhoneNoValue, ShippingEmailValue, billingSameShippingValue, billingFirstNameValue, billingLastNameValue, billingAddress1Value, billingAddress2Value, billingCityValue, billingProvinceStateValue, billingZipCodeValue, billingCountryValue, billingPhoneNoValue, billingShippingEmailValue))

        btn_updateProf = Button(shippingButtonFrame, text="↑ Update", command = updateShippingTask, font=('URW Gothic L', '10','bold'), bg="IndianRed2", activebackground="IndianRed1", width=15, height=2)
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

        optionsFrame = Frame(SettingsTab, bg="black", highlightcolor="white", highlightthickness=3)

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
