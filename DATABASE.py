import mysql.connector

class MyDb:
    def __init__(self):

        self.my_connection = mysql.connector.connect(
            user='root', host='localhost', password='1234', port=3306, database='cs19d')
        self.my_cursor = self.my_connection.cursor()

    def iud(self, qry, values):
        self.my_cursor.execute(qry, values)
        self.my_connection.commit()

    def insert_with_id_return(self, qry, values):
        self.my_cursor.execute(qry, values)
        self.my_connection.commit()
        return self.my_cursor.lastrowid

    def insert_multiple_row(self, qry, values): #values is a list
        self.my_cursor.executemany(qry, values)
        self.my_connection.commit()

    def get_data(self, qry):
        self.my_cursor.execute(qry)
        data = self.my_cursor.fetchall()
        print(data)
        return data

    def get_data_p(self, qry, values):
        self.my_cursor.execute(qry, values)
        data = self.my_cursor.fetchall()
        return data

    def get_data_i(self, qry, values):
        self.my_cursor.execute(qry, values)
        data = self.my_cursor.fetchone()
        return data

    def searchbyname(self,keyword):
        qry = "SELECT * FROM booksdetail WHERE name LIKE '" + keyword + "%'"
        all_items = self.get_data(qry)
        print(all_items)
        return all_items


    def searchbywriter(self,keyword):
        qry = "SELECT * FROM booksdetail WHERE writer LIKE '" + keyword + "%'"
        all_items = self.get_data(qry)
        print(all_items)
        return all_items

    def searchbypublisher(self,keyword):
        qry = "SELECT * FROM booksdetail WHERE publisher LIKE '" + keyword + "%'"
        all_items = self.get_data(qry)
        print(all_items)
        return all_items

    def searchbycatagory(self,keyword):
        qry = "SELECT * FROM booksdetail WHERE catagory LIKE '" + keyword + "%'"
        all_items = self.get_data(qry)
        print(all_items)
        return all_items

    def get_name(self,username,password):
        qry = '''select name from registers where username = %s and password = %s'''
        values = (username, password)
        billing = self.get_data_i(qry, values)
        billname = (billing[0])
        print(billname,'has logged in')
        return billname

    def all_books(self):
        qry = '''select * from booksdetail'''
        result=self.get_data(qry)
        return result






#tty=MyDb()
##tul=tty.ola('bipin44','rollon')
#if len(tul) == 0:
    #print("Login successful")
#else:
    #print("Wrong id or password")



# qry = "CREATE DATABASE cs19d"
# qry = "CREATE TABLE items (id int PRIMARY KEY AUTO_INCREMENT, name varchar(100), " \
#       "type varchar(100), price double)"
# qry = "INSERT INTO items (name, type, price) VALUES ('Burger', 'Chicken', 130)"
# my_cursor.execute(qry)
# my_connection.commit()

# qry = "SELECT * FROM items"
# my_cursor.execute(qry)
# all_items = my_cursor.fetchall()
# for i in all_items:
#     print(i)
