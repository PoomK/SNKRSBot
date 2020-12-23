import tkinter as tk
import tkinter.messagebox
from tkinter import *
from tkinter import ttk

class Sneaker:
    def __init__(self, root):
        self.root=root
        self.root.title("SNKRS Bot")
        self.root.geometry("1000x600")
        self.root.configure(bg = 'black')

    #======= All variables =======#
        self.taskNameVar = StringVar()
        self.linkVar = StringVar()
        self.sizeChoiceVar = StringVar()
        self.proxyVar = StringVar()
        self.profileVar = StringVar()
        self.taskQuantityVar = StringVar()

    #======= Create task frame =======#
        createTaskFrame = Frame(self.root, bd=1, bg="medium spring green")
        createTaskFrame.place(x=10, y=10, width=300, height=580)

        #=== Inputs ===# Max width = 25, BG = Medium sprint green, standard font size=15
        createTaskTitle = Label(createTaskFrame, text="Create tasks", font=("times new roman", 20, "bold"), bg="medium spring green")
        createTaskTitle.grid(row=0, columnspan=2)

        # lbl_taskID = Label(createTaskFrame, text="Task ID", bg="medium spring green", font=("times new roman", 15, "bold"))
        # lbl_taskID.grid(row=1, column=0, pady=5, padx=10, sticky="W")

        # entry_taskID = Entry(createTaskFrame, font=("times new roman", 10, "normal"), width=13)
        # entry_taskID.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        lbl_taskName = Label(createTaskFrame, text="Task Name", bg="medium spring green", font=("times new roman", 15, "bold"))
        lbl_taskName.grid(row=2, column=0, pady=5, padx=10, sticky="W")
        entry_taskName = Entry(createTaskFrame, textvariable=self.taskNameVar, font=("times new roman", 10, "normal"), width=21)
        entry_taskName.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        lbl_link = Label(createTaskFrame, text="Link", bg="medium spring green", font=("times new roman", 15, "bold"))
        lbl_link.grid(row=3, column=0, pady=5, padx=10, sticky="w")
        entry_link = Entry(createTaskFrame, font=("times new roman", 10, "normal"), width=21)
        entry_link.grid(row=3, column=1, pady=5, padx=10)

        lbl_sizeChoice = Label(createTaskFrame, text="Size", bg="medium spring green", font=("times new roman", 15, "bold"))
        lbl_sizeChoice.grid(row=4, column=0, pady=5, padx=10, sticky="w")
        combo_sizeChoice = ttk.Combobox(createTaskFrame, textvariable="", width=10)
        combo_sizeChoice['values']=('EU 37.5','EU 38', 'EU 38.5', 'EU 39','EU 40', 'EU 40.5', 'EU 41', 'EU 42', 'EU 42.5', 'EU 43', 'EU 44', 'S', 'M', 'L')
        combo_sizeChoice.grid(row=4, column=1, pady=5, padx=10, sticky="w")

        lbl_proxy = Label(createTaskFrame, text="Proxy", bg="medium spring green", font=("times new roman", 15, "bold"))
        lbl_proxy.grid(row=5, column=0, pady=5, padx=10, sticky="w")
        #Need to add tab for user to enter profiles to save to file
        combo_proxy = ttk.Combobox(createTaskFrame, textvariable="", width=10)
        combo_proxy['values']=('none','proxy1')
        combo_proxy.grid(row=5, column=1, pady=5, padx=10, sticky="w")

        lbl_profile = Label(createTaskFrame, text="Profile", bg="medium spring green", font=("times new roman", 15, "bold"))
        lbl_profile.grid(row=6, column=0, pady=5, padx=10, sticky="w")
        #Need to add tab for user to enter profiles to save to file
        combo_profile = ttk.Combobox(createTaskFrame, textvariable="", width=10)
        combo_profile['values']=('Profile1', 'Profile2', 'Profile3', 'Profile4')
        combo_profile.grid(row=6, column=1, pady=5, padx=10, sticky="w")

        lbl_taskQuantity = Label(createTaskFrame, text="Task Quantity", bg="medium spring green", font=("times new roman", 15, "bold"))
        lbl_taskQuantity.grid(row=7, column=0, pady=5, padx=10, sticky="W")
        entry_taskQuantity = Entry(createTaskFrame, textvariable=self.taskQuantityVar, font=("times new roman", 10, "normal"), width=21)
        entry_taskQuantity.grid(row=7, column=1, pady=5, padx=10, sticky="w")

    #======= Display task frame =======#
        displayTaskFrame = Frame(self.root, bd=1, bg="medium spring green")
        displayTaskFrame.place(x=320, y=10, width=670, height=580)

        createTaskTitle = Label(displayTaskFrame, text="Tasks", font=("times new roman", 20, "bold"), bg="medium spring green")
        createTaskTitle.grid(row=0, columnspan=2, padx=10)

    #======= Table frame within display task frame =======#
        tableFrame = Frame(displayTaskFrame, bg="medium spring green")
        tableFrame.place(x=10, y=35, width=650, height=530)

        #Styling treeview
        style = ttk.Style()

        # scroll_x = Scrollbar(tableFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(tableFrame, orient=VERTICAL)
        task_table = ttk.Treeview(tableFrame, columns=("ID", "TaskName", "Profile", "Link", "Size", "Proxy"), yscrollcommand=scroll_y.set)
        # scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        # scroll_x.config(command=task_table.xview)
        scroll_y.config(command=task_table.yview)
        
        #Treeview headings
        task_table.heading("ID", text="ID")
        task_table.heading("TaskName", text="Task name")
        task_table.heading("Profile", text="Profile")
        task_table.heading("Link", text="Link")
        task_table.heading("Size", text="Size")
        task_table.heading("Proxy", text="Proxy")
        task_table['show']='headings'

        #Treeview columns
        task_table.column("ID", width=30)
        task_table.column("TaskName", width=100)
        task_table.column("Profile", width=75)
        task_table.column("Link", width=290)
        task_table.column("Size", width=50)
        task_table.column("Proxy", width=75)
        task_table.pack(fill=BOTH, expand=1)

    #======= Button frame within create task frame =======#
        btnFrame = Frame(createTaskFrame, bd=1, bg="black")
        btnFrame.place(x=5, y=490, width=290, height=80)

        self.i=1

        def createTask():
            #print("task created")
            
            #Returns user the value of amount of tasks user wants to create
            taskQuantityVar = int(entry_taskQuantity.get())

            #For loop for entering value
            for b in range(taskQuantityVar):
                taskNameVar = entry_taskName.get()
                linkVar = entry_link.get()
                sizeVar = combo_sizeChoice.get()
                proxyVar = combo_proxy.get()
                profileVar = combo_profile.get()

                task_table.insert('', 'end', values=(self.i, taskNameVar, profileVar, linkVar, sizeVar, proxyVar))

                self.i = self.i + 1
        
        createBtn = Button(btnFrame, text = "create", command = createTask, width=10, height=4)
        createBtn.grid(row=1, column=0, padx=8, pady=3)

        #Function to delete currently selected task
        def deleteTask():
            #print("task deleted")

            selectedTask = task_table.selection()[0]
            task_table.delete(selectedTask)

        deleteBtn = Button(btnFrame, text = "delete", command = deleteTask, width=10, height=4)
        deleteBtn.grid(row=1, column=1, padx=8, pady=3)

        #Function to clear all tasks in the table
        def clearTask():
            #print("tasks cleared")

            #Message box to confirm is user really wants to delete tasks
            clearMsgBox = tkinter.messagebox.askquestion("Confirm","Are you sure you want to delete all tasks?")

            if clearMsgBox == 'yes':
                for a in task_table.get_children():
                    task_table.delete(a)
                self.i = 1

        clearBtn = Button(btnFrame, text = "clear", command = clearTask, width=10, height=4)
        clearBtn.grid(row=1, column=2, padx=8, pady=3)

root = Tk()
ob = Sneaker(root)
root.mainloop()