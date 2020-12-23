import tkinter as tk
import tkinter.messagebox
from tkinter import *
from tkinter import ttk

root = tk.Tk()
root.title("Proxy")
root.geometry("1000x600")
root.configure(bg="black")

#======= Variables =======#
proxyNameVar = StringVar()
IPVar = StringVar()
PortVar = StringVar()
UsernameVar = StringVar()
PasswordVar = StringVar()
StoreVar = StringVar()

#======= Frames =======#
addProxyFrame = Frame(root, bd=1, bg = "black")
addProxyFrame.place(x=10, y=10, width=980, height=200)

displayProxyFrame = Frame(root, bd=1, bg="black")
displayProxyFrame.place(x=10, y=220, width=980, height=370)

buttonFrame = Frame(addProxyFrame, bd=1, bg="black")
buttonFrame.place(x=620, y=145, width=350, height=45)

#======= Input =======#
#Proxy name
lbl_proxyName = Label(addProxyFrame, text="Proxy name", fg = "white", bg="black")
lbl_proxyName.grid(row=0, column=0, pady=3, padx=10, sticky="W")
entry_proxyName = Entry(addProxyFrame, font=("times new roman", 10, "normal"), width=30)
entry_proxyName.grid(row=0, column=1, columnspan=3, pady=3, padx=10, sticky="w")

#IP
lbl_IP = Label(addProxyFrame, text="IP", fg = "white", bg="black")
lbl_IP.grid(row=1, column=0, pady=3, padx=10, sticky="W")
entry_IP = Entry(addProxyFrame, font=("times new roman", 10, "normal"), width=15)
entry_IP.grid(row=1, column=1, pady=3, padx=10, sticky="w")

#Port
lbl_port = Label(addProxyFrame, text="Port", fg = "white", bg="black")
lbl_port.grid(row=2, column=0, pady=3, padx=10, sticky="W")
entry_port = Entry(addProxyFrame, font=("times new roman", 10, "normal"), width=15)
entry_port.grid(row=2, column=1, pady=3, padx=10, sticky="w")

#Username
lbl_username = Label(addProxyFrame, text="Username", fg = "white", bg="black")
lbl_username.grid(row=3, column=0, pady=3, padx=10, sticky="W")
entry_username = Entry(addProxyFrame, font=("times new roman", 10, "normal"), width=30)
entry_username.grid(row=3, column=1, columnspan=3, pady=3, padx=10, sticky="w")

#Password
lbl_password = Label(addProxyFrame, text="Password", fg = "white", bg="black")
lbl_password.grid(row=4, column=0, pady=3, padx=10, sticky="W")
entry_password = Entry(addProxyFrame, font=("times new roman", 10, "normal"), width=30)
entry_password.grid(row=4, column=1, columnspan=3, pady=3, padx=10, sticky="w")

#Store
lbl_store = Label(addProxyFrame, text="Store", fg = "white", bg = "black")
lbl_store.grid(row=5, column=0, pady=3, padx=10, sticky="W")
combo_store = ttk.Combobox(addProxyFrame, width=18)
combo_store['values']=('Nike', 'Adidas')
combo_store.grid(row=5, column=1, pady=5, padx=10, sticky="w")

#======= Table =======#
#Headers: Name, IP, Port, username, password, status, actions

scroll_y = Scrollbar(displayProxyFrame, orient=VERTICAL)
proxy_table = ttk.Treeview(displayProxyFrame, columns=("ProxyName", "IP", "Port", "Username", "Password", "Store", "Status", "Actions"), yscrollcommand=scroll_y.set)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=proxy_table.yview)

#Treeview headings
proxy_table.heading("ProxyName", text="Proxy name")
proxy_table.heading("IP", text="IP")
proxy_table.heading("Port", text="Port")
proxy_table.heading("Username", text="Username")
proxy_table.heading("Password", text="Password")
proxy_table.heading("Store", text="Store")
proxy_table.heading("Status", text="Status")
proxy_table.heading("Actions", text="Actions")
proxy_table['show']='headings'

#Treeview columns
proxy_table.column("ProxyName", width=75)
proxy_table.column("IP", width=120)
proxy_table.column("Port", width=75)
proxy_table.column("Username", width=75)
proxy_table.column("Password", width=75)
proxy_table.column("Store", width=75)
proxy_table.column("Status", width=75)
proxy_table.column("Actions", width=75)
proxy_table.pack(fill=BOTH, expand=1)

#======= Buttons =======#
def addProxy():

    proxyNameVar = entry_proxyName.get()
    IPVar = entry_IP.get()
    PortVar = entry_port.get()
    UsernameVar = entry_username.get()
    PasswordVar = entry_password.get()
    StoreVar = combo_store.get()

    proxy_table.insert('', 'end', values=(proxyNameVar, IPVar, PortVar, UsernameVar, PasswordVar, StoreVar))

btn_createProf = Button(buttonFrame, text="Create", command=addProxy, width=20, border=4)
btn_createProf.grid(row=0, column=0, pady=5, padx=10, sticky='W')

def deleteProxyTask():

    #Message box to confirm is user really wants to delete proxy
    deleteProfMsgBox = tkinter.messagebox.askquestion("Confirm","Are you sure you want to delete this proxy?")

    if deleteProfMsgBox == 'yes':
        selectedTask = proxy_table.selection()[0]
        proxy_table.delete(selectedTask)

btn_deleteProf = Button(buttonFrame, text="Delete", command=deleteProxyTask, width=20, border=4)
btn_deleteProf.grid(row=0, column=1, pady=5, padx=10, sticky='W')

root.mainloop()