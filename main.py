from tkinter import messagebox

from tkinter import *

import mysql.connector

from playsound import *

try:
    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', database='EOM_TEST')
    mycursor = mydb.cursor()


    def func_logout():
        def func_sign_out():
            update_sql = "Update tblTime SET Leave_at = curtime() WHERE id = '" + en_ID.get() + "'"
            mycursor.execute(update_sql)
            mydb.commit()

            en_ID.delete(0, END)
            en_password.delete(0, END)
            frm_logout.destroy()
        frm_logout = Frame(login, bg="black")
        frm_logout.place(x=0, y=0, width=700, height=300)

        lbl_logout = Label(frm_logout, text="Log out form", bg="black", fg="#8dc63f")
        lbl_logout["font"] = "Times", 20
        lbl_logout.place(x=0, y=10, width=700)

        btn_logout = Button(frm_logout, text="Signout", bg="#346ab3", fg="#8dc63f")
        btn_logout["command"] = func_sign_out
        btn_logout.place(x=50, y=200, width=600, height=350)
        btn_logout["font"] = "Times", 20


    def func_register():
        msg = messagebox.askquestion("Confirm", "Are you sure you don't have an account")
        if msg == "yes":
            login.destroy()
            import Register

    def sound():
        playsound("Computer Error sound effect.mp3")


    def func_login():
        login_query = 'SELECT * FROM tblClients'
        mycursor.execute(login_query)
        valid = False
        for k in mycursor:
            # print(k)
            if k[0] == en_ID.get() and k[4] == en_password.get():
                valid = True
        if not valid:
            sound()
            messagebox.showerror("Error", "Invalid id or password")
        elif valid:
            update_sql = "Update tblTime SET Enter_at = curTime(), Day = curDate() WHERE id = '" + en_ID.get() + "'"
            mycursor.execute(update_sql)
            mydb.commit()
            messagebox.showinfo("Welcome", "You have succesfully loged in")
            func_logout()


    def func_exit():
        msg = messagebox.askquestion("Confirm", "Are you sure you want to exit")
        if msg == "yes":
            login.destroy()


    login = Tk()
    login.resizable(0, 0)
    login.title("Log-in")
    login.geometry("700x350")
    login["bg"] = "black"

    # Heading start
    lbl_head = Label(login, text="Log-in", bg="black", fg="#8dc63f")
    lbl_head["font"] = "Times", 20
    lbl_head.place(x=0, y=10, width=700)
    # Heading end

    # ID start
    lbl_ID = Label(login, text="Please enter your id number:", bg="black", fg="#8dc63f")
    lbl_ID["font"] = "Times", 15
    lbl_ID.place(x=50, y=100)

    en_ID = Entry(login, fg="#8dc63f", bg="#346ab3")
    en_ID["font"] = "Times", 15
    en_ID.place(x=300, y=100, width=350)
    # ID end

    # Password start
    lbl_password = Label(login, text="Please enter password:", bg="black", fg="#8dc63f")
    lbl_password["font"] = "Times", 15
    lbl_password.place(x=50, y=150)

    en_password = Entry(login, fg="#8dc63f", bg="#346ab3")
    en_password["font"] = "Times", 15
    en_password.place(x=300, y=150, width=350)
    # Password end

    # Buttons start
    btn_login = Button(login, text="Login", bg="#346ab3", fg="#8dc63f")
    btn_login["command"] = func_login
    btn_login["font"] = "Times", 15
    btn_login.place(x=50, y=200, width=250)

    btn_Register = Button(login, text="Register new user", bg="#346ab3", fg="#8dc63f")
    btn_Register["command"] = func_register
    btn_Register["font"] = "Times", 15
    btn_Register.place(x=400, y=200, width=250)

    btn_Exit = Button(login, text="Exit", bg="#346ab3", command=func_exit, fg="#8dc63f")
    btn_Exit["font"] = "Times", 15
    btn_Exit.place(x=200, y=250, width=300)
    # Buttons end

    # hot keys to access admin form


    def execute(event):
        login.destroy()
        import Management

    login.bind("<Control_L><a>", execute)
    login.bind("<Control_L><A>", execute)

    login.mainloop()

except mysql.connector.Error as er:
    messagebox.showerror("Error", er)
