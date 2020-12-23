import tkinter as tk
import tkinter.messagebox
from tkinter import *
from tkinter import ttk

settings = tk.Tk()
settings.title("Setting")
settings.geometry("1000x600")
settings.configure(bg="black")

#======= Frames =======#
accountFrame = Frame(settings, bg="black")
accountFrame.place(x=0, y=0, width=1000, height=150)

notificationFrame = Frame(settings, bg="black")
notificationFrame.place(x=0, y=150, width=1000, height=150)

backUpFrame = Frame(settings, bg="black")
backUpFrame.place(x=0, y=300, width=1000, height=150)

versionFrame = Frame(settings, bg="black")
versionFrame.place(x=0, y=450, width=1000, height=150)

#======= Account =======#
lbl_accountTitle = Label(accountFrame, text = "Accounts", font=("times new roman", 24, "normal"), fg="white", bg="black")
lbl_accountTitle.grid(row=1, column=1, padx=5)

#======= Notifications =======#
lbl_notificationsTitle = Label(notificationFrame, text = "Notifications", font=("times new roman", 24, "normal"), fg="white", bg="black")
lbl_notificationsTitle.grid(row=1, column=1, padx=5)

#======= Back up =======# #Might delete soon
lbl_backUpTitle = Label(backUpFrame, text = "Back up", font=("times new roman", 24, "normal"), fg="white", bg="black")
lbl_backUpTitle.grid(row=1, column=1, padx=5)

#======= Version =======#
lbl_versionTitle = Label(versionFrame, text = "Version", font=("times new roman", 24, "normal"), fg="white", bg="black")
lbl_versionTitle.grid(row=1, column=1, padx=5, sticky="w")

lbl_versionTitle = Label(versionFrame, text = "Version 0.0.1", font=("times new roman", 15, "normal"), fg="white", bg="black")
lbl_versionTitle.grid(row=2, column=1, columnspan=2, padx=5)

settings.mainloop()