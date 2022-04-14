from tkinter import *
from tkinter import ttk
from db import database
db=database("Employee.db")
from tkinter import messagebox


window=Tk()
window.title('Registration Form')
window.geometry("1920x1080+0+0")
window.config(bg="#2c3e50")
window.state("zoomed")

name = StringVar()
age = StringVar()
doj = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()


# frame
entries_frame= Frame(window,bg="#535c68") 
entries_frame.pack(side=TOP, fill=X)
title= Label(entries_frame, text="Employee Management System",font=("calibri", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=1, sticky="W") 

#name 
lblname=Label(entries_frame, text="Name",font=("Poppins", 16), bg="#535c68", fg="White")
lblname.grid(row=1, column=0, padx= 10, pady=10, sticky="W") 
txtname = Entry(entries_frame, textvariable=name, font=("calibri", 16),width=30)
txtname.grid(row=1, column=1,padx= 10, pady=10)

#age 
lblage=Label(entries_frame, text="Age",font=("Poppins", 16), bg="#535c68", fg="white")
lblage.grid(row=1, column=2, padx= 10, pady=10, sticky="W") 
txtage = Entry(entries_frame, textvariable=age, font=("calibri", 16),width=30)
txtage.grid(row=1, column=3, padx= 10, pady=10)

#doj 
lbldoj=Label(entries_frame, text="DOJ",font=("Poppins", 16), bg="#535c68", fg="white")
lbldoj.grid(row=2, column=0,padx= 10, pady=10, sticky="W") 
txtdoj = Entry(entries_frame, textvariable=doj, font=("calibri", 16),width=30)
txtdoj.grid(row=2, column=1,padx= 10, pady=10)

#gender 
lblgender=Label(entries_frame, text="Gender",font=("Poppins", 16), bg="#535c68", fg="white")
lblgender.grid(row=2, column=2,padx= 10, pady=10, sticky="W") 
combogender = ttk.Combobox(entries_frame, font=("calibri", 16),width=28,textvariable=gender,state="readonly")
combogender['values']=("Male","Female")
combogender.grid(row=2, column=3,padx= 1)

#email 
lblemail=Label(entries_frame, text="Email",font=("Poppins", 16), bg="#535c68", fg="white")
lblemail.grid(row=3, column=0,padx= 10, pady=10, sticky="W") 
txtemail = Entry(entries_frame, textvariable=email, font=("calibri", 16),width=30)
txtemail.grid(row=3, column=1,padx= 10, pady=10)
#contact 
lblcontact=Label(entries_frame, text="Contact",font=("Poppins", 16), bg="#535c68", fg="white")
lblcontact.grid(row=3, column=2,padx= 10, pady=10, sticky="W") 
txtcontact = Entry(entries_frame, textvariable=contact, font=("calibri", 16),width=30)
txtcontact.grid(row=3, column=3,padx= 10, pady=10)

#Address
lbladdress=Label(entries_frame, text="Address", font=("Poppins", 16),bg="#535c68", fg="white")
lbladdress.grid(row=4, column=0, padx=10, pady=10, sticky="W")
txtaddress=Text(entries_frame, width=85, height=2, font=("Poppins", 16))
txtaddress.grid(row=5, column=0,columnspan=4, padx=10, sticky="W")

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    # print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtaddress.delete(1.0, END)
    txtaddress.insert(END, row[7])





def displayall():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END, values=row)



def add_emp():
    if txtname.get()=="" or txtage.get()=="" or txtdoj.get()=="" or txtemail.get()=="" or combogender.get()=="" or txtcontact.get() == "" or  txtaddress.get(1.0, END)=="" :
        messagebox.showerror("Error in Input", "Please all the details perfectly")
        return
    db.insert(txtname.get(), txtage.get(), txtdoj.get(),txtemail.get(),combogender.get(), txtcontact.get(), txtaddress.get(1.0, END))
    messagebox.showinfo("success", "Record Inserted")
    clearall()
    displayall()



def edit_emp():
    if txtname.get()=="" or txtage.get()=="" or txtdoj.get()=="" or txtemail.get()=="" or combogender.get()=="" or txtcontact.get() == "" or  txtaddress.get(1.0, END)=="" :
        messagebox.showerror("Error in Input", "Please all the details perfectly")
        return
    db.update(row[0], txtname.get(), txtage.get(), txtdoj.get(),txtemail.get(),combogender.get(), txtcontact.get(), txtaddress.get(1.0, END))
    messagebox.showinfo("success", "Record Inserted")
    clearall()
    displayall()



def delete_emp():
    db.remove(row[0])
    clearall()
    displayall() 

def clearall():
    name.set("")
    age.set("")
    doj.set("")
    email.set("")
    combogender.set("")
    contact.set("")
    txtaddress.delete(1.0, END)

clearall()
# displayall()

# def clear_emp():
#     name .set("")
#     age .set("")
#     doj .set("")
#     gender .set("")
#     email .set("")
#     contact .set("")
#     txtaddress.delete(1.0, END)




#addbutton
btnframe=Frame(entries_frame, bg='#535c68')
btnframe.grid(row=6, column=0,columnspan=4, padx=10, pady=3, sticky="W")
btnadd=Button(btnframe, command=add_emp, text="Add Details", width=10,height=1, font=("Poppins", 10, "bold"),fg="white", bg='#16a085')
btnadd.grid(row=0, column=0 ,pady=10)

#editbutton
btnedit=Button(btnframe, command=edit_emp, text="Edit", width=10,height=1, font=("Poppins", 10, "bold"),fg="white", bg='#2980b9')
btnedit.grid(row=0, column=1, padx=10, pady=10)

#deletebutton
btndelete=Button(btnframe, command=delete_emp, text="Delete", width=10,height=1, font=("Poppins", 10, "bold"),fg="white", bg='#c0392b')
btndelete.grid(row=0, column=2, padx=10, pady=10)

#clearbutton
btnclear=Button(btnframe, command=clearall, text="Clear", width=10,height=1, font=("Poppins", 10, "bold"),fg="white", bg='#f39c12')
btnclear.grid(row=0, column=3, padx=10, pady=10)

#table frame
tree_frame= Frame(window, bg="white")
tree_frame.place(x=0, y=430, width=1450, height=520)
style=ttk.Style()
style.configure("mystyle.Treeview", font=("calibri", 10),rowheight=50) #modify the font of body
style.configure("mystyle.Treeview.Heading",font=("poppins", 10))#modify the font of heading

tv=ttk.Treeview(tree_frame, columns=(1,2,3,4,5,6,7,8), style="mystyle.Treeview")
tv.heading("1", text='id')
tv.column("1", width=0)
tv.heading("2", text='name')
tv.column("2", width=5)
tv.heading("3", text='age')
tv.column("3", width=5)
tv.heading("4", text='doj')
tv.column("4", width=10)
tv.heading("5", text='email')
tv.column("5", width=8)
tv.heading("6", text='gender')
tv.column("6", width=10)
tv.heading("7", text='contact')
tv.column("7", width=10)
tv.heading("8", text='address')
tv.bind("<ButtonRelease-1>", getData)
tv['show']='headings'
tv.pack(fill=X)


displayall()


window.mainloop()
