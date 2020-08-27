from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DATABASE import MyDb

class FetchBill:
    def __init__(self):
        self.db=MyDb()

    def fgui(self):
        self.see_dis = Tk()
        self.see_dis.title('SEE BILLS')
        self.see_dis.geometry('1920x1080+0+0')
        self.see_dis.configure(bg='turquoise3')

        self.lbl111 = Label(self.see_dis, bg='turquoise1', width=600, height=4,
                            font=('Ariel', 15, 'bold'))
        self.lbl111.place(x=1, y=20)

        self.lbl113 = Label(self.see_dis, bg='turquoise1', width=60, height=21)
        self.lbl113.place(x=60, y=250)

        self.lbl115 = Label(self.see_dis, bg='turquoise1', width=68, height=4)
        self.lbl115.place(x=1, y=160)

        self.lbl112 = Label(self.see_dis, text='ORIENTAL BOOK HOUSE', bg='turquoise1', fg='black',
                            font=('Ariel', 19, 'bold'))
        self.lbl112.place(x=560, y=30)

        self.lbl112 = Label(self.see_dis, text='Bagbazar, Kathmandu', bg='turquoise1', fg='black',
                            font=('Ariel', 12, 'bold'))
        self.lbl112.place(x=620, y=75)

        self.lbl113 = Label(self.see_dis, bg='turquoise1', width=30, height=4)
        self.lbl113.place(x=580, y=160)

        self.sort_lbl = Label(self.see_dis, text='Search and Sort Bills', bg='turquoise1',
                              font=('Ariel', 16, 'bold'))
        self.sort_lbl.place(x=150, y=180)

        self.sortby_lbl = Label(self.see_dis, text='Search by :', font=('Ariel', 13, 'bold'))
        self.sortby_lbl.place(x=130, y=330)

        self.cat = ttk.Combobox(self.see_dis, text="Category", font=('Ariel', 13), width=16)
        self.cat.place(x=230, y=330)
        self.cat.set('--SELECT FIRST--')
        # opening above saved file to show it on combobox
        # access category from database here---
        # self.cat['values'] =
        # self.cat.grid()
        sortby = ['Book Name', 'Date (yyyy-mm-dd)', 'Bill by']

        self.cat['values'] = sortby

        # self.selectbut = Button(self.see_dis, text='Select', font=('Ariel', 11, 'bold'))
        # self.selectbut.place(x=340, y=360)

        self.search_ent = Entry(self.see_dis, text='Keyword', font=('Ariel', 13, 'bold'), width=18)
        self.search_ent.place(x=230, y=400)

        self.selectbut = Button(self.see_dis, text='Search 🔎', command=self.select,
                                font=('Ariel', 15, 'bold'))
        self.selectbut.place(x=220, y=470)

        self.search_lbl = Label(self.see_dis, text='Keyword :', font=('Ariel', 13, 'bold'))
        self.search_lbl.place(x=130, y=400)

        self.lbl33 = Label(self.see_dis, text='Results', bg='turquoise1', font=('Ariel', 16, 'bold'))
        self.lbl33.place(x=650, y=180)

        self.add_tree = ttk.Treeview(self.see_dis, column=('a', 'b','o', 'c', 'd', 'e', 'f', 'g','h'), height=15)
        self.add_tree.place(x=580, y=250)
        self.add_tree['show'] = 'headings'
        self.add_tree.column('a', width=50)
        self.add_tree.column('b', width=70)
        self.add_tree.column('c', width=100)
        self.add_tree.column('d', width=100)
        self.add_tree.column('e', width=60)
        self.add_tree.column('f', width=60)
        self.add_tree.column('g', width=100)
        self.add_tree.column('h', width=70)
        self.add_tree.column('o', width=150)
        self.add_tree.heading('a', text='Bill Id')
        self.add_tree.heading('b', text='Date')
        self.add_tree.heading('o', text='Book')
        self.add_tree.heading('c', text='Customer Name')
        self.add_tree.heading('d', text='Customer Phone')
        self.add_tree.heading('e', text='Price')
        self.add_tree.heading('f', text='Discount')
        self.add_tree.heading('g', text='Total')
        self.add_tree.heading('h', text='Bill by')

        self.dataa()

        self.see_dis.mainloop()

    def select(self):
        self.db = MyDb()
        user_chosen = self.cat.get()

        if user_chosen == '':
            messagebox.showerror('Error', 'Select first')


        elif user_chosen == 'Book Name':
            keyword= self.search_ent.get()
            qry = "SELECT * FROM bill WHERE bookname LIKE '" + keyword + "%'"
            values = (keyword)
            result = self.db.get_data_p(qry, values)

            self.add_tree.delete(*self.add_tree.get_children())
            for i in result:
                self.add_tree.insert("", "end", text=i[0], value=(i[0], i[7], i[9], i[1], i[2], i[4], i[5],i[6],i[8]))



        elif user_chosen == 'Date (yyyy-mm-dd)':
            keyword = self.search_ent.get()
            qry = "SELECT * FROM bill WHERE date LIKE '" + keyword + "%'"
            values = (keyword)
            result = self.db.get_data_p(qry, values)

            self.add_tree.delete(*self.add_tree.get_children())
            for i in result:
                self.add_tree.insert("", "end", text=i[0], value=(i[0], i[7], i[9], i[1], i[2], i[4], i[5],i[6],i[8]))


        elif user_chosen == 'Bill by':
            keyword = self.search_ent.get()
            qry = "SELECT * FROM bill WHERE bill_by LIKE '" + keyword + "%'"
            values = (keyword)
            result = self.db.get_data_p(qry, values)

            self.add_tree.delete(*self.add_tree.get_children())
            for i in result:
                self.add_tree.insert("", "end", text=i[0], value=(i[0], i[7], i[9], i[1], i[2], i[4], i[5],i[6],i[8]))



    def dataa(self):
        self.db=MyDb()
        qry='''select * from bill'''
        data=self.db.get_data(qry)

        self.add_tree.delete(*self.add_tree.get_children())
        for i in data:
            self.add_tree.insert("", "end", text=i[0], value=(i[0], i[7], i[9], i[1], i[2], i[4], i[5], i[6], i[8]))




