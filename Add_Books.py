from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DATABASE import MyDb



class AddBooks:
    def __init__(self):
        self.db=MyDb()
        self.update_index = ""


    def add_gui(self):
        try:
            self.display=Tk()
            self.display.title('ADD BOOKS')
            self.display.geometry('1920x1080+0+0')
            self.display.configure(bg='springgreen2')



            self.lbl111 = Label(self.display, bg='Seagreen1', width=600, height=4,
                               font=('Ariel', 15, 'bold'))
            self.lbl111.place(x=1, y=20)

            self.lbl113 = Label(self.display, bg='Seagreen1', width=60, height=24)
            self.lbl113.place(x=60, y=250)

            self.lbl115 = Label(self.display, bg='Seagreen1', width=68, height=4)
            self.lbl115.place(x=1, y=160)

            self.lbl113 = Label(self.display, bg='Seagreen1', width=40, height=4)
            self.lbl113.place(x=550, y=160)

            self.lbl112 = Label(self.display, text='ORIENTAL BOOK HOUSE', bg='Seagreen1', fg='black',
                                font=('Ariel', 19, 'bold'))
            self.lbl112.place(x=560, y=30)

            self.lbl112 = Label(self.display, text='Bagbazar, Kathmandu', bg='Seagreen1', fg='black',
                                font=('Ariel', 12, 'bold'))
            self.lbl112.place(x=620, y=75)

            self.top1_lbl = Label(self.display, bg='Seagreen1', text='Book Registry', font=('Ariel', 15, 'bold'))
            self.top1_lbl.place(x=190, y=180)


            self.add_name= Label(self.display,bg='Seagreen1', text='Book Name',font=('Ariel', 10, 'bold'))
            self.add_name.place(x=140, y=270)

            self.ent01= Entry(self.display,font=('Ariel', 10))
            self.ent01.place(x=240, y=270)

            self.add_writer = Label(self.display,bg='Seagreen1', text='Writer',font=('Ariel', 10, 'bold'))
            self.add_writer.place(x=140, y=310)

            self.wn_ent = Entry(self.display,font=('Ariel', 10))
            self.wn_ent.place(x=240, y=310)

            self.add_pub = Label(self.display,bg='Seagreen1', text='Publisher',font=('Ariel', 10, 'bold'))
            self.add_pub.place(x=140, y=350)

            self.pub_ent = Entry(self.display,font=('Ariel', 10))
            self.pub_ent.place(x=240, y=350)

            self.add_price = Label(self.display,bg='Seagreen1', text='Price',font=('Ariel', 10, 'bold'))
            self.add_price.place(x=140, y=390)

            self.price_ent = Entry(self.display,font=('Ariel', 10))
            self.price_ent.place(x=240, y=390)

            self.add_cat = Label(self.display,bg='Seagreen1', text='Category',font=('Ariel', 10, 'bold'))
            self.add_cat.place(x=140, y=430)

            self.cat = ttk.Combobox(self.display, text="Category",font=('Ariel', 10))
            self.cat.set('--choose category--')
            self.cat['values']= self.combo()
            self.cat.place(x=240,y=430)


            self.reg_book = Label(self.display,bg='Seagreen1', text='Added Piece',font=('Ariel', 10, 'bold'))
            self.reg_book.place(x=140, y=470)

            self.pie_ent = Entry(self.display, font=('Ariel', 10))
            self.pie_ent.place(x=240, y=470)

            self.rem_book = Label(self.display, bg='Seagreen1', text='Remain Piece',font=('Ariel', 10, 'bold'))
            self.rem_book.place(x=140, y=510)

            self.rem_ent = Entry(self.display, font=('Ariel', 10))
            self.rem_ent.place(x=240, y=510)

            self.ad_book= Button(self.display,text='Add', command=self.addbooks_hand, bg='black', fg='white', width=6, font=('Ariel', 11, 'bold'))
            self.ad_book.place(x=140, y=570)

            self.up_book = Button(self.display, text='Update',bg='black', fg='white',command=self.update_item, font=('Ariel', 11, 'bold'))
            self.up_book.place(x=240, y=570)


            self.del_book = Button(self.display, text='Delete',bg='black', fg='white',command=self.delete_item, font=('Ariel', 11, 'bold'))
            self.del_book.place(x=340, y=570)


            self.top_lbl = Label(self.display,bg='Seagreen1', text='Recently added books',font=('Ariel', 15, 'bold'))
            self.top_lbl.place(x=570, y=180)



            self.add_tree = ttk.Treeview(self.display, column=('n', 'w', 'p', 'm','c','e','r'), height=17)
            self.add_tree.place(x=550, y=250)
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

            self. show_items_in_tree()

            self.ser_book = Button(self.display, bg='yellow', text='Search', font=('Ariel', 10, 'bold'),command=self.searchbook)
            self.ser_book.place(x=1270, y=85)

            self.search_book=Entry(self.display, text='Search', font=('Ariel', 10))
            self.search_book.place(x=1110,y=90)

            self.display.mainloop()
        except Exception as e:
            print (e)



    def addbooks_hand(self):
        try:
            name = self.ent01.get()
            print(name)
            writer = self.wn_ent.get()
            print(writer)
            price = self.price_ent.get()
            print(price)
            publisher = self.pub_ent.get()
            print(publisher)
            reg=self.pie_ent.get()
            rem=self.rem_ent.get()

            catagory= self.cat.get()

            if name == '' or writer == '' or price == '' or publisher == '' or catagory == '' or reg == ''or rem =='':
                messagebox.showerror('Error', 'Fill all the entries !!')
                return False
            elif not price.isdigit():
                messagebox.showerror("Error", "Invalid Price")
                return False

            else:
                self.add_books1(name, writer, price, publisher, catagory, reg, rem)
                messagebox.showinfo("BOOKS", "BOOK Added 😊")
                self.show_items_in_tree()

        except Exception as e:
            print(e)



    def add_books1(self, name, writer, price, publisher, catagory,reg, rem):
        if name == '' or writer == '' or price == '' or publisher == '' or catagory == '' or reg == ''or rem =='':
            return False
        elif not price.isdigit():
            return False
        else:
            qry = "INSERT INTO booksdetail (name, writer, price, publisher,catagory,ent_book, rem_book) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            values = (name, writer, price, publisher, catagory, reg, rem)
            return self.db.iud(qry, values)


    def combo(self):
        qry = '''SELECT catagory FROM catq'''
        combox = self.db.get_data(qry)
        return combox

    def show_items_in_tree(self):
        all_items = self.show_books()
        self.add_tree.delete(*self.add_tree.get_children())
        for i in all_items:
            self.add_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3],i[4],i[5],i[6],i[7]))
        self.add_tree.bind("<Double-1>", self.select_item)

    def show_books(self):
        qry = "SELECT * FROM booksdetail"
        all_books = self.db.get_data(qry)
        return all_books

    def select_item(self, event):
        sel_row = self.add_tree.selection()[0]
        sel_item = self.add_tree.item(sel_row)
        self.update_index = self.add_tree.item(sel_row, 'text')
        selected_data = self.add_tree.item(sel_row, 'values')
        self.ent01.delete(0, 'end')
        self.ent01.insert(0, selected_data[0])
        self.wn_ent.delete(0, 'end')
        self.wn_ent.insert(0, selected_data[1])
        self.price_ent.delete(0, 'end')
        self.price_ent.insert(0, selected_data[2])
        self.cat.delete(0, 'end')
        self.cat.insert(0, selected_data[4])
        self.pub_ent.delete(0, 'end')
        self.pub_ent.insert(0, selected_data[3])
        self.pie_ent.delete(0, 'end')
        self.pie_ent.insert(0, selected_data[5])
        self.rem_ent.delete(0, 'end')
        self.rem_ent.insert(0, selected_data[6])

    def update_books(self, index, name, writer, price, publisher, catagory,reg, rem):
        try:
            qry = "UPDATE booksdetail SET name = %s, writer = %s, price = %s, publisher=%s, catagory=%s, ent_book =%s, rem_book=%s WHERE id = %s"
            values = (name, writer, price, publisher, catagory,reg, rem, index)
            self.db.iud(qry, values)
            return True
        except Exception as e:
            print(e)
            return False

    def update_item(self):
        name = self.ent01.get()
        writer = self.wn_ent.get()
        price = self.price_ent.get()
        publisher = self.pub_ent.get()
        catagory = self.cat.get()
        reg= self.pie_ent.get()
        rem=self.rem_ent.get()

        if self.update_index == "":
            messagebox.showerror("Error", "Select Item first")
        elif not name == '' or writer == '' or price == '' or publisher == '' or catagory == '' or reg == ''or rem =='':

            if self.update_books(int(self.update_index), name, writer, price, publisher, catagory, reg, rem):
                messagebox.showinfo("Item", "Item Updated")
                self.show_items_in_tree()
                print(self.update_index)
            else:
                messagebox.showerror("Error", "Item can not be Updated")

    def delete_books(self, id):
        try:
            qry = "DELETE FROM booksdetail WHERE id = %s"
            values = (id)
            self.db.iud(qry, values)
            return True
        except Exception as e:
            print(e)
            return False

    def delete_item(self):

        name = self.ent01.get()
        writer = self.wn_ent.get()
        price = self.price_ent.get()
        publisher = self.pub_ent.get()
        catagory = self.cat.get()
        reg = self.pie_ent.get()
        rem = self.rem_ent.get()

        if self.update_index == "":
            messagebox.showerror("Error", "Select Item first")
        elif not name == '' or writer == '' or price == '' or publisher == '' or catagory == '' or reg == ''or rem =='':

            self.delete_books(self.del_help(name,publisher))
            messagebox.showinfo("Success", "Delete success")
            self.show_items_in_tree()



    def del_help(self,name, publisher):
        name = self.ent01.get()
        publisher = self.pub_ent.get()

        qry='''select id from booksdetail where name= %s and publisher=%s'''
        values=(name, publisher)
        gett= self.db.get_data_i(qry,values)
        print (gett)
        return gett

    def searchbook(self):
        self.db = MyDb()
        searchbook=self.search_book.get()

        if searchbook=='':
            messagebox.showerror('Empty','Insert some keyword please!')
        else:
            qry = "SELECT * FROM booksdetail WHERE name LIKE '" + searchbook + "%'"
            values = (searchbook)
            result = self.db.get_data_p(qry, values)

            self.add_tree.delete(*self.add_tree.get_children())
            for i in result:
                self.add_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
                self.add_tree.bind("<Double-1>", self.select_item)


