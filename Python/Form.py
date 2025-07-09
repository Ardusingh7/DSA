import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

r=Tk()

lb=Label(r,text="REGISTRATION FORM",fg="aqua",bg="gray25",font=("arial",23))
lb.grid(row=0,column=1)


lb2=Label(r,text="Name",fg="orange",bg="black",font=7)
lb2.grid(row=1,column=0)

e=Entry(r,font=5)
e.grid(row=1,column=1)

lb2=Label(r,text="Father's name",fg="white",bg="black",font=7)
lb2.grid(row=2,column=0)

e2=Entry(r,font=5)
e2.grid(row=2,column=1)

lb3=Label(r,text="ERP ID",fg="green",bg="black",font=7)
lb3.grid(row=3,column=0)

e3=Entry(r,font=5)
e3.grid(row=3,column=1)

lb4=Label(r,text="Branch",fg="orange",bg="black",font=7)
lb4.grid(row=4,column=0)

e4=Entry(r,font=5)
e4.grid(row=4,column=1)

lb5=Label(r,text="Section",fg="white",bg="black",font=7)
lb5.grid(row=5,column=0)

sections = ["---Select---","A","B","C","D","E","F"]

v = StringVar(r)
v.set(sections[0])

dm = OptionMenu(r, v, *sections)
dm.grid(row=5,column=1)

lb6=Label(r,text="Address",fg="green",bg="black",font=7)
lb6.grid(row=6,column=0)

e5=Text(r,height=5,width=25,font=5)
e5.grid(row=6,column=1)

lb7=Label(r,text="Gender",fg="orange",bg="black",font=7)
lb7.grid(row=7,column=0)

Gender_var=tk.StringVar()

Male=ttk.Radiobutton(r, text="M", value="Male", variable=Gender_var)
Male.grid(row=7, column=1)

Female=ttk.Radiobutton(r, text="F", value="Female", variable=Gender_var)
Female.grid(row=7, column=2)

lb8=Label(r,text="Category",fg="white",bg="black",font=7)
lb8.grid(row=8,column=0)

cb=ttk.Combobox(r, width=27,state="readonly")
cb['values']=("---------Select Category----------","Scheduled Castes (SCs)","Scheduled Tribes (STs)","Other Backward Castes (OBCs)",
              "Economically Backward Section (EBCs)","General")

cb.current(0)
cb.grid(row=8, column=1)

lb9=Label(r,text="Language",fg="green",bg="black",font=7)
lb9.grid(row=9,column=0)

cb=Checkbutton(r, text = "Python",font=7)
cb.grid(row=9,column=1)

cb=Checkbutton(r, text = "Java",font=7)
cb.grid(row=10,column=1)

cb=Checkbutton(r, text = "C++",font=7)
cb.grid(row=11,column=1)

cb=Checkbutton(r, text = "OOPs",font=7)
cb.grid(row=12,column=1)

def click():

    name=e.get()
    fname=e2.get()
    erp=e3.get()
    branch=e4.get()
    
    if name=="":
        messagebox.showinfo('ERROR',"PLEASE ENTER NAME!")
    elif fname=="":
        messagebox.showinfo("ERROR","PLEASE ENTER FATHER'S NAME!")
    elif erp=="":
        messagebox.showinfo("ERROR","PLEASE ENTER ERP_ID!")
    elif branch=="":
        messagebox.showinfo("ERROR","PLEASE ENTER BRANCH!")
    else:
        e.delete(0, tk.END)
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)
        e4.delete(0, tk.END)
        print("Bye :)")
        messagebox.showinfo("Info","You have successfully, registered.")


b=Button(r,text="Submit",command=click,height=5,width=20)
b.grid(row=13,column=0)

b2=Button(r,text="Cancel",command=r.destroy,height=5,width=20)
b2.grid(row=13,column=2)

r.mainloop()
