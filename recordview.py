from tkinter.ttk import Treeview
from tkinter import *
import mysql.connector
from tkinter import messagebox
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Savi@123", database="demobase"
)
mycursor = mydb.cursor()

root = Tk()
root.title("View Record by ENO")
root.geometry("600x300")
Label(root, text="Enter ENO:", font=("Arial", 12)).grid(row=0, column=0, pady=10, padx=10)
eno_entry = Entry(root, width=30, borderwidth=5)
eno_entry.grid(row=0, column=1, pady=10, padx=10)

tree = Treeview(root, columns=("ENO", "ENAME", "ESAL", "EGRADE"), show="headings", height=5)
tree.grid(row=2, column=0, columnspan=2, pady=20)
tree.heading("ENO", text="ENO")
tree.heading("ENAME", text="ENAME")
tree.heading("ESAL", text="ESAL")
tree.heading("EGRADE", text="EGRADE")
tree.column("ENO", width=100)
tree.column("ENAME", width=150)
tree.column("ESAL", width=100)
tree.column("EGRADE", width=100)

def fetch_record():
    for row in tree.get_children():
        tree.delete(row)  # Clear the Treeview

    eno = eno_entry.get()
    if eno:
        query = "SELECT * FROM myemp WHERE eno = %s"
        mycursor.execute(query, (eno,))
        record = mycursor.fetchone()
        if record:
            tree.insert("", "end", values=record)
        else:
            messagebox.showinfo("No Record", "No record found for ENO: " + eno)
    else:
        messagebox.showwarning("Input Required", "Please enter an ENO!")
Button(root, text="Search", width=10, command=fetch_record).grid(row=1, column=1, pady=10)
root.mainloop()
