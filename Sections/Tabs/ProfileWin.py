import tkinter as tk
import tkinter.messagebox
from tkinter import *
from tkinter import ttk

root = tk.Tk()
root.title("Profiles")
root.geometry("1000x600")
root.configure(bg="black")

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

#======= Frames =======#
createProfileFrame = Frame(root, bd=1, bg="black")
createProfileFrame.place(x=10, y=10, width=980, height=350)

displayProfileFrame = Frame(root, bd=1, bg="black")
displayProfileFrame.place(x=10, y=370, width=980, height=220)

nameLogInFrame = Frame(createProfileFrame, bd=1, bg="black")
nameLogInFrame.place(x=10, y=10, width=300, height=150)

cardInfoFrame = Frame(createProfileFrame, bd=1, bg="black")
cardInfoFrame.place(x=10, y=170, width=300, height=170)

addressFrame = Frame(createProfileFrame, bd=1, bg="black")
addressFrame.place(x=320, y=10, width=650, height=275)

buttonFrame = Frame(createProfileFrame, bd=1, bg="black")
buttonFrame.place(x=620, y=295, width=350, height=45)

profileDisTitle = Label(nameLogInFrame, text="Profile name", font=("times new roman", 13, "bold"), fg = "red", bg="black")
profileDisTitle.grid(row=1, column=0, columnspan=2, pady=3, padx=10, sticky='W')

#Profile name
lbl_profileName = Label(nameLogInFrame, text="Profile name", fg = "white", bg="black")
lbl_profileName.grid(row=2, column=0, pady=3, padx=10, sticky="W")
entry_profileName = Entry(nameLogInFrame, font=("times new roman", 10, "normal"), width=30)
entry_profileName.grid(row=2, column=1, pady=3, padx=10, sticky="w")

#======= Log in details =======#
logInTitle = Label(nameLogInFrame, text="Log-in details", font=("times new roman", 13, "bold"), fg = "red", bg="black")
logInTitle.grid(row=3, column=0, columnspan=2, pady=3, padx=10, sticky='W')

#Email
lbl_email = Label(nameLogInFrame, text="Email", fg = "white", bg="black")
lbl_email.grid(row=4, column=0, pady=3, padx=10, sticky="W")
entry_email = Entry(nameLogInFrame, font=("times new roman", 10, "normal"), width=30)
entry_email.grid(row=4, column=1, pady=3, padx=10, sticky="w")

#Password
lbl_password = Label(nameLogInFrame, text="Password", fg = "white", bg="black")
lbl_password.grid(row=5, column=0, pady=3, padx=10, sticky="W")
entry_password = Entry(nameLogInFrame, font=("times new roman", 10, "normal"), width=30)
entry_password.grid(row=5, column=1, pady=3, padx=10, sticky="w")

# #======= Shipping details =======#
shippingTitle = Label(addressFrame, text="Shipping details", font=("times new roman", 13, "bold"), fg = "red", bg="black")
shippingTitle.grid(row=1, column=0, columnspan=2, pady=2, padx=10, sticky='W')

# #First name
lbl_firstName = Label(addressFrame, text="First name", fg = "white", bg="black")
lbl_firstName.grid(row=2, column=0, pady=3, padx=10, sticky="W")
entry_firstName = Entry(addressFrame, font=("times new roman", 10, "normal"), width=21)
entry_firstName.grid(row=2, column=1, pady=3, padx=10, sticky="w")

# #Last name
lbl_lastName = Label(addressFrame, text="Last name", fg = "white", bg="black")
lbl_lastName.grid(row=2, column=2, pady=5, padx=10, sticky="W")
entry_lastName = Entry(addressFrame, font=("times new roman", 10, "normal"), width=21)
entry_lastName.grid(row=2, column=3, pady=5, padx=10, sticky="w")

# #Address 1
lbl_address1 = Label(addressFrame, text="Address 1", fg = "white", bg="black")
lbl_address1.grid(row=3, column=0, pady=3, padx=10, sticky="W")
entry_address1 = Entry(addressFrame, font=("times new roman", 10, "normal"), width=80)
entry_address1.grid(row=3, column=1, columnspan=4, pady=3, padx=10, sticky="w")

# #Address 2
lbl_address2 = Label(addressFrame, text="Address 2", fg = "white", bg="black")
lbl_address2.grid(row=4, column=0, pady=5, padx=10, sticky="W")
entry_address2 = Entry(addressFrame, font=("times new roman", 10, "normal"), width=80)
entry_address2.grid(row=4, column=1, columnspan=4, pady=5, padx=10, sticky="w")

# #City
lbl_city = Label(addressFrame, text="City", fg = "white", bg="black")
lbl_city.grid(row=5, column=0, pady=5, padx=10, sticky="W")
entry_city = Entry(addressFrame, font=("times new roman", 10, "normal"), width=21)
entry_city.grid(row=5, column=1, pady=5, padx=10, sticky="w")

# #Zipcode
lbl_zipcode = Label(addressFrame, text="Zipcode", fg = "white", bg="black")
lbl_zipcode.grid(row=6, column=0, pady=5, padx=10, sticky="W")
entry_zipcode = Entry(addressFrame, font=("times new roman", 10, "normal"), width=21)
entry_zipcode.grid(row=6, column=1, pady=5, padx=10, sticky="w")

# #Province
lbl_province = Label(addressFrame, text="Province", fg = "white", bg="black")
lbl_province.grid(row=7, column=0, pady=5, padx=10, sticky="W")
combo_province = ttk.Combobox(addressFrame, width=18)
combo_province['values']=('Bangkok', 'Chiang mai', 'Chiang rai', 'Pattaya')
combo_province.grid(row=7, column=1, pady=5, padx=10, sticky="w")

# #Country
lbl_country = Label(addressFrame, text="Country", fg = "white", bg="black")
lbl_country.grid(row=8, column=0, pady=5, padx=10, sticky="W")
combo_country = ttk.Combobox(addressFrame, width=18)
combo_country['values']=('Thailand')
combo_country.grid(row=8, column=1, pady=5, padx=10, sticky="w")

# #Phone number
lbl_phoneNumber = Label(addressFrame, text="Phone No.", fg = "white", bg="black")
lbl_phoneNumber.grid(row=9, column=0, pady=5, padx=10, sticky="W")
entry_phoneNumber = Entry(addressFrame, font=("times new roman", 10, "normal"), width=21)
entry_phoneNumber.grid(row=9, column=1, pady=5, padx=10, sticky="w")

# #======= Card details =======#
shippingTitle = Label(cardInfoFrame, text="Card details", font=("times new roman", 13, "bold"), fg = "red", bg="black")
shippingTitle.grid(row=1, column=0, columnspan=2, pady=2, padx=10, sticky='W')

lbl_cardNumber = Label(cardInfoFrame, text="Card No.", fg = "white", bg="black")
lbl_cardNumber.grid(row=2, column=0, pady=5, padx=10, sticky="W")
entry_cardNumber = Entry(cardInfoFrame, font=("times new roman", 10, "normal"), width=21)
entry_cardNumber.grid(row=2, column=1, pady=5, padx=10, sticky="w")

lbl_expMonth = Label(cardInfoFrame, text="Exp. month", fg = "white", bg="black")
lbl_expMonth.grid(row=3, column=0, pady=5, padx=10, sticky="W")
combo_expMonth = ttk.Combobox(cardInfoFrame, width=18)
combo_expMonth['values']=('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
combo_expMonth.grid(row=3, column=1, pady=5, padx=10, sticky="w")

lbl_expYear = Label(cardInfoFrame, text="Exp. year", fg = "white", bg="black")
lbl_expYear.grid(row=4, column=0, pady=5, padx=10, sticky="W")
combo_expYear = ttk.Combobox(cardInfoFrame, width=18)
combo_expYear['values']=('2021', '2022', '2023', '2024', '2025', '2026')
combo_expYear.grid(row=4, column=1, pady=5, padx=10, sticky="w")

lbl_CVV = Label(cardInfoFrame, text="CVV", fg = "white", bg="black")
lbl_CVV.grid(row=5, column=0, pady=5, padx=10, sticky="W")
entry_CVV = Entry(cardInfoFrame, font=("times new roman", 10, "normal"), width=21)
entry_CVV.grid(row=5, column=1, pady=5, padx=10, sticky="w")

#======= Table to display profiles =======#
style = ttk.Style()

scroll_x = Scrollbar(displayProfileFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(displayProfileFrame, orient=VERTICAL)
profile_table = ttk.Treeview(displayProfileFrame, columns=("ProfileName", "Email", "Password", "CardNo", "ExpMonth", "ExpYear", "CVV", "FirstName", "LastName", "Address1", "Address2", "City", "ZipCode", "Province", "Country", "PhoneNo"), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
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
profile_table.heading("ExpYear", text="Exp. date")
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
profile_table.column("ProfileName", width=75)
profile_table.column("Email", width=175)
profile_table.column("Password", width=90)
profile_table.column("CardNo", width=120)
profile_table.column("ExpMonth", width=75)
profile_table.column("ExpYear", width=60)
profile_table.column("CVV", width=30)
profile_table.column("FirstName", width=80)
profile_table.column("LastName", width=80)
profile_table.column("Address1", width=200)
profile_table.column("Address2", width=150)
profile_table.column("City", width=80)
profile_table.column("ZipCode", width=55)
profile_table.column("Province", width=80)
profile_table.column("Country", width=80)
profile_table.column("PhoneNo", width=100)
profile_table.pack(fill=BOTH, expand=1)

#======= Buttons to create and delete task =======#

# #Create button

def createProfileTask():
    #print("Profile created")

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

btn_createProf = Button(buttonFrame, text="Create", command = createProfileTask, width=20, border=4)
btn_createProf.grid(row=0, column=0, pady=5, padx=10, sticky='W')

# #Delete button

def deleteProfileTask():
    #print("Profile deleted")

    #Message box to confirm is user really wants to delete tasks
    deleteProfMsgBox = tkinter.messagebox.askquestion("Confirm","Are you sure you want to delete this profile?")

    if deleteProfMsgBox == 'yes':
        selectedTask = profile_table.selection()[0]
        profile_table.delete(selectedTask)


btn_deleteProf = Button(buttonFrame, text="Delete", command = deleteProfileTask, width=20, border=4)
btn_deleteProf.grid(row=0, column=1, pady=5, padx=10, sticky='W')

root.mainloop()