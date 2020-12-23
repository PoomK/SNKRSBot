import sys, os
import csv
import tkinter as tk
from tkinter import *
from tkinter import ttk
import time

root = tk.Tk()
root.title("Widget test")
root.geometry("1000x600")
root.configure(background="black")

nameVar = StringVar()
numberVar = StringVar()

entry_name = Entry(root)
entry_name.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

entry_number = Entry(root)
entry_number.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

treeviewFrame = Frame(root, bg="white")
treeviewFrame.place(x=10, y=100, width=500, height=300)

scroll_y = Scrollbar(treeviewFrame, orient=VERTICAL)
name_table = ttk.Treeview(treeviewFrame, columns=('Name', 'number'), yscrollcommand=scroll_y.set)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=name_table.yview)

name_table.heading("Name", text="Name")
name_table.heading("number", text="Number")
name_table['show']='headings'

name_table.column("Name", anchor='center')
name_table.column("number", anchor='center')
name_table.pack(fill=BOTH, expand=1)

nameArray = []
numberArray = []

# with open("names.csv", "w+") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["Name", "Number"])

def addName():
    
    nameVary = entry_name.get()
    numberVary = entry_number.get()

    with open('names.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, lineterminator='\r')
        writer.writerow([nameVary, numberVary])

    name_table.insert('', 'end', values=(nameVary, numberVary))

btn_add = Button(root, text="add", command=addName)
btn_add.grid(row=2, column=0, padx=5, pady=5)

def deleteName():
    #print("nameDeleted")

    selected_item = name_table.selection()[0]
    name_table.delete(selected_item)


btn_delete = Button(root, text="delete", command=deleteName)
btn_delete.grid(row=2, column=1, padx=5, pady=5)

def updateName():

    for a in name_table.get_children():
        name_table.delete(a)

    del nameArray[:]
    del numberArray[:]

    with open('names.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)

        for line in reader:
            name = line[0]
            number = line[1]

            nameArray.append(name)
            #print(nameArray)
            numberArray.append(number)
            #print(numberArray)

            name_table.insert('', 'end', values=(name, number))
            

btn_update = Button(root, text="update", command=updateName)
btn_update.grid(row=2, column=2, padx=5, pady=5)

def editName():
    # print("name edited")
    entry_name.insert(0, "Teddy")

    with open('names.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)

btn_edit = Button(root, text="edit", command=editName)
btn_edit.grid(row=2, column=3, padx=5, pady=5)

def saveName():
    print("name saved")

btn_save = Button(root, text="save", command=saveName)
btn_save.grid(row=2, column=4, padx=5, pady=5)

root.mainloop()