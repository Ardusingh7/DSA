import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
import Conditions

win=tk.Tk()
win.title("DU")
win.geometry()

#Labels

Name_label=ttk.Label(win, text ="First name :-")
Name_label.grid(row=0,column=0, sticky=tk.W)

Surname_label=ttk.Label(win, text ="Surname :-")
Surname_label.grid(row=25,column=0, sticky=tk.W)

Dob_label=ttk.Label(win, text="Date_of_Birth :-")
Dob_label.grid(row=50,column=0, sticky=tk.W)

Gender_label=ttk.Label(win, text="Gender")
Gender_label.grid(row=75, column=0, sticky=tk.W)

Category_label=ttk.Label(win, text="Category")
Category_label.grid(row=100, column=0, sticky=tk.W)

State_label=ttk.Label(win, text="State")
State_label.grid(row=125, column=0, sticky=tk.W)

F_Name_label=ttk.Label(win, text="Father's name :-")
F_Name_label.grid(row=150, column=0, sticky=tk.W)

M_Name_label=ttk.Label(win, text="Mother's name :-")
M_Name_label.grid(row=175, column=0, sticky=tk.W)

Email_label=ttk.Label(win, text ="Email ID :-")
Email_label.grid(row=200,column=0, sticky=tk.W)

Marks_label=ttk.Label(win, text ="Percentile in 10+2 :-")
Marks_label.grid(row=225,column=0, sticky=tk.W)

#Entryboxes

Name_var=tk.StringVar()
Name_entrybox=ttk.Entry(win, width=30, textvariable= Name_var)
Name_entrybox.grid(row=0,column=1,pady=10)
Name_entrybox.focus()

Surname_var=tk.StringVar()
Surname_entrybox=ttk.Entry(win, width=30, textvariable= Surname_var)
Surname_entrybox.grid(row=25,column=1,pady=10)

Dob_var=tk.StringVar()
Dob_entrybox=ttk.Entry(win, width=30, textvariable= Dob_var)
Dob_entrybox.grid(row=50,column=1,pady=10)

F_Name_var=tk.StringVar()
F_Name_entrybox=ttk.Entry(win, width=30, textvariable= F_Name_var)
F_Name_entrybox.grid(row=150,column=1,pady=10)

M_Name_var=tk.StringVar()
M_Name_entrybox=ttk.Entry(win, width=30, textvariable= M_Name_var)
M_Name_entrybox.grid(row=175,column=1,pady=10)

Email_var=tk.StringVar()
Email_entrybox=ttk.Entry(win, width=30, textvariable= Email_var)
Email_entrybox.grid(row=200,column=1,pady=10)

Marks_var=tk.StringVar()
Marks_entrybox=ttk.Entry(win, width=30, textvariable= Marks_var)
Marks_entrybox.grid(row=225,column=1,pady=10)

#Drop_down_boxes

State_var=tk.StringVar()
State_box=ttk.Combobox(win, width=27, textvariable= State_var, state="readonly")
State_box['values']=("-----------Select State----------","Andaman and Nicobar","Andhra Pradesh", "Arunachal Pradesh","Assam","Bihar","Chattisgarh","Daman and Diu",
                     "Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Lakshadweep","Madhya Pradesh",
                     "Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura",
                     "Uttarakhand","Uttar Pradesh","West Bengal")
State_box.current(0)
State_box.grid(row=125, column=1,pady=10)

Category_var=tk.StringVar()
Category_box=ttk.Combobox(win, width=27, textvariable= Category_var, state="readonly")
Category_box['values']=("---------Select Category----------","Scheduled Castes (SCs)","Scheduled Tribes (STs)","Other Backward Castes (OBCs)",
                        "Economically Backward Section (EBCs)","General")
Category_box.current(0)
Category_box.grid(row=100, column=1,pady=10)

#Radio_Buttons

Gender_var=tk.StringVar()

Male=ttk.Radiobutton(win, text="Male", value="Male", variable=Gender_var)
Male.grid(row=75, column=1)

Female=ttk.Radiobutton(win, text="Female", value="Female", variable=Gender_var)
Female.grid(row=80, column=1)

Others=ttk.Radiobutton(win, text="Others", value="Others", variable=Gender_var)
Others.grid(row=85, column=1)


def action():
    Firstname=Name_var.get()
    Lastname=Surname_var.get()
    Dob=Dob_var.get()
    Email=Email_var.get()
    State=State_var.get()
    Gender=Gender_var.get()
    Category=Category_var.get()
    F_Name=F_Name_var.get()
    M_Name=M_Name_var.get()
    Marks=Marks_var.get()

    with open("File.csv",'a') as f:
        dict_writer=DictWriter(f, fieldnames=["FirstName","LastName","Date_of_birth","Gender","Category","State","Father's Name","Mother's Name","Email_Id",
                                              "Percentile"])

        if os.stat("File.csv",).st_size==0:
            dict_writer.writeheader()
            
        dict_writer.writerow({
            "FirstName":Firstname,
            "LastName":Lastname,
            "Date_of_birth":Dob,
            "Category":Category,
            "Gender":Gender,
            "State":State,
            "Father's Name":F_Name,
            "Mother's Name":M_Name,
            "Email_Id":Email,
            "Percentile":Marks})

    Name_entrybox.delete(0, tk.END)
    Surname_entrybox.delete(0, tk.END)
    Dob_entrybox.delete(0, tk.END)
    F_Name_entrybox.delete(0, tk.END)
    M_Name_entrybox.delete(0, tk.END)
    Email_entrybox.delete(0, tk.END)
    Marks_entrybox.delete(0, tk.END)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

    print("Hello,",Firstname)

    if Firstname=="":
        print("PLEASE ENTER NAME!")
        print("--------------------------------")
    elif Gender=="":
        print("PLEASE ENTER GENDER!")
        print("--------------------------------")
    elif Marks=="": 
        print("PLEASE ENTER MARKS!")
        print("--------------------------------")
        
    
    if Marks>="95" and Category=="Scheduled Castes (SCs)" and Gender=="Female":
        Conditions.A1()
    elif Marks>="95" and Category=="Scheduled Tribes (STs)" and Gender=="Female":
        Conditions.A2()
    elif Marks>="95" and Category=="Other Backward Castes (OBCs)" and Gender=="Female":
        Conditions.A3()
    elif Marks>="95" and Category=="Economically Backward Section (EBCs)" and Gender=="Female":
        Conditions.A4()
    elif Marks>="95" and Category=="General" and Gender=="Female":
        Conditions.A5()
    elif Marks>="95" and Category=="Scheduled Castes (SCs)" or Category=="Other Backward Castes (OBCs)":
        Conditions.A6()
    elif Marks>="95" and Category=="Scheduled Tribes (STs)":
        Conditions.A7()
    elif Marks>="95" and Category=="Economically Backward Section (EBCs)":
        Conditions.A8()
    elif Marks>="95" and Category=="General":
        Conditions.A9()
        
    elif Marks>="90" and Category=="Scheduled Castes (SCs)" and Gender=="Female":
        Conditions.B1()
    elif Marks>="90" and Category=="Scheduled Tribes (STs)" and Gender=="Female":
        Conditions.B2()
    elif Marks>="90" and Category=="Other Backward Castes (OBCs)" and Gender=="Female":
        Conditions.B3()
    elif Marks>="90" and Category=="Economically Backward Section (EBCs)" and Gender=="Female":
        Conditions.B4()
    elif Marks>="90" and Category=="General" and Gender=="Female":
        Conditions.B5()
    elif Marks>="90" and Category=="Scheduled Castes (SCs)" or Category=="Other Backward Castes (OBCs)":
        Conditions.B6()
    elif Marks>="90" and Category=="Scheduled Tribes (STs)":
        Conditions.B7()
    elif Marks>="90" and Category=="Economically Backward Section (EBCs)":
        Conditions.B8()
    elif Marks>="90" and Category=="General" and Gender=="Male" or Gender=="Others":
        Conditions.B9()

    elif Marks>="85" and Category=="Scheduled Castes (SCs)" and Gender=="Female":
        Conditions.C1()
    elif Marks>="85" and Category=="Scheduled Tribes (STs)" and Gender=="Female":
        Conditions.C2()
    elif Marks>="85" and Category=="Other Backward Castes (OBCs)" and Gender=="Female":
        Conditions.C3()
    elif Marks>="85" and Category=="Economically Backward Section (EBCs)" and Gender=="Female":
        Conditions.C4()
    elif Marks>="85" and Category=="General" and Gender=="Female":
        Conditions.C5()
    elif Marks>="85" and Category=="Scheduled Castes (SCs)" or Category=="Other Backward Castes (OBCs)":
        Conditions.C6()
    elif Marks>="85" and Category=="Scheduled Tribes (STs)":
        Conditions.C7()
    elif Marks>="85" and Category=="Economically Backward Section (EBCs)":
        Conditions.C8()
    elif Marks>="85" and Category=="General":
        Conditions.C9()

    elif Marks>="80" and Category=="Scheduled Castes (SCs)" and Gender=="Female":
        Conditions.D1()
    elif Marks>="80" and Category=="Scheduled Tribes (STs)" and Gender=="Female":
        Conditions.D2()
    elif Marks>="80" and Category=="Other Backward Castes (OBCs)" and Gender=="Female":
        Conditions.D3()
    elif Marks>="80" and Category=="Economically Backward Section (EBCs)" and Gender=="Female":
        Conditions.D4()
    elif Marks>="80" and Category=="General" and Gender=="Female":
        Conditions.D5()
    elif Marks>="80" and Category=="Scheduled Castes (SCs)" or Category=="Other Backward Castes (OBCs)":
        Conditions.D6()
    elif Marks>="80" and Category=="Scheduled Tribes (STs)":
        Conditions.D7()
    elif Marks>="80" and Category=="Economically Backward Section (EBCs)":
        Conditions.D8()
    elif Marks>="80" and Category=="General":
        Conditions.D9()

    elif Marks>="0" and Marks<="79":
        Conditions.E()
        
Submit_button=ttk.Button(win, text="Submit",width=20, command=action)
Submit_button.grid(row=1000, column=1)

win.mainloop()


