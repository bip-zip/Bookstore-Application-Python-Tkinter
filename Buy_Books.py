from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DATABASE import MyDb
from Add_Books import AddBooks
from See_Books import *
from datetime import date
#from Application import Guis

class BuyBooks(SeeBooks):
    def __init__(self):

        super().__init__()
        self.see=SeeBooks()
        self.db=MyDb()
        #self.app = Guis()



    def buy_gui(self):
        self.buy_dis = Tk()
        self.buy_dis.title('BUY BOOKS')
        self.buy_dis.geometry('1920x1080')
        self.buy_dis.configure(bg='dark orange3')

        self.see = SeeBooks()

        self.lbl111 = Label(self.buy_dis, bg='dark orange1', width=600, height=4,
                            font=('Ariel', 15, 'bold'))
        self.lbl111.place(x=1, y=20)

        self.lbl113 = Label(self.buy_dis, bg='dark orange1', width=60, height=12)
        self.lbl113.place(x=60, y=250)


        self.lbl116 = Label(self.buy_dis, bg='dark orange1', width=60, height=14)
        self.lbl116.place(x=60, y=460)

        self.lbl115 = Label(self.buy_dis, bg='dark orange1', width=68, height=4)
        self.lbl115.place(x=1, y=160)

        self.lbl113 = Label(self.buy_dis, bg='dark orange1', width=40, height=4)
        self.lbl113.place(x=600, y=160)

        self.lbl118 = Label(self.buy_dis, bg='dark orange1', width=600, height=4)
        self.lbl118.place(x=600, y=600)

        self.lbl112 = Label(self.buy_dis, text='ORIENTAL BOOK HOUSE', bg='dark orange1', fg='black',
                            font=('Ariel', 19, 'bold'))
        self.lbl112.place(x=560, y=30)

        self.lbl112 = Label(self.buy_dis, text='Bagbazar, Kathmandu', bg='dark orange1', fg='black',
                            font=('Ariel', 13, 'bold'))
        self.lbl112.place(x=620, y=75)
        self.sort_lbl = Label(self.buy_dis, text='Search and Sort Books', bg='dark orange1', font=('Ariel', 16, 'bold'))
        self.sort_lbl.place(x=110, y=180)

        self.sortby_lbl = Label(self.buy_dis, text='Search by :', font=('Ariel', 13, 'bold'))
        self.sortby_lbl.place(x=130, y=270)

        self.cat = ttk.Combobox(self.buy_dis, text="Category",font=('Ariel', 13),width=16)
        self.cat.place(x=230, y=270)
        self.cat.set('----SELECT FIRST----')
        # opening above saved file to show it on combobox
        # access category from database here---
        # self.cat['values'] =
        # self.cat.grid()
        sortby = ['Name', 'Writer', 'Publisher', 'Catagory']

        self.cat['values'] = sortby

        self.selectbut = Button(self.buy_dis, text='Select', command=self.select,font=('Ariel', 11, 'bold'))
        self.selectbut.place(x=340, y=300)

        self.lbl33=Label(self.buy_dis,text='Results:',bg='dark orange1', font=('Ariel', 16, 'bold'))
        self.lbl33.place(x=650, y=180)

        self.add_tree = ttk.Treeview(self.buy_dis, column=('n', 'w', 'p', 'm', 'c'))
        self.add_tree.place(x=600, y=250)
        self.add_tree['show'] = 'headings'
        self.add_tree.column('n', width=200)
        self.add_tree.column('w', width=100)
        self.add_tree.column('p', width=100)
        self.add_tree.column('m', width=100)
        self.add_tree.column('c', width=100)
        self.add_tree.heading('n', text='Book')
        self.add_tree.heading('w', text='Writer')
        self.add_tree.heading('p', text='Price')
        self.add_tree.heading('m', text='Publisher')
        self.add_tree.heading('c', text='Catagory')

        self.start_tree()


        self.lbl22 = Label(self.buy_dis, text='*Selected', bg='dark orange1', font=('Ariel', 10, 'bold'))
        self.lbl22.place(x=130, y=470)

        self.get1 = Label(self.buy_dis, text='Book :', font=('Ariel', 13, 'bold'), width=9)
        self.get1.place(x=130, y=500)

        self.get1 = Label(self.buy_dis, text='Price :', font=('Ariel', 13, 'bold'), width=9)
        self.get1.place(x=130, y=540)

        self.get1 = Label(self.buy_dis, text='Dis % :', font=('Ariel', 13, 'bold'), width=9)
        self.get1.place(x=130, y=580)

        self.nament = Entry(self.buy_dis, font=('Ariel', 13, 'bold'), width=18)
        self.nament.place(x=230, y=500)

        self.priceent = Entry(self.buy_dis, font=('Ariel', 13, 'bold'), width=18)
        self.priceent.place(x=230, y=540)

        self.disent = Entry(self.buy_dis, font=('Ariel', 13, 'bold'), width=18)
        self.disent.place(x=230, y=580)

        self.addbill = Button(self.buy_dis, text="Calculate", command=self.bills, font=('Ariel', 11, 'bold'))
        self.addbill.place(x=390, y=620)


        self.back=Button(self.buy_dis, text="Back", command=self.backbut, bg='green', font=('Ariel', 9, 'bold'))
        self.back.place(x=1290,y=620)

        self.buy_dis.mainloop()


    def select(self):
        self.ab = AddBooks()

        user_chosen = self.cat.get()

        if user_chosen == '':
            messagebox.showerror('Error', 'Select first')


        elif user_chosen == 'Name':
            self.search_ent = Entry(self.buy_dis, text='Keyword', font=('Ariel', 13, 'bold'), width=18)
            self.search_ent.place(x=230, y=350)

            self.selectbut = Button(self.buy_dis, text='Search', command=self.tree_byname,
                                    font=('Ariel', 11, 'bold'))
            self.selectbut.place(x=335, y=380)

            self.search_lbl = Label(self.buy_dis, text='Keyword :', font=('Ariel', 13, 'bold'))
            self.search_lbl.place(x=130, y=350)

            # self.lbl22=Label (self.buy_dis, text='*Selected',bg='dark orange1', font=('Ariel', 10, 'bold'))
            # self.lbl22.place(x=130, y=470)
            #
            # self.get1=Label(self.buy_dis, text='Book :',font=('Ariel', 13, 'bold'),width=9)
            # self.get1.place(x=130, y=500)
            #
            # self.get1 = Label(self.buy_dis, text='Price :',font=('Ariel', 13, 'bold'),width=9)
            # self.get1.place(x=130, y=540)
            #
            # self.get1 = Label(self.buy_dis, text='Dis % :',font=('Ariel', 13, 'bold'),width=9)
            # self.get1.place(x=130, y=580)
            #
            # self.nament=Entry(self.buy_dis,font=('Ariel', 13, 'bold'), width=18)
            # self.nament.place(x=230, y=500)
            #
            #
            # self.priceent = Entry(self.buy_dis,font=('Ariel', 13, 'bold'), width=18)
            # self.priceent.place(x=230, y=540)
            #
            #
            # self.disent = Entry(self.buy_dis,font=('Ariel', 13, 'bold'), width=18)
            # self.disent.place(x=230, y=580)
            #
            # self.addbill= Button(self.buy_dis, text="Calculate", command=self.bills, font=('Ariel', 11, 'bold'))
            # self.addbill.place(x=390, y=620)




        elif user_chosen == 'Writer':

            self.search_ent = Entry(self.buy_dis, text='Keyword', font=('Ariel', 13, 'bold'), width=18)
            self.search_ent.place(x=230, y=350)

            self.selectbut = Button(self.buy_dis, text='Search', command=self.tree_bywriter,
                                    font=('Ariel', 11, 'bold'))
            self.selectbut.place(x=335, y=380)

            self.search_lbl = Label(self.buy_dis, text='Keyword :', font=('Ariel', 13, 'bold'))
            self.search_lbl.place(x=130, y=350)

            # self.lbl22 = Label(self.buy_dis, text='*Selected', bg='dark orange1', font=('Ariel', 10, 'bold'))
            # self.lbl22.place(x=130, y=470)
            #
            # self.get1 = Label(self.buy_dis, text='Book :', font=('Ariel', 13, 'bold'), width=9)
            # self.get1.place(x=130, y=500)
            #
            # self.get1 = Label(self.buy_dis, text='Price :', font=('Ariel', 13, 'bold'), width=9)
            # self.get1.place(x=130, y=540)
            #
            # self.get1 = Label(self.buy_dis, text='Dis % :', font=('Ariel', 13, 'bold'), width=9)
            # self.get1.place(x=130, y=580)
            #
            # self.nament = Entry(self.buy_dis, font=('Ariel', 13, 'bold'), width=18)
            # self.nament.place(x=230, y=500)
            #
            # self.priceent = Entry(self.buy_dis, font=('Ariel', 13, 'bold'), width=18)
            # self.priceent.place(x=230, y=540)
            #
            # self.disent = Entry(self.buy_dis, font=('Ariel', 13, 'bold'), width=18)
            # self.disent.place(x=230, y=580)
            #
            # self.addbill = Button(self.buy_dis, text="Calculate", command=self.bills, font=('Ariel', 11, 'bold'))
            # self.addbill.place(x=390, y=620)

        elif user_chosen == 'Publisher':

            self.search_ent = Entry(self.buy_dis, text='Keyword', font=('Ariel', 13, 'bold'), width=18)
            self.search_ent.place(x=230, y=350)

            self.selectbut = Button(self.buy_dis, text='Search', command=self.tree_bypublisher,
                                    font=('Ariel', 11, 'bold'))
            self.selectbut.place(x=335, y=380)

            self.search_lbl = Label(self.buy_dis, text='Keyword :', font=('Ariel', 13, 'bold'))
            self.search_lbl.place(x=130, y=350)

            # self.lbl22 = Label(self.buy_dis, text='*Selected', bg='dark orange1', font=('Ariel', 10, 'bold'))
            # self.lbl22.place(x=130, y=470)
            #
            # self.get1 = Label(self.buy_dis, text='Book :', font=('Ariel', 13, 'bold'), width=9)
            # self.get1.place(x=130, y=500)
            #
            # self.get1 = Label(self.buy_dis, text='Price :', font=('Ariel', 13, 'bold'), width=9)
            # self.get1.place(x=130, y=540)
            #
            # self.get1 = Label(self.buy_dis, text='Dis % :', font=('Ariel', 13, 'bold'), width=9)
            # self.get1.place(x=130, y=580)
            #
            # self.nament = Entry(self.buy_dis, font=('Ariel', 13, 'bold'), width=18)
            # self.nament.place(x=230, y=500)
            #
            # self.priceent = Entry(self.buy_dis, font=('Ariel', 13, 'bold'), width=18)
            # self.priceent.place(x=230, y=540)
            #
            # self.disent = Entry(self.buy_dis, font=('Ariel', 13, 'bold'), width=18)
            # self.disent.place(x=230, y=580)
            #
            # self.addbill = Button(self.buy_dis, text="Calculate", command=self.bills, font=('Ariel', 11, 'bold'))
            # self.addbill.place(x=390, y=620)

        elif user_chosen == 'Catagory':

            values = self.ab.combo()

            self.search_ent = ttk.Combobox(self.buy_dis, text='Keyword', font=('Ariel', 13, 'bold'), width=16,values=values)
            self.search_ent.place(x=230, y=350)

            self.selectbut = Button(self.buy_dis, text='Search', command=self.tree_bycatagory,
                                    font=('Ariel', 11, 'bold'))
            self.selectbut.place(x=335, y=380)

            self.search_lbl = Label(self.buy_dis, text='Keyword :', font=('Ariel', 13, 'bold'))
            self.search_lbl.place(x=130, y=350)

            # self.lbl22 = Label(self.buy_dis, text='*Selected', bg='dark orange1', font=('Ariel', 10, 'bold'))
            # self.lbl22.place(x=130, y=470)
            #
            # self.get1 = Label(self.buy_dis, text='Book :', font=('Ariel', 13, 'bold'), width=9)
            # self.get1.place(x=130, y=500)
            #
            # self.get1 = Label(self.buy_dis, text='Price :', font=('Ariel', 13, 'bold'), width=9)
            # self.get1.place(x=130, y=540)
            #
            # self.get1 = Label(self.buy_dis, text='Dis % :', font=('Ariel', 13, 'bold'), width=9)
            # self.get1.place(x=130, y=580)
            #
            # self.nament = Entry(self.buy_dis, font=('Ariel', 13, 'bold'), width=18)
            # self.nament.place(x=230, y=500)
            #
            # self.priceent = Entry(self.buy_dis, font=('Ariel', 13, 'bold'), width=18)
            # self.priceent.place(x=230, y=540)
            #
            # self.disent = Entry(self.buy_dis, font=('Ariel', 13, 'bold'), width=18)
            # self.disent.place(x=230, y=580)
            #
            # self.addbill = Button(self.buy_dis, text="Calculate", command=self.bills, font=('Ariel', 11, 'bold'))
            # self.addbill.place(x=390, y=620)

        else:
            messagebox.showinfo("No Selection",'Select First!!')

    def start_tree(self):
        all_items= self.db.all_books()

        self.add_tree.delete(*self.add_tree.get_children())
        for i in all_items:
            self.add_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5]))
            self.add_tree.bind("<Double-1>", self.select_item)

    def tree_byname(self):
        name = self.search_ent.get()
        all_items= self.db.searchbyname(name)

        self.add_tree.delete(*self.add_tree.get_children())
        for i in all_items:
            self.add_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5]))
            self.add_tree.bind("<Double-1>", self.select_item)

    def tree_bywriter(self):
        writer = self.search_ent.get()
        all_items= self.db.searchbywriter(writer)

        self.add_tree.delete(*self.add_tree.get_children())
        for i in all_items:
            self.add_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5]))
            self.add_tree.bind("<Double-1>", self.select_item)


    def tree_bypublisher(self):
        publisher = self.search_ent.get()
        all_items= self.db.searchbypublisher(publisher)

        self.add_tree.delete(*self.add_tree.get_children())
        for i in all_items:
            self.add_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5]))
            self.add_tree.bind("<Double-1>", self.select_item)


    def tree_bycatagory(self):
        catagory = self.search_ent.get()
        all_items= self.db.searchbycatagory(catagory)

        self.add_tree.delete(*self.add_tree.get_children())
        for i in all_items:
            self.add_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5]))
            self.add_tree.bind("<Double-1>", self.select_item)

    def select_item(self, event):
        sel_row = self.add_tree.selection()[0]
        sel_item = self.add_tree.item(sel_row)
        self.update_index = self.add_tree.item(sel_row, 'text')
        selected_data = self.add_tree.item(sel_row, 'values')
        self.nament.delete(0, 'end')
        self.nament.insert(0, selected_data[0])
        self.priceent.delete(0, 'end')
        self.priceent.insert(0, selected_data[2])

    def bills(self):
        discount=self.disent.get()

        if discount == '':
            messagebox.showerror('Error','Enter discount percentage first!')

        else:
            money = float(self.priceent.get())
            discount = float(self.disent.get())

            self.addbilllbl = Label(self.buy_dis, text='TOTAL: ',font=('Ariel', 15, 'bold'),fg='dark green')
            self.addbilllbl.place(x=680, y=620)


            self.addbillent = Entry(self.buy_dis, width=10, bg='black',fg='white',font=('Ariel', 15, 'bold'))
            self.addbillent.place(x=770, y=620)

            dis= discount/100
            tt= money * dis

            global total
            total= money - tt
            print(total)

            self.addbillent.insert(0, total)

            self.bill_button= Button(self.buy_dis, bg='blue', fg='white', command=self.bill_gui, text='Add to Bills',font=('Ariel', 11, 'bold'))
            self.bill_button.place(x=1100,y=618)




    def bill_gui(self):

        self.bill_dis = Tk()
        self.bill_dis.title('BILLING')
        self.bill_dis.geometry('600x350')
        self.bill_dis.configure(bg='sky blue2')

        self.lbl_ = Label(self.bill_dis, text='ORIENTAL BOOK HOUSE', fg='maroon', bg='sky blue2',font=('Ariel', 15, 'bold'))
        self.lbl_.place(x=200, y=30)

        self._lbl = Label(self.bill_dis, text='Estimate Bill', bg='sky blue2', font=('Ariel', 12, 'bold'))
        self._lbl.place(x=270, y=70)

        self.date_lbl=Label(self.bill_dis, text='Date: ', bg='sky blue2')
        self.date_lbl.place(x=445, y=100)

        self.date_ent = Entry(self.bill_dis, width=10)
        self.date_ent.place(x=480, y=100)

        self.cust_name = Label(self.bill_dis, text="Customer's Name ", bg='sky blue2',font=('Ariel', 8, 'bold') )
        self.cust_name.place(x=30, y=140)

        self.cust_phone = Label(self.bill_dis, text="Customer's Phone ", bg='sky blue2', font=('Ariel', 8, 'bold'))
        self.cust_phone.place(x=150, y=140)

        self.booki = Label(self.bill_dis, text="Book ", bg='sky blue2', font=('Ariel', 8, 'bold'))
        self.booki.place(x=295, y=140)

        self.prici = Label(self.bill_dis, text="Price ", bg='sky blue2', font=('Ariel', 8, 'bold'))
        self.prici.place(x=390, y=140)

        self.disc = Label(self.bill_dis, text="discount %", bg='sky blue2', font=('Ariel', 8, 'bold'))
        self.disc.place(x=430, y=140)

        self.amt = Label(self.bill_dis, text="Tot. Amount", bg='sky blue2', font=('Ariel', 8, 'bold'))
        self.amt.place(x=500, y=140)

        self.cus_name=Entry(self.bill_dis, width=15)
        self.cus_name.place(x=30, y=170)

        self.cus_phn = Entry(self.bill_dis, width=15)
        self.cus_phn.place(x=150, y=170)

        self.book_ent = Entry(self.bill_dis)
        self.book_ent.place(x=260, y=170)

        self.pr_ent = Entry(self.bill_dis,width=6)
        self.pr_ent.place(x=390, y=170)

        self.dis_ent = Entry(self.bill_dis,width=6)
        self.dis_ent.place(x=440, y=170)

        self.tot_ent = Entry(self.bill_dis,width=10)
        self.tot_ent.place(x=500, y=170)

        com=['Bipin','Kishan','Badri','Hari']
        self.billby = ttk.Combobox(self.bill_dis, font=('Ariel', 9),width=8, values=com)
        self.billby.place(x=420, y=270)

        self.billby_lbl=Label(self.bill_dis,text="Bill by: ")
        self.billby_lbl.place(x=360,y=270)


        self.st_button = Button(self.bill_dis, bg='black', fg='white',text='Store',command=self.billdb, font=('Ariel', 10, 'bold'))
        self.st_button.place(x=520, y=270)

        money = float(self.priceent.get())
        bookss=self.nament.get()
        discount = float(self.disent.get())
        today = date.today()
        #billcutter= self.app.getname()

        self.book_ent.insert(0, bookss)
        self.pr_ent.insert(0, money)
        self.dis_ent.insert(0, discount)
        self.tot_ent.insert(0, total)
        self.date_ent.insert(0,today)
        #self.billby.insert(0,billcutter)


        self.bill_dis.mainloop()

    def billdb(self):
        cus_name = self.cus_name.get()
        print(cus_name)
        cus_phone = self.cus_phn.get()
        booko = self.book_ent.get()
        #bookid----methoddatabase
        price = self.pr_ent.get()
        bookido = self.bookid(booko, price)
        discount = self.dis_ent.get()
        total = self.tot_ent.get()
        date = self.date_ent.get()
        book = self.book_ent.get()
        billby=self.billby.get()

        if cus_name == '' or cus_phone == '' or price == '' or discount == '' or total== ''or date == '' or billby=='':
            messagebox.showerror('Error', 'Fill all the entries !!')
            return False

        else:
            self.databill(cus_name,cus_phone,bookido,price,discount, total,date,book,billby)
            messagebox.showinfo("Done", "Bill Added 😊")


    def databill(self,cus_name,cus_phone,bookid,price,discount, total,date,book,billby):
        self.db = MyDb()
        qry = "INSERT INTO bill (cus_name, cus_phone, book, price, discount, total,date,bookname,bill_by) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (cus_name,cus_phone,bookid,price,discount, total,date,book,billby)
        return self.db.iud(qry, values)


    def bookid(self,book, price):
        self.db = MyDb()
        book = self.book_ent.get()
        price = self.pr_ent.get()
        print(book)
        print(price)
        qry = '''select id from booksdetail where name=%s and price=%s'''
        values = (book,price)
        get= self.db.get_data_i(qry, values)
        print(type(get))
        bipin =int(get[0])
        print(type(bipin))
        return bipin


    def backbut(self):
        self.buy_dis.destroy()



# a=BuyBooks()
# a.buy_gui()