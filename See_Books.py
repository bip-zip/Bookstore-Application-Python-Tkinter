from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DATABASE import MyDb
from Add_Books import *

class SeeBooks:
    def __init__(self):
        self.db=MyDb()
        self.ab=AddBooks()


    def see_gui(self):
        self.see_dis = Tk()
        self.see_dis.title('SEE BOOKS')
        self.see_dis.geometry('1920x1080+0+0')
        self.see_dis.configure(bg='purple3')

        self.lbl111 = Label(self.see_dis, bg='medium purple1', width=600, height=4,
                            font=('Ariel', 15, 'bold'))
        self.lbl111.place(x=1, y=20)

        self.lbl113 = Label(self.see_dis, bg='medium purple2', width=60, height=21)
        self.lbl113.place(x=60, y=250)

        self.lbl115 = Label(self.see_dis, bg='medium purple1', width=68, height=4)
        self.lbl115.place(x=1, y=160)

        self.lbl112 = Label(self.see_dis, text='ORIENTAL BOOK HOUSE',bg='medium purple1',fg='black',
                           font=('Ariel', 19, 'bold'))
        self.lbl112.place(x=560, y=30)

        self.lbl112 = Label(self.see_dis, text='Bagbazar, Kathmandu', bg='medium purple1', fg='black',
                            font=('Ariel', 12, 'bold'))
        self.lbl112.place(x=620, y=75)

        self.lbl113 = Label(self.see_dis, bg='medium purple1', width=30, height=4)
        self.lbl113.place(x=580, y=160)

        self.sort_lbl = Label(self.see_dis, text='Search and Sort Books', bg='medium purple1', font=('Ariel', 16, 'bold'))
        self.sort_lbl.place(x=150, y=180)

        self.sortby_lbl= Label(self.see_dis, text='Search by :',font=('Ariel', 13, 'bold'))
        self.sortby_lbl.place(x=130, y=330)

        self.cat = ttk.Combobox(self.see_dis, text="Category",font=('Ariel', 13 ), width=16)
        self.cat.place(x=230, y=330)
        self.cat.set('--SELECT FIRST--')
        # opening above saved file to show it on combobox
        # access category from database here---
        # self.cat['values'] =
        # self.cat.grid()
        sortby=['Name', 'Writer', 'Publisher', 'Catagory']

        self.cat['values'] = sortby

        self.selectbut= Button(self.see_dis, text='Select', command=self.select,font=('Ariel', 11, 'bold'))
        self.selectbut.place(x=340, y=360)

        self.lbl33 = Label(self.see_dis, text='Results', bg='medium purple1', font=('Ariel', 16, 'bold'))
        self.lbl33.place(x=650, y=180)

        self.add_tree = ttk.Treeview(self.see_dis, column=('n', 'w', 'p', 'm', 'c','e','r'),height=15)
        self.add_tree.place(x=580, y=250)
        self.add_tree['show'] = 'headings'
        self.add_tree.column('n', width=200)
        self.add_tree.column('w', width=100)
        self.add_tree.column('p', width=100)
        self.add_tree.column('m', width=100)
        self.add_tree.column('c', width=100)
        self.add_tree.column('e', width=70)
        self.add_tree.column('r', width=70)
        self.add_tree.heading('n', text='Book')
        self.add_tree.heading('w', text='Writer')
        self.add_tree.heading('p', text='Price')
        self.add_tree.heading('m', text='Publisher')
        self.add_tree.heading('c', text='Catagory')
        self.add_tree.heading('e', text='Reg-piece')
        self.add_tree.heading('r', text='Rem-piece')

        self.start_tree()




        self.see_dis.mainloop()


    def select(self):
        self.ab = AddBooks()
        user_chosen = self.cat.get()

        if user_chosen == '':
            messagebox.showerror('Error', 'Select first')


        elif user_chosen == 'Name':
            self.search_ent = Entry(self.see_dis, text='Keyword', font=('Ariel', 13, 'bold'), width=18)
            self.search_ent.place(x=230, y=400)

            self.selectbut = Button(self.see_dis, text='Search 🔎', command=self.tree_byname,
                                    font=('Ariel', 15, 'bold'))
            self.selectbut.place(x=220, y=470)

            self.search_lbl = Label(self.see_dis, text='Keyword :', font=('Ariel', 13, 'bold'))
            self.search_lbl.place(x=130, y=400)


        elif user_chosen == 'Writer':

            self.search_ent = Entry(self.see_dis, text='Keyword',font=('Ariel', 13, 'bold'),width=18)
            self.search_ent.place(x=230, y=400)

            self.selectbut = Button(self.see_dis, text='Search 🔎', command=self.tree_bywriter,font=('Ariel', 15, 'bold') )
            self.selectbut.place(x=220, y=470)

            self.search_lbl = Label(self.see_dis, text='Keyword :',font=('Ariel', 13, 'bold'))
            self.search_lbl.place(x=130, y=400)

        elif user_chosen == 'Publisher':

            self.search_ent = Entry(self.see_dis, text='Keyword', font=('Ariel', 13, 'bold'), width=18)
            self.search_ent.place(x=230, y=400)

            self.selectbut = Button(self.see_dis, text='Search 🔎', command=self.tree_bypublisher,
                                    font=('Ariel', 15, 'bold'))
            self.selectbut.place(x=220, y=470)

            self.search_lbl = Label(self.see_dis, text='Keyword :', font=('Ariel', 13, 'bold'))
            self.search_lbl.place(x=130, y=400)
        elif user_chosen == 'Catagory':

            values=self.ab.combo()

            self.search_ent = ttk.Combobox(self.see_dis, values=values,font=('Ariel', 13), width=16)
            self.search_ent.set('--Choose--')
            self.search_ent.place(x=230, y=400)


            self.selectbut = Button(self.see_dis, text='Search 🔎', command=self.tree_bycatagory,
                                    font=('Ariel', 15, 'bold'))
            self.selectbut.place(x=220, y=470)

            self.search_lbl = Label(self.see_dis, text='Keyword :', font=('Ariel', 13, 'bold'))
            self.search_lbl.place(x=130, y=400)
        else:
            messagebox.showinfo("No Selection",'Select First!!')







    def tree_byname(self):
        name = self.search_ent.get()
        all_items= self.db.searchbyname(name)

        self.add_tree.delete(*self.add_tree.get_children())
        for i in all_items:
            self.add_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5],i[6],i[7]))

    def tree_bywriter(self):
        writer = self.search_ent.get()
        all_items= self.db.searchbywriter(writer)

        self.add_tree.delete(*self.add_tree.get_children())
        for i in all_items:
            self.add_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5],i[6],i[7]))


    def tree_bypublisher(self):
        publisher = self.search_ent.get()
        all_items= self.db.searchbypublisher(publisher)

        self.add_tree.delete(*self.add_tree.get_children())
        for i in all_items:
            self.add_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6],i[7]))


    def tree_bycatagory(self):
        catagory = self.search_ent.get()
        all_items= self.db.searchbycatagory(catagory)

        self.add_tree.delete(*self.add_tree.get_children())
        for i in all_items:
            self.add_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6],i[7]))


    def start_tree(self):
        try:
            all_items=self.db.all_books()

            self.add_tree.delete(*self.add_tree.get_children())
            for i in all_items:
                self.add_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
        except Exception as e:
            print(e)










