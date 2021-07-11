from builtins import breakpoint
from tkinter import messagebox

from tkinter import *

import mysql.connector

import rsaidnumber

from playsound import *

from pynput import keyboard


try:
    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', database='EOM_TEST')
    mycursor = mydb.cursor()


    def sound():
        playsound("Computer Error sound effect.mp3")

    def func_logout():
        def func_sign_out():
            update_sql = "Update tblTime SET Leave_at = curtime() WHERE id = '" + en_ID.get() + "'"
            mycursor.execute(update_sql)
            mydb.commit()

            en_ID.delete(0, END)
            en_password.delete(0, END)
            en_name.delete(0, END)
            en_phone.delete(0, END)
            en_surname.delete(0, END)
            en_phone_K.delete(0, END)
            en_surname_K.delete(0, END)
            en_name_K.delete(0, END)
            frm_logout.destroy()
        frm_logout = Frame(register, bg="black")

        frm_logout.place(x=0, y=0, width=1000, height=600)
        lbl_logout = Label(frm_logout, text="Log out form", bg="black", fg="#8dc63f")
        lbl_logout["font"] = "Times", 20

        lbl_logout.place(x=0, y=10, width=1000)
        btn_logout = Button(frm_logout, text="Sign out", bg="#346ab3", fg="#8dc63f")
        btn_logout["command"] = func_sign_out

        btn_logout.place(x=50, y=200, width=900, height=200)
        btn_logout["font"] = "Times", 20

    def func_insert():
        val = (en_ID.get(), en_name.get(), en_surname.get(), en_phone.get(), en_password.get())
        SQL = 'INSERT INTO tblClients(id, Name, Surname, PhoneNumber, Password) \n VALUES(%s, %s, %s, %s, %s)'
        xy = mycursor.execute(SQL, val)

        mydb.commit()

        val = (en_name_K.get(), en_surname_K.get(), en_phone_K.get(), en_ID.get())
        SQL = 'INSERT INTO tblKin(Name, Surname, PhoneNumber, id) \n VALUES(%s, %s, %s, %s)'
        xy = mycursor.execute(SQL, val)

        mydb.commit()

        val = (en_ID.get())
        SQL = 'INSERT INTO tblTime(Day, Enter_at, id) \n VALUES(curDate(), curtime(), "' + en_ID.get() + '");'
        xyz = mycursor.execute(SQL)

        mydb.commit()

        func_logout()

    def val_space():
        msg = messagebox.askquestion("Confirm", "Do you want to continue")
        if msg == "yes":
            if en_ID.get() == "":
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
            elif en_name_K.get() == "":
                sound()
                messagebox.showerror("Error", "Please enter their name")
            elif en_surname_K.get() == "":
                sound()
                messagebox.showerror("Error", "Please enter their surname")
            elif en_phone_K.get() == "":
                sound()
                messagebox.showerror("Error", "Please enter their phone")
            else:
                val_id()

    def val_id():
        try:
            id_number = rsaidnumber.parse(en_ID.get())
            if id_number.valid:
                val_phones()
        except:
            pass
            sound()
            messagebox.showerror("Error", "Invalid ID number")

    def val_phones():
        try:
            int(en_phone.get())
            int(en_phone_K.get())

            if len(en_phone.get()) == len(en_phone_K.get()) == 10:
                if en_phone.get() != en_phone_K.get():
                    func_insert()
                else:
                    sound()
                    messagebox.showerror("Error", "Please make sure you add a different numbers")
            else:
                sound()
                messagebox.showerror("Error", "You need 10 characters in the phone number")
        except ValueError as vr:
            messagebox.showerror("Error", vr)

    def func_account():
        msg = messagebox.askquestion("Confirm", "You will loose all your progress")
        if msg == "yes":
            register.destroy()
            import main

    def func_exit():
        msg = messagebox.askquestion("Confirm", "Are you sure you want to exit")
        if msg == "yes":
            register.destroy()

    register = Tk()
    register.resizable(0, 0)
    register.title("Register")
    register.geometry("1000x600")
    register["bg"] = "black"

    # Heading start
    lbl_head = Label(register, text="Register", bg="black", fg="#8dc63f")
    lbl_head["font"] = "Times", 20
    lbl_head.place(x=0, y=10, width=1000)
    # Heading end

    # frame start
    frm_User = LabelFrame(register, text="User's details", bg="#346ab3", fg="#8dc63f")
    frm_User.place(x=50, y=50, width=400, height=300)

    frm_Kin = LabelFrame(register, text="Next of Kin's details", bg="#346ab3", fg="#8dc63f")
    frm_Kin.place(x=550, y=50, width=400, height=300)

    frm_Login = LabelFrame(register, text="User login Details", bg="#346ab3", fg="#8dc63f")
    frm_Login.place(x=50, y=370, width=900, height=100)
    # frame end

    # name start
    lbl_name = Label(frm_User, text="Please enter your name:", bg="#346ab3", fg="#8dc63f")
    lbl_name["font"] = "Times", 15
    lbl_name.place(x=10, y=10)

    en_name = Entry(frm_User, fg="#346ab3", bg="black")
    en_name["font"] = "Times", 15
    en_name.place(x=10, y=40, width=300)

    lbl_name_K = Label(frm_Kin, text="Please enter their name:", bg="#346ab3", fg="#8dc63f")
    lbl_name_K["font"] = "Times", 15
    lbl_name_K.place(x=10, y=10)

    en_name_K = Entry(frm_Kin, fg="#346ab3", bg="black")
    en_name_K["font"] = "Times", 15
    en_name_K.place(x=10, y=40, width=300)
    # name end

    # Surname start
    lbl_surname = Label(frm_User, text="Please enter your surname:", bg="#346ab3", fg="#8dc63f")
    lbl_surname["font"] = "Times", 15
    lbl_surname.place(x=10, y=110)

    en_surname = Entry(frm_User, fg="#346ab3", bg="black")
    en_surname["font"] = "Times", 15
    en_surname.place(x=10, y=140, width=300)

    lbl_surname_K = Label(frm_Kin, text="Please enter their surname:", bg="#346ab3", fg="#8dc63f")
    lbl_surname_K["font"] = "Times", 15
    lbl_surname_K.place(x=10, y=110)

    en_surname_K = Entry(frm_Kin, fg="#346ab3", bg="black")
    en_surname_K["font"] = "Times", 15
    en_surname_K.place(x=10, y=140, width=300)
    # Surname end

    # Phone number start
    lbl_phone = Label(frm_User, text="Please enter your phone number:", bg="#346ab3", fg="#8dc63f")
    lbl_phone["font"] = "Times", 15
    lbl_phone.place(x=10, y=210)

    en_phone = Entry(frm_User, fg="#346ab3", bg="black")
    en_phone["font"] = "Times", 15
    en_phone.place(x=10, y=240, width=300)

    lbl_phone_K = Label(frm_Kin, text="Please enter their phone number:", bg="#346ab3", fg="#8dc63f")
    lbl_phone_K["font"] = "Times", 15
    lbl_phone_K.place(x=10, y=210)

    en_phone_K = Entry(frm_Kin, fg="#346ab3", bg="black")
    en_phone_K["font"] = "Times", 15
    en_phone_K.place(x=10, y=240, width=300)
    # Phone number end

    # ID start
    lbl_ID = Label(frm_Login, text="Please enter your id number:", bg="#346ab3", fg="#8dc63f")
    lbl_ID["font"] = "Times", 15
    lbl_ID.place(x=10, y=10)

    en_ID = Entry(frm_Login, fg="#346ab3", bg="black")
    en_ID["font"] = "Times", 15
    en_ID.place(x=10, y=40, width=300)
    # ID end

    # Password start
    lbl_password = Label(frm_Login, text="Please enter your password:", bg="#346ab3", fg="#8dc63f")
    lbl_password["font"] = "Times", 15
    lbl_password.place(x=510, y=10)

    en_password = Entry(frm_Login, fg="#346ab3", bg="black")
    en_password["font"] = "Times", 15
    en_password.place(x=510, y=40, width=300)
    # Password end

    # Buttons start
    btn_login = Button(register, text="Already have an account", bg="#346ab3", fg="#8dc63f")
    btn_login["command"] = func_account
    btn_login["font"] = "Times", 15
    btn_login.place(x=50, y=500, width=400)

    btn_Register = Button(register, text="Register current user", bg="#346ab3", fg="#8dc63f")
    btn_Register["command"] = val_space
    btn_Register["font"] = "Times", 15
    btn_Register.place(x=550, y=500, width=400)

    btn_Exit = Button(register, text="Exit", bg="#346ab3", fg="#8dc63f")
    btn_Exit["command"] = func_exit
    btn_Exit["font"] = "Times", 15
    btn_Exit.place(x=300, y=550, width=400)
    # Buttons end


    def execute(event):
        register.destroy()
        import Management

    register.bind("<Control_L><a>", execute)
    register.bind("<Control_L><A>", execute)

    register.mainloop()
except mysql.connector.Error as er:
    messagebox.showerror("Error", er)
