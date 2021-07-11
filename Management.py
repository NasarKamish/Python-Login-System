import tkinter.ttk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview

import rsaidnumber

from playsound import *

import mysql.connector


def sound():
    playsound("Computer Error sound effect.mp3")


def func_delete():
    try:
        selected_item = Clients.selection()[0]

        delete_sql = "DELETE FROM tblKin WHERE id=%s"
        val = (Clients.item(selected_item)['values'][0],)
        mycursor.execute(delete_sql, val)
        mydb.commit()

        disable_sql = "SET FOREIGN_KEY_CHECKS=OFF"
        mycursor.execute(disable_sql)
        mydb.commit()

        delete_sql = "DELETE FROM tblClients WHERE id=%s"
        mycursor.execute(delete_sql, val)
        mydb.commit()

        enable_sql = "SET FOREIGN_KEY_CHECKS=ON"
        mycursor.execute(enable_sql)
        mydb.commit()

        Clients.delete(selected_item)
        Kin.delete(selected_item)
    except:
        sound()
        messagebox.showerror("Error", "Please select on the Client table")


def func_insert():
    def func_cancel():
        msg = messagebox.askquestion("Confirm", "Are you sure you want to cancel")
        if msg == "yes":
            frm_insert.destroy()

    def func_add():
        def func_insert_user():
            val = (en_id.get(), en_name.get(), en_surname.get(), en_phone.get(), en_password.get())
            SQL = 'INSERT INTO tblClients(id, Name, Surname, PhoneNumber, Password) \n VALUES(%s, %s, %s, %s, %s)'
            xy = mycursor.execute(SQL, val)

            mydb.commit()

            val = (en_name_k.get(), en_surname_k.get(), en_phone_k.get(), en_id.get())
            SQL = 'INSERT INTO tblKin(Name, Surname, PhoneNumber, id) \n VALUES(%s, %s, %s, %s)'
            xy = mycursor.execute(SQL, val)

            mydb.commit()

            global counter

            v = (en_id.get(), en_name.get(), en_surname.get(), en_phone.get(), en_password.get())

            if counter % 2 == 0:
                Clients.insert(parent='', index=counter, iid=counter, text='', values=(v[0], v[1], v[2], v[3], v[4]),
                               tag=("even",))
            else:
                Clients.insert(parent='', index=counter, iid=counter, text='', values=(v[0], v[1], v[2], v[3], v[4]),
                               tag=("odd",))
            counter += 1

            Clients.tag_configure("even", foreground="black", background="White")
            Clients.tag_configure("odd", foreground="white", background="black")
            messagebox.showinfo("Register", "User successfully registered")
            frm_insert.destroy()

        def val_space():
            msg = messagebox.askquestion("Confirm", "Do you want to continue")
            if msg == "yes":
                if en_id.get() == "":
                    sound()
                    messagebox.showerror("Error", "Please enter your id")
                elif en_name.get() == "":
                    sound()
                    messagebox.showerror("Error", "Please enter your name")
                elif en_surname.get() == "":
                    sound()
                    messagebox.showerror("Error", "Please enter your surname")
                elif en_phone.get() == "":
                    sound()
                    messagebox.showerror("Error", "Please enter your phone number")
                elif en_password.get() == "":
                    sound()
                    messagebox.showerror("Error", "Please enter your password")
                elif en_name_k.get() == "":
                    sound()
                    messagebox.showerror("Error", "Please enter their name")
                elif en_surname_k.get() == "":
                    sound()
                    messagebox.showerror("Error", "Please enter their surname")
                elif en_phone_k.get() == "":
                    sound()
                    messagebox.showerror("Error", "Please enter their phone")
                else:
                    val_id()

        def val_id():
            try:
                id_number = rsaidnumber.parse(en_id.get())
                if id_number.valid:
                    val_phones()
            except:
                pass
                sound()
                messagebox.showerror("Error", "Invalid ID number")

        def val_phones():
            try:
                int(en_phone.get())
                int(en_phone_k.get())

                if len(en_phone.get()) == len(en_phone_k.get()) == 10:
                    if en_phone.get() != en_phone_k.get():
                        func_insert_user()
                    else:
                        sound()
                        messagebox.showerror("Error", "Please make sure you add a different numbers")
                else:
                    sound()
                    messagebox.showerror("Error", "You need 10 characters in the phone number")
            except ValueError as vr:
                messagebox.showerror("Error", vr)
        val_space()

    frm_insert = Frame(management, bg="black", width=1100, height=300)
    frm_insert.place(x=0, y=0, width=1100, height=680)

    # Heading start
    lbl_head = Label(frm_insert, text="Add user", bg="black", fg="#8dc63f")
    lbl_head["font"] = "Times", 25
    lbl_head.place(x=0, y=10, width=1100)
    # Heading end

    # frame start
    frm_user = LabelFrame(frm_insert, text="User's details", bg="#346ab3", fg="#8dc63f")
    frm_user.place(x=50, y=100, width=450, height=300)

    frm_kin = LabelFrame(frm_insert, text="Next of Kin's details", bg="#346ab3", fg="#8dc63f")
    frm_kin.place(x=600, y=100, width=450, height=300)

    frm_login = LabelFrame(frm_insert, text="User login Details", bg="#346ab3", fg="#8dc63f")
    frm_login.place(x=50, y=450, width=1000, height=100)
    # frame end

    # name start
    lbl_name = Label(frm_user, text="Please enter your name:", bg="#346ab3", fg="#8dc63f")
    lbl_name["font"] = "Times", 15
    lbl_name.place(x=10, y=10)

    en_name = Entry(frm_user, fg="#346ab3", bg="black")
    en_name["font"] = "Times", 15
    en_name.place(x=10, y=40, width=300)

    lbl_name_k = Label(frm_kin, text="Please enter their name:", bg="#346ab3", fg="#8dc63f")
    lbl_name_k["font"] = "Times", 15
    lbl_name_k.place(x=10, y=10)

    en_name_k = Entry(frm_kin, fg="#346ab3", bg="black")
    en_name_k["font"] = "Times", 15
    en_name_k.place(x=10, y=40, width=300)
    # name end

    # Surname start
    lbl_surname = Label(frm_user, text="Please enter your surname:", bg="#346ab3", fg="#8dc63f")
    lbl_surname["font"] = "Times", 15
    lbl_surname.place(x=10, y=110)

    en_surname = Entry(frm_user, fg="#346ab3", bg="black")
    en_surname["font"] = "Times", 15
    en_surname.place(x=10, y=140, width=300)

    lbl_surname_k = Label(frm_kin, text="Please enter their surname:", bg="#346ab3", fg="#8dc63f")
    lbl_surname_k["font"] = "Times", 15
    lbl_surname_k.place(x=10, y=110)

    en_surname_k = Entry(frm_kin, fg="#346ab3", bg="black")
    en_surname_k["font"] = "Times", 15
    en_surname_k.place(x=10, y=140, width=300)
    # Surname end

    # Phone number start
    lbl_phone = Label(frm_user, text="Please enter your phone number:", bg="#346ab3", fg="#8dc63f")
    lbl_phone["font"] = "Times", 15
    lbl_phone.place(x=10, y=210)

    en_phone = Entry(frm_user, fg="#346ab3", bg="black")
    en_phone["font"] = "Times", 15
    en_phone.place(x=10, y=240, width=300)

    lbl_phone_k = Label(frm_kin, text="Please enter their phone number:", bg="#346ab3", fg="#8dc63f")
    lbl_phone_k["font"] = "Times", 15
    lbl_phone_k.place(x=10, y=210)

    en_phone_k = Entry(frm_kin, fg="#346ab3", bg="black")
    en_phone_k["font"] = "Times", 15
    en_phone_k.place(x=10, y=240, width=300)
    # Phone number end

    # ID start
    lbl_id = Label(frm_login, text="Please enter your id number:", bg="#346ab3", fg="#8dc63f")
    lbl_id["font"] = "Times", 15
    lbl_id.place(x=10, y=10)

    en_id = Entry(frm_login, fg="#346ab3", bg="black")
    en_id["font"] = "Times", 15
    en_id.place(x=10, y=40, width=300)
    # ID end

    # Password start
    lbl_password = Label(frm_login, text="Please enter your password:", bg="#346ab3", fg="#8dc63f")
    lbl_password["font"] = "Times", 15
    lbl_password.place(x=560, y=10)

    en_password = Entry(frm_login, fg="#346ab3", bg="black")
    en_password["font"] = "Times", 15
    en_password.place(x=560, y=40, width=300)
    # Password end

    btn_add = Button(frm_insert, text="Add account", bg="#346ab3", fg="#8dc63f")
    btn_add["command"] = func_add
    btn_add["font"] = "Times", 15
    btn_add.place(x=50, y=600, width=450)

    btn_cancel = Button(frm_insert, text="Cancel", bg="#346ab3", fg="#8dc63f")
    btn_cancel["command"] = func_cancel
    btn_cancel["font"] = "Times", 15
    btn_cancel.place(x=600, y=600, width=450)


mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', database='EOM_TEST')
mycursor = mydb.cursor()

management = Tk()
management.resizable(0, 0)
management.title("Management")
management.geometry("1100x700")
management["bg"] = "black"

# Heading start
lbl_Client = Label(management, text="Client Table", bg="black", fg="#8dc63f")
lbl_Client["font"] = "Times", 20
lbl_Client.place(x=0, y=10, width=1100)

lbl_Kin = Label(management, text="Next of Kin Table", bg="black", fg="#8dc63f")
lbl_Kin["font"] = "Times", 20
lbl_Kin.place(x=0, y=300, width=1100)
# Heading end

# User start
s = tkinter.ttk.Style(management)
s.theme_use("clam")
s.configure(".", font=('Helvetica', 11))
s.configure("Treeview.Heading", foreground="#8dc63f", background="#346ab3", font=('Arial', 15, 'bold'))

Clients = Treeview(management)
Clients['show'] = "headings"
Clients['columns'] = ('ID', 'Name', 'Surname', 'Phone', 'Password')
Clients.column('#0', width=0, stretch=NO)
Clients.column('ID', anchor=CENTER, width=200)
Clients.column('Name', anchor=CENTER, width=200)
Clients.column('Surname', anchor=CENTER, width=200)
Clients.column('Phone', anchor=CENTER, width=200)
Clients.column('Password', anchor=CENTER, width=200)

Clients.heading('#0', text='', anchor=CENTER)
Clients.heading('ID', text='Id', anchor=CENTER)
Clients.heading('Name', text='Name', anchor=CENTER)
Clients.heading('Surname', text='Surname', anchor=CENTER)
Clients.heading('Phone', text='Phone', anchor=CENTER)
Clients.heading('Password', text='Password', anchor=CENTER)


SQL1 = 'SELECT * FROM tblClients'
xy1 = mycursor.execute(SQL1)
counter = 0
for i in mycursor:
    if counter % 2 == 0:
        Clients.insert(parent='', index=counter, iid=counter, text='', values=(i[0], i[1], i[2], i[3], i[4]), tag=("even",))
    else:
        Clients.insert(parent='', index=counter, iid=counter, text='', values=(i[0], i[1], i[2], i[3], i[4]), tag=("odd",))
    counter += 1

Clients.tag_configure("even", foreground="black", background="White")
Clients.tag_configure("odd", foreground="white", background="black")

Clients.place(x=50, y=50)
# User end

# Next of kin start
s = tkinter.ttk.Style(management)
s.theme_use("clam")
s.configure(".", font=('Helvetica', 11))
s.configure("Treeview.Heading", foreground="#8dc63f", background="#346ab3", font=('Arial', 15, 'bold'))

Kin = Treeview(management)
Kin['show'] = "headings"
Kin['columns'] = ('KinID', 'Name', 'Surname', 'Phone', 'ID')
Kin.column('#0', width=0, stretch=NO)
Kin.column('KinID', anchor=CENTER, width=200)
Kin.column('Name', anchor=CENTER, width=200)
Kin.column('Surname', anchor=CENTER, width=200)
Kin.column('Phone', anchor=CENTER, width=200)
Kin.column('ID', anchor=CENTER, width=200)

Kin.heading('#0', text='', anchor=CENTER)
Kin.heading('KinID', text='KinId', anchor=CENTER)
Kin.heading('Name', text='Name', anchor=CENTER)
Kin.heading('Surname', text='Surname', anchor=CENTER)
Kin.heading('Phone', text='Phone', anchor=CENTER)
Kin.heading('ID', text='ID', anchor=CENTER)


SQL1 = 'SELECT * FROM tblKin'
xy1 = mycursor.execute(SQL1)
counter = 0
for i in mycursor:
    if counter % 2 == 0:
        Kin.insert(parent='', index=counter, iid=counter, text='', values=(i[0], i[1], i[2], i[3], i[4]), tag=("even",))
    else:
        Kin.insert(parent='', index=counter, iid=counter, text='', values=(i[0], i[1], i[2], i[3], i[4]), tag=("odd",))
    counter += 1

Kin.tag_configure("even", foreground="black", background="White")
Kin.tag_configure("odd", foreground="white", background="black")

Kin.place(x=50, y=350)
# Next of kin end

# Buttons start
btn_Insert = Button(management, text="Insert", bg="#346ab3", fg="#8dc63f")
btn_Insert["command"] = func_insert
btn_Insert["font"] = "Arial", 15
btn_Insert.place(x=50, y=600, width=450)

btn_Delete = Button(management, text="Delete", bg="#346ab3", fg="#8dc63f")
btn_Delete["command"] = func_delete
btn_Delete["font"] = "Arial", 15
btn_Delete.place(x=600, y=600, width=450)
# Buttons end


def execute(event):
    management.destroy()
    import Register


management.bind("<Control_L><a>", execute)
management.bind("<Control_L><A>", execute)

management.mainloop()
