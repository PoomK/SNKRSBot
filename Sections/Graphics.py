#========== Setting up ==========#
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import logging

root = tk.Tk()
root.title("SNKRS Bot")
root.geometry("1300x845")
root.resizable(width=0, height=0)

#========== Styling ==========#
style = ttk.Style()

style.configure('TNotebook.Tab', font=('URW Gothic L', '20','bold'))
style.configure('TNotebook', background='black')
style.configure('TFrame', background='black')
style.configure("Treeview.Heading", background='gray24', foreground='black', font=('URW Gothic L', '13', 'bold'))
style.configure("Treeview", background='gray90', font=('URW Gothic L', '10', 'normal') )

#========== Tab control ==========#
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

#========== Task Tab ==========#
class TaskTab():
    def __init__(self, TasksTab):
    
    #===== All Variables =====#
        self.taskNameVar = StringVar()
        self.siteNameVar = StringVar()
        self.linkVar = StringVar()
        self.sizeChoiceVar = StringVar()
        self.proxyVar = StringVar()
        self.profileVar = StringVar()
        self.taskQuantityVar = StringVar()
        
    #===== Frames =====#
        #Frame for title bar
        TaskTitleBarFrame = Frame(TasksTab, bd=1, bg='black')
        TaskTitleBarFrame.place(x=0, y=0, width=1300, height=75)

        #Frame for inputs, create task, logging
        CreateActionTaskFrame = Frame(TasksTab, bd=1, bg='black')
        CreateActionTaskFrame.place(x=0, y=75, width=375, height=725)

        btnFrame = Frame(CreateActionTaskFrame, bd=1, bg="black")
        btnFrame.place(x=0, y=320, width=320, height=45)

        loggingTitleFrame = Frame(CreateActionTaskFrame, bd=1, bg="black")
        loggingTitleFrame.place(x=0, y=367, width=320, height=45)

        loggingFrame = Frame(CreateActionTaskFrame, bd=1, bg="white")
        loggingFrame.place(x=10, y=410, width=345, height=305)

        #Frame for treeview and Start task actions
        DisplayTaskFrame = Frame(TasksTab, bd=1, bg='black')
        DisplayTaskFrame.place(x=370, y=75, width=980, height=725)

        TaskTableFrame = Frame(DisplayTaskFrame, bg="white")
        TaskTableFrame.place(x=7, y=10, width=910, height=650)

        TaskButtonActionFrame = Frame(DisplayTaskFrame, bg="black")
        TaskButtonActionFrame.place(x=7, y=670, width=960, height=45)

    #===== Title bar =====#
        lbl_TaskTabTitle = Label(TaskTitleBarFrame, text="SNKRS Bot", font=('FixedSYS', '50','bold'), fg='deep sky blue', bg='Black')
        lbl_TaskTabTitle.grid(row=1, column=1, padx=5)

    #===== Create task =====#
        createTaskTitle = Label(CreateActionTaskFrame, text="Create task", font=("URW Gothic L", 20, "bold"), fg='red', bg="black")
        createTaskTitle.grid(row=0, columnspan=2)

        lbl_taskName = Label(CreateActionTaskFrame, text="Task Name", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_taskName.grid(row=1, column=0, pady=5, padx=10, sticky="W")
        entry_taskName = Entry(CreateActionTaskFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=21)
        entry_taskName.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        lbl_siteName = Label(CreateActionTaskFrame, text="Site Name", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_siteName.grid(row=2, column=0, pady=5, padx=10, sticky="W")
        combo_siteName = ttk.Combobox(CreateActionTaskFrame, font=("URW Gothic L", 12, "normal"), width=15)
        combo_siteName['values']=('Nike TH', 'Nike US')
        combo_siteName.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        lbl_link = Label(CreateActionTaskFrame, text="Link", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_link.grid(row=3, column=0, pady=5, padx=10, sticky="w")
        entry_link = Entry(CreateActionTaskFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=21)
        entry_link.grid(row=3, column=1, pady=5, padx=10)

        lbl_sizeChoice = Label(CreateActionTaskFrame, text="Size", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_sizeChoice.grid(row=4, column=0, pady=5, padx=10, sticky="w")
        combo_sizeChoice = ttk.Combobox(CreateActionTaskFrame, font=("URW Gothic L", 12, "normal"), textvariable="", width=10)
        combo_sizeChoice['values']=('EU 37.5','EU 38', 'EU 38.5', 'EU 39','EU 40', 'EU 40.5', 'EU 41', 'EU 42', 'EU 42.5', 'EU 43', 'EU 44')
        combo_sizeChoice.grid(row=4, column=1, pady=5, padx=10, sticky="w")

        lbl_proxy = Label(CreateActionTaskFrame, text="Proxy", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_proxy.grid(row=5, column=0, pady=5, padx=10, sticky="w")
        #Need to add tab for user to enter profiles to save to file
        combo_proxy = ttk.Combobox(CreateActionTaskFrame, font=("URW Gothic L", 12, "normal"), textvariable="", width=10)
        combo_proxy['values']=('none','proxy1')
        combo_proxy.grid(row=5, column=1, pady=5, padx=10, sticky="w")

        lbl_profile = Label(CreateActionTaskFrame, text="Profile", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_profile.grid(row=6, column=0, pady=5, padx=10, sticky="w")
        #Need to add tab for user to enter profiles to save to file
        combo_profile = ttk.Combobox(CreateActionTaskFrame, font=("URW Gothic L", 12, "normal"), textvariable="", width=10)
        combo_profile['values']=('Profile1', 'Profile2', 'Profile3', 'Profile4')
        combo_profile.grid(row=6, column=1, pady=5, padx=10, sticky="w")

        lbl_taskQuantity = Label(CreateActionTaskFrame, text="Task Quantity", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_taskQuantity.grid(row=7, column=0, pady=5, padx=10, sticky="W")
        entry_taskQuantity = Entry(CreateActionTaskFrame, textvariable="", font=("URW Gothic L", 12, "normal"), fg='black', width=21)
        entry_taskQuantity.grid(row=7, column=1, pady=5, padx=10, sticky="w")

    #===== Logging =====#
        loggingTitle = Label(loggingTitleFrame, text="Log", font=('URW Gothic L', '20','bold'), fg='Red', bg='black')
        loggingTitle.grid(row=0, column=0, padx=7)

        scroll_y = Scrollbar(loggingFrame, orient=VERTICAL)
        logging_table = ttk.Treeview(loggingFrame, columns=("Action"), yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=logging_table.yview)

    #===== Display task + Start task buttons =====#

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
        task_table.column("SiteName", width=100, anchor='center')
        task_table.column("TaskName", width=100, anchor='center')
        task_table.column("Profile", width=100, anchor='center')
        task_table.column("Link", width=355, anchor='center')
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
                    profileVar = combo_profile.get()

                    startButton = Button(DisplayTaskFrame, text="Hello")

                    logging.info("Hello")

                    task_table.insert('', 'end', values=(self.i, siteNameVar, taskNameVar, profileVar, linkVar, sizeVar, proxyVar))

                    self.i = self.i + 1

        createTaskBtn = Button(btnFrame, text="Create", command=CreateTaskCommand, font=('URW Gothic L', '10','bold'), bg="IndianRed2", activebackground="IndianRed1", width=9, height=2)
        createTaskBtn.grid(row=0, column=0, padx=10)

    #===== Task action frame =====#
    
        StartAllTaskBtn = Button(TaskButtonActionFrame, text="Start all", font=('URW Gothic L', '10','bold'), bg="IndianRed2", activebackground="IndianRed1", width=20, height=2)
        StartAllTaskBtn.grid(row=0, column=0, padx=0)

        StartTaskBtn = Button(TaskButtonActionFrame, text="Start", font=('URW Gothic L', '10','bold'), bg="IndianRed2", activebackground="IndianRed1", width=20, height=2)
        StartTaskBtn.grid(row=0, column=1, padx=24)

        # def DeleteTaskCommand():
        #     print("Task deleted")

        #     selectedTask = task_table.selection()[0]
        #     task_table.delete(selectedTask)

        # deleteTaskBtn = Button(TaskButtonActionFrame, text="Delete", command=DeleteTaskCommand, font=('URW Gothic L', '10','bold'), bg="IndianRed2", activebackground="IndianRed1", width=20, height=2)
        # deleteTaskBtn.grid(row=0, column=2, padx=0)

        def ClearTaskCommand():
            print("Tasks cleared")

            #Message box to confirm is user really wants to delete tasks
            clearTaskMsgBox = tkinter.messagebox.askquestion("Confirm","Are you sure you want to delete all tasks?")

            if clearTaskMsgBox == 'yes':
                for a in task_table.get_children():
                    task_table.delete(a)
                self.i = 1

        clearTaskBtn = Button(TaskButtonActionFrame, text="Clear", command=ClearTaskCommand, font=('URW Gothic L', '10','bold'), bg="IndianRed2", activebackground="IndianRed1", width=20, height=2)
        clearTaskBtn.grid(row=0, column=3, padx=0)

ab = TaskTab(TasksTab)

#========== Profle Tab ==========#
class ProfileTab():
    def __init__(self, ProfileTab):

    #===== All Variables =====#

    #===== Frames =====#
        ProfileTitleBarFrame = Frame(ProfilesTab, bd=1, bg='black')
        ProfileTitleBarFrame.place(x=0, y=0, width=1300, height=75)

        CreateProfileFrame = Frame(ProfilesTab, bd=1, bg="black")
        CreateProfileFrame.place(x=0, y=75, width=1300, height=400)

        DisplayProfileFrame = Frame(ProfilesTab,bg="black")
        DisplayProfileFrame.place(x=10, y=435, width=1280, height=355)

    #===== Title bar =====#
        lbl_ProfileTabTitle = Label(ProfileTitleBarFrame, text="SNKRS Bot", font=('FixedSYS', '50','bold'), fg='deep sky blue', bg='Black')
        lbl_ProfileTabTitle.grid(row=1, column=1, padx=5)

    #======= Variables =======#
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
        buttonFrame.place(x=375, y=295, width=700, height=60)

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

        # #======= Shipping details =======#
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

        # #======= Card details =======#
        shippingTitle = Label(cardInfoFrame, text="Card details", font=("URW Gothic L", 20, "bold"), fg='red', bg="black")
        shippingTitle.grid(row=1, column=0, columnspan=2, pady=2, sticky='W')

        lbl_cardNumber = Label(cardInfoFrame, text="Card No.", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_cardNumber.grid(row=2, column=0, sticky="W")
        entry_cardNumber = Entry(cardInfoFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=21)
        entry_cardNumber.grid(row=2, column=1, padx=10, sticky="w")

        lbl_expMonth = Label(cardInfoFrame, text="Exp. month", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_expMonth.grid(row=3, column=0, sticky="W")
        combo_expMonth = ttk.Combobox(cardInfoFrame, width=18, font=("URW Gothic L", 12, "normal"))
        combo_expMonth['values']=('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
        combo_expMonth.grid(row=3, column=1, padx=10, sticky="w")

        lbl_expYear = Label(cardInfoFrame, text="Exp. year", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_expYear.grid(row=4, column=0, sticky="W")
        combo_expYear = ttk.Combobox(cardInfoFrame, width=18, font=("URW Gothic L", 12, "normal"))
        combo_expYear['values']=('2021', '2022', '2023', '2024', '2025', '2026')
        combo_expYear.grid(row=4, column=1, padx=10, sticky="w")

        lbl_CVV = Label(cardInfoFrame, text="CVV", font=("URW Gothic L", 15, "bold"), fg='white', bg="black")
        lbl_CVV.grid(row=5, column=0, sticky="W")
        entry_CVV = Entry(cardInfoFrame, font=("URW Gothic L", 12, "normal"), fg='black', width=21)
        entry_CVV.grid(row=5, column=1, padx=10, sticky="w")

        #======= Table to display profiles =======#
        style = ttk.Style()

        scroll_x = Scrollbar(DisplayProfileFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(DisplayProfileFrame, orient=VERTICAL)
        profile_table = ttk.Treeview(DisplayProfileFrame, columns=("ProfileName", "Email", "Password", "CardNo", "ExpMonth", "ExpYear", "CVV", "FirstName", "LastName", "Address1", "Address2", "City", "ZipCode", "Province", "Country", "PhoneNo"), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
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
        profile_table.column("Email", width=175, anchor='center')
        profile_table.column("Password", width=90, anchor='center')
        profile_table.column("CardNo", width=120, anchor='center')
        profile_table.column("ExpMonth", width=100, anchor='center')
        profile_table.column("ExpYear", width=90, anchor='center')
        profile_table.column("CVV", width=45, anchor='center')
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

        #======= Buttons to create and delete task =======#

        # #Create button

        def createProfileTask():
            #print("Profile created")

            CreateProfileConfirmMsgBox = tkinter.messagebox.askquestion("Create task", "Are you sure all entry is correct?")

            if CreateProfileConfirmMsgBox == "yes":

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

                profile_table.insert('', 'end', values=(profileNameVar, emailVar, passwordVar, cardNoVar, expMonthVar, expYearVar, CVVVar, firstNameVar, lastNameVar, address1Var, address2Var, cityVar, zipCodeVar, provinceVar, countryVar, phoneNoVar))

                entry_profileName.delete(0, END)
                entry_email.delete(0, END)
                entry_password.delete(0, END)

        btn_createProf = Button(buttonFrame, text="Create", command = createProfileTask, font=('URW Gothic L', '10','bold'), bg="IndianRed2", activebackground="IndianRed1", width=20, height=2)
        btn_createProf.grid(row=0, column=0, pady=5, padx=10, sticky='W')

        # #Delete button

        def deleteProfileTask():
            #print("Profile deleted")

            #Message box to confirm is user really wants to delete tasks
            deleteProfMsgBox = tkinter.messagebox.askquestion("Confirm","Are you sure you want to delete this profile?")

            if deleteProfMsgBox == 'yes':
                selectedTask = profile_table.selection()[0]
                profile_table.delete(selectedTask)


        btn_deleteProf = Button(buttonFrame, text="Delete", command = deleteProfileTask, font=('URW Gothic L', '10','bold'), bg="IndianRed2", activebackground="IndianRed1", width=20, height=2)
        btn_deleteProf.grid(row=0, column=1, pady=5, padx=10, sticky='W')

        def updateProfileTask():
            print("Profiles updated")

        btn_updateProf = Button(buttonFrame, text="Update", command = updateProfileTask, font=('URW Gothic L', '10','bold'), bg="IndianRed2", activebackground="IndianRed1", width=20, height=2)
        btn_updateProf.grid(row=0, column=2, pady=5, padx=10, sticky='W')

bc = ProfileTab(ProfilesTab)

#========== Proxy Tab ==========#
class ProxyTab():
    def __init__(self, proxiesTab):

    #===== All Variables =====#
        self.proxyNameVar = StringVar()
        self.IPVar = StringVar()
        self.PortVar = StringVar()
        self.UsernameVar = StringVar()
        self.PasswordVar = StringVar()
        self.StoreVar = StringVar()

    #===== Frames =====#
        ProxyTitleBarFrame = Frame(ProxiesTab, bd=1, bg='black')
        ProxyTitleBarFrame.place(x=0, y=0, width=1300, height=75)

    #===== Title bar =====#
        lbl_ProxyTabTitle = Label(ProxyTitleBarFrame, text="SNKRS Bot", font=('FixedSYS', '50','bold'), fg='deep sky blue', bg='Black')
        lbl_ProxyTabTitle.grid(row=1, column=1, padx=5)

de = ProxyTab(ProxiesTab)

#========== Settings Tab ==========#
class SettingTab():
    def __init__(self, settingsTab):

    #===== Frames =====#
        SettingsTitleBarFrame = Frame(SettingsTab, bd=1, bg='black')
        SettingsTitleBarFrame.place(x=0, y=0, width=1300, height=75)

        AccountsFrame = Frame(SettingsTab, bg='red')
        AccountsFrame.place(x=0, y=75, width=1300, height=200)

        NotificationFrame = Frame(SettingsTab, bg="green")
        NotificationFrame.place(x=0, y=275, width=1300, height=200)

    #===== Title bar =====#
        lbl_TitleTabTitle = Label(SettingsTitleBarFrame, text="SNKRS Bot", font=('FixedSYS', '50','bold'), fg='deep sky blue', bg='Black')
        lbl_TitleTabTitle.grid(row=1, column=1, padx=5)

    #===== Notifications =====#

fg = SettingTab(SettingsTab)

root.mainloop()