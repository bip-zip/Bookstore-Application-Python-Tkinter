from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DATABASE import MyDb
from Add_Books import AddBooks
from See_Books import *
from datetime import date
from Buy_Books import *
from Fetch_Bill import *
import smtplib


class Guis:
    def __init__(self):
        self.buy = BuyBooks()
        self.log_in()
        self.data_base = MyDb()
        self.ab = AddBooks()
        self.see = SeeBooks()
        self.fetch=FetchBill()

    def log_in(self):
        try:
            self.main_dis = Tk()
            self.main_dis.title('Log-in')
            self.main_dis.geometry('1920x1080')
            self.main_dis.configure(bg='steelblue3')



            self.lbl111 = Label(self.main_dis, bg='Steelblue1', width=600, height=4,
                                font=('Ariel', 15, 'bold'))
            self.lbl111.place(x=1, y=20)

            self.lbl112 = Label(self.main_dis, text='ORIENTAL BOOK HOUSE', bg='Steelblue1', fg='black',
                                font=('Ariel', 19, 'bold'))
            self.lbl112.place(x=560, y=30)

            self.lbl112 = Label(self.main_dis, text='Bagbazar, Kathmandu', bg='Steelblue1', fg='black',
                                font=('Ariel', 12, 'bold'))
            self.lbl112.place(x=620, y=75)

            self.lbl113 = Label(self.main_dis, bg='Steelblue1', width=40, height=2)
            self.lbl113.place(x=560, y=160)

            self.lbl1131 = Label(self.main_dis, bg='Steelblue1', width=40, height=10)
            self.lbl1131.place(x=560, y=240)

            self.lbl11314 = Label(self.main_dis, bg='Steelblue1', width=40, height=3)
            self.lbl11314.place(x=560, y=440)

            self.lbl1 = Label(self.main_dis, text='Log-In Portal', bg='Steelblue1', font=('Ariel', 15, 'bold'))
            self.lbl1.place(x=640, y=165)

            self.lbl2 = Label(self.main_dis, text='Username', bg='Steelblue1', font=('Ariel', 11, 'bold'))
            self.lbl2.place(x=570, y=290)

            self.ent1 = Entry(self.main_dis, font=('Ariel', 11, 'bold'))
            self.ent1.place(x=670, y=290)

            self.lbl3 = Label(self.main_dis, text='Password', bg='Steelblue1', font=('Ariel', 11, 'bold'))
            self.lbl3.place(x=570, y=330)

            self.ent2 = Entry(self.main_dis, show='*',font=('Ariel', 11, 'bold'))
            self.ent2.place(x=670, y=330)

            self.btn01 = Button(self.main_dis, text='     Log-in     ', bg='black', fg='white', command=self.do_login,
                                font=('Ariel', 13, 'bold'), width=10)
            self.btn01.place(x=650, y=450)

            self.btn03 = Button(self.main_dis, text='     Register for new    ', bg='black', fg='yellow',
                                font=('Ariel', 9, 'bold'), command=self.reg_screen)
            self.btn03.place(x=1200, y=165)

            self.main_dis.mainloop()

        except Exception as e:
            print(e)


    def reg_screen(self):
        try:
            self.main_dis.destroy()
            self.reges = Tk()
            self.reges.title('User Registration')
            self.reges.geometry('1920x1080+0+0')
            self.reges.configure(bg='springgreen2')


            self.lbl111 = Label(self.reges, bg='palegreen', width=600, height=4,
                                font=('Ariel', 15, 'bold'))
            self.lbl111.place(x=1, y=20)

            self.lbl112 = Label(self.reges, text='ORIENTAL BOOK HOUSE', bg='palegreen', fg='black',
                                font=('Ariel', 19, 'bold'))
            self.lbl112.place(x=560, y=30)

            self.lbl112 = Label(self.reges, text='Bagbazar, Kathmandu', bg='palegreen', fg='black',
                                font=('Ariel', 12, 'bold'))
            self.lbl112.place(x=620, y=75)

            self.lbl113 = Label(self.reges, bg='palegreen', width=40, height=2)
            self.lbl113.place(x=560, y=140)

            self.lbl1131 = Label(self.reges, bg='palegreen', width=40, height=13)
            self.lbl1131.place(x=560, y=190)

            self.lbl1131 = Label(self.reges, bg='palegreen', width=40, height=5)
            self.lbl1131.place(x=560, y=410)


            self.lbl11314 = Label(self.reges, bg='palegreen', width=190, height=3)
            self.lbl11314.place(x=560, y=530)

            self.lbl1 = Label(self.reges, text='Admin Registration', bg='palegreen', font=('Ariel', 15, 'bold'))
            self.lbl1.place(x=615, y=145)

            self.lbl2 = Label(self.reges, text='Name', bg='palegreen',font=('Ariel', 11, 'bold'))
            self.lbl2.place(x=570, y=210)

            self.ent1 = Entry(self.reges,font=('Ariel', 11, 'bold'))
            self.ent1.place(x=660, y=210)

            self.lbl3 = Label(self.reges, text='Address', bg='palegreen',font=('Ariel', 11, 'bold'))
            self.lbl3.place(x=570, y=250)

            self.lbl21 = Label(self.reges, text='Phone No.', bg='palegreen',font=('Ariel', 11, 'bold'))
            self.lbl21.place(x=570, y=290)

            self.ent3 = Entry(self.reges,font=('Ariel', 11, 'bold'))
            self.ent3.place(x=660, y=250)

            self.lbl29 = Label(self.reges, text='Email', bg='palegreen',font=('Ariel', 11, 'bold'))
            self.lbl29.place(x=570, y=340)

            self.ent00 = Entry(self.reges,font=('Ariel', 11, 'bold'))
            self.ent00.place(x=660, y=290)

            self.ent2 = Entry(self.reges,font=('Ariel', 10, 'bold'), width='26')
            self.ent2.place(x=640, y=340)

            self.lbl22 = Label(self.reges, text='Password', bg='palegreen',font=('Ariel', 11, 'bold'))
            self.lbl22.place(x=570, y=460)

            self.lbl23 = Label(self.reges, text='Username', bg='palegreen',font=('Ariel', 11, 'bold'))
            self.lbl23.place(x=570, y=420)

            self.ent4 = Entry(self.reges,font=('Ariel', 11, 'bold'))
            self.ent4.place(x=660, y=420)

            self.ent5 = Entry(self.reges,font=('Ariel', 11, 'bold'))
            self.ent5.place(x=660, y=460)

            self.btn01 = Button(self.reges, text='     Register     ', bg='black', fg='white', font=('Ariel', 13, 'bold'),
                                command=self.do_register)
            self.btn01.place(x=640, y=540)

            self.btn03 = Button(self.reges, text='Login Screen', bg='yellow', fg='black',
                                font=('Ariel', 12, 'bold'),command=self.back1)
            self.btn03.place(x=1090, y=540)


            self.reges.mainloop()
        except Exception as e:
            print(e)

    def aft_log(self):

        self.update_index = ''
        username1 = self.ent1.get()
        password1 = self.ent2.get()
        self.window = Tk()
        self.window.title('BOOK CASE')
        self.window.geometry('1920x1080+0+0')
        self.window.configure(bg='darkslategray3')
        self.ab = AddBooks()
        self.see = SeeBooks()
        self.fetch = FetchBill()

        self.lbl111 = Label(self.window, bg='darkslategray1', width=600, height=4,
                            font=('Ariel', 15, 'bold'))
        self.lbl111.place(x=1, y=20)

        self.lbl112 = Label(self.window, text='ORIENTAL BOOK HOUSE', bg='darkslategray1', fg='black',
                            font=('Ariel', 19, 'bold'))
        self.lbl112.place(x=560, y=30)

        self.lbl113 = Label(self.window, bg='darkslategray1', width=40, height=2)
        self.lbl113.place(x=560, y=140)

        self.lbl112 = Label(self.window, text='Bagbazar, Kathmandu', bg='darkslategray1', fg='black',
                            font=('Ariel', 12, 'bold'))
        self.lbl112.place(x=620, y=75)

        self.lbl113 = Label(self.window, bg='darkslategray1', width=16, height=4)
        self.lbl113.place(x=740, y=230)

        self.lbl1131 = Label(self.window, bg='darkslategray1', width=16, height=4)
        self.lbl1131.place(x=540, y=230)

        self.lbl1131 = Label(self.window, bg='darkslategray1', width=16, height=4)
        self.lbl1131.place(x=540, y=430)

        self.lbl1131 = Label(self.window, bg='darkslategray1', width=16, height=4)
        self.lbl1131.place(x=740, y=430)


        self.lbl1 = Label(self.window, text='Choose options', bg='darkslategray1', font=('Ariel', 15, 'bold'))
        self.lbl1.place(x=615, y=145)

        self.book_add = Button(self.window, text="ADD BOOK", command=self.ab.add_gui, bg='black', fg='white',
                               font=('Ariel', 11, 'bold'))
        self.book_add.place(x=550, y=250)

        self.book_buy = Button(self.window, text="BUY BOOK", command=self.buy.buy_gui, bg='black', fg='white',
                               font=('Ariel', 11, 'bold'))
        self.book_buy.place(x=550, y=450)

        self.see_buy = Button(self.window, text="SEE BOOK", command=self.see.see_gui, bg='black', fg='white',
                              font=('Ariel', 11, 'bold'))
        self.see_buy.place(x=750, y=250)

        self.see_bill = Button(self.window, text="SEE BILL", command=self.fetch.fgui, bg='black', fg='white',
                              font=('Ariel', 11, 'bold'),width=9)
        self.see_bill.place(x=750, y=450)

        self.logst = Label(self.window, text='👤',
                             font=('Ariel', 40), bg='darkslategray1', fg='blue')
        self.logst.place(x=1170, y=20)

        self.logname= Label(self.window, text=self.data_base.get_name(username1, password1),font=('Times New Roman', 12, 'italic'),bg='darkslategray1', fg='blue')
        self.logname.place(x=1150, y=90)
        self.main_dis.destroy()
        self.window.mainloop()

    def do_register(self):
        try:


            self.data_base = MyDb()

            username = self.ent4.get()
            password = self.ent5.get()
            name = self.ent1.get()
            address = self.ent3.get()
            phone = self.ent2.get()
            email = self.ent00.get()


            if username == " " or password == '' or name == '' or address == '' or phone == '' or email=='':
                messagebox.showerror("Error", "Enter everyboxes carefully 😒 ")
            else:
                qry = """INSERT INTO registers (username, password, name, address, phone, email)
                                VALUES (%s,%s,%s,%s,%s,%s)"""
                values = (username, password, name, address, phone, email)
                self.data_base.iud(qry, values)

                messagebox.showinfo("Success", "Registered Successfully 😊 ")
                self.send_mail(email)
        except Exception as e:
            print(e)


    def do_login(self):
        self.data_base = MyDb()
        username1 = self.ent1.get()
        password1 = self.ent2.get()
        qry = """SELECT * FROM registers WHERE username = %s and password = %s"""
        values = (username1, password1)
        user = self.data_base.get_data_p(qry, values)

        print(len(user))

        if username1 == " " or password1 == '':
            messagebox.showerror("Error", "Enter everyboxes carefully!")

        else:
            if len(user) == 1:
                messagebox.showinfo('Success', 'BOOM!!  Login successful!')
                self.aft_log()
                self.data_base.get_name(username1, password1)




            else:
                print("Wrong id or password")
                messagebox.showinfo('Sorry', 'INCORRECT Password or id')


    def back1(self):
        self.reges.destroy()
        self.log_in()


    def send_mail(self,email):

        try:

            server = smtplib.SMTP("smtp.gmail.com:587")
            server.ehlo()
            server.starttls()
            server.login('orientalbooksbbz@gmail.com', 'bagbazar')
            message = "Subject: {} {}".format('Hello there!', "You've registered as an admin of ORIENTAL BOOK HOUSE. Thank You!")
            server.sendmail('orientalbooksbbz@gmail.com', email, message)
            server.quit()
            print('Successful!')

        except Exception as e:
            print(e)


Guis()
