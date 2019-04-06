import os
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import tkinter.scrolledtext as tkst
from tkinter import filedialog
import csv1
import datetime
conn = sqlite3.connect('abc_manufaturer.db')
c=conn.cursor()


root = Tk()
root.geometry('350x250')

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        def userpage():
            root.title('ABC Manufacturer')
            userpage = Toplevel(root)
            userpage.geometry('750x600')
            userpage.config(bg='cyan')
            s = ttk.Style()
            s.configure('my.TFrame', background='cyan')
            nb = ttk.Notebook(userpage, name='nb', style='my.TFrame', width=1200, height=800)
            nb.place(x=10, y=10)

            Frame = ttk.Frame(nb, name='tab', style='my.TFrame')
            nb.add(Frame, text='   Order Page   ')

            Frame1 = ttk.Frame(nb, name='tab1', style='my.TFrame')
            nb.add(Frame1, text='   Stock Page   ')

            Frame2 = ttk.Frame(nb, name='tab2', style='my.TFrame')
            nb.add(Frame2, text='   Product status Page   ')

            Frame3 = ttk.Frame(nb, name='tab3', style='my.TFrame')
            nb.add(Frame3, text='   Feedback System Page   ')

            nb.select(Frame)

            global account

            #order function
            def showproduct():
                c.execute("SELECT * FROM products Order by item_id ASC")
                rows = c.fetchall()
                for row in rows:
                    print(row)  # it print all records in the database
                    tree.insert("", tk.END, values=row)

            def searchitem():
                itemname = str(searchp_ey.get())
                c.execute("SELECT * FROM products where item_name like'%" + itemname + "%'")
                itemname1 = c.fetchall()
                for i in tree.get_children():
                    tree.delete(i)
                for item in itemname1:
                    tree.insert('', 0, values=(item))

            def showitems():
                c.execute("SELECT * FROM products Order by item_id ASC")
                rows = c.fetchall()
                for i in tree.get_children():
                    tree.delete(i)
                for row in rows:
                    print(row)  # it print all records in the database
                    tree.insert("", tk.END, values=row)

            def on_tree_select(event):
                item = tree.focus()
                # item = tree.selection()[1]
                abc = (tree.item(item)['values'][0])
                # print(str(abc))
                selected_ey.delete(0, 'end')
                selected_ey.insert(0, abc)
            #Ordersystem
            def purchasing():
                order1="ORD"
                c.execute("SELECT Count(*) FROM order_table Order by item_id ASC")
                existOrder = c.fetchall()[0]
           # print(existOrder[0])
                order2= existOrder[0] + 1
                if order2 < 10:
                    order2 =  "0000"+str(order2)
                elif order2 <100:
                    order2 = "000"+str(order2)
                elif order2 <1000:
                    order2 = "00" + str(order2)
                elif order2 < 10000:
                    order2 = "0" + str(order2)
                else:
                    order2 = str(order2)
                    #print(order2)
                order_id = str(order1) + order2
           #print(order_id)
                order_date = datetime.date.today()
           # print(order_date)
                item_id = selected_ey.get()

                if item_id == "":
                    messagebox.showerror("Error", "Please select product.")
                    return
                else:
                    c.execute("SELECT item_id FROM products where item_id = '" + item_id + "'")
                    stored_id = c.fetchone()
                    if stored_id != None:
                        stored_id1 = stored_id
                        print(stored_id)
                    else:
                        messagebox.showerror("Error", "Worng product id.")
                        return
                if str(stored_id1) == None:
                    messagebox.showerror("Error", "Worng product id.")
                    return
                else:
                    item_id1 = str(item_id)


           #print(item_id)
                c.execute("SELECT item_name FROM products where item_id = '"+item_id+"'")
                item_set = c.fetchone()
                item_name = item_set[0]
           #print(item_name)
                item_qty = str(qty_ey.get())
                if item_qty == "":
                    messagebox.showerror("Error", "Please type in product quantity.")
                    return
                elif int(item_qty) <= 0:
                    messagebox.showerror("Error", "Product quantity cannot be 0 or lesser.")
                    return
                else:
                    item_qty1 = str(item_qty)
           #print(item_qty)
                c.execute("SELECT item_price FROM products where item_id = '" + item_id + "'")
                price_set = c.fetchone()
                item_price = price_set[0]
                total_price = int(item_qty)*int(item_price)
           #print(total_price)
                retailer_id = str(userac_ey.get())
                c.execute("SELECT * FROM users where user_id = '" + retailer_id + "'")
                retailer_set = c.fetchone()
                retailer_name = str(retailer_set[2])
           #print(retailer_name)
                retailer_tel = retailer_set[3]
           #print(retailer_tel)
                retailer_address = retailer_set[4]
           #print(retailer_address)
           # print(order_id, order_date, item_id, item_name, item_qty, total_price, retailer_id, retailer_name, retailer_tel, retailer_address)

                c.execute("SELECT remaining FROM products WHERE item_id = '" + item_id + "'")
                stocklevel = c.fetchone()
                stocklevel1 = stocklevel[0]
                print("item quantity: "+item_qty1)
                print("stocklevel1= " + str(stocklevel1))
                if stocklevel1 <= 0 or int(item_qty1) > stocklevel1:

                    messagebox.showwarning("Sorry", "Product stock out !")
                    return
                else:
                    order_set = (order_id, str(order_date), item_id1, item_name, item_qty1, total_price, retailer_id, retailer_name, retailer_tel, retailer_address)
               # print(order_set)
                    c.execute("INSERT INTO order_table VALUES (?,?,?,?,?,?,?,?,?,?);",order_set)
                    c.execute("SELECT remaining FROM products where item_id = '" + item_id + "'")
                    o_value = c.fetchone()
                    o_value1 = o_value[0]
                    print("old value: " + str(o_value1))
                    new_value = int(o_value1) - int(item_qty)
                    new_value1 = str(new_value)
                    print("new value: " + str(new_value1))
                    status_set = (order_id, "N", "")
                    print(status_set)
                    c.execute("INSERT INTO status VALUES (?,?,?);", status_set)
                    c.execute("UPDATE  products SET remaining = "+new_value1+" WHERE item_id = '" + item_id + "'")
                    conn.commit()
                    messagebox.showinfo("Information", "The order has been received")
            def csv():
                def load():
                    load_path = filedialog.askopenfilename()
                    csv_ey.delete("1.0", END)
                    csv_ey.insert(INSERT, load_path)

                def import1():
                    path = csv_ey.get('1.0', '1.end')
                    csvfile = open(path, 'r')
                    creader = csv1.reader(csvfile)
                    print(creader)
                    for row in creader:
                        print(row)
                        # book_date = str(datetime.date.today())
                        c.execute("INSERT INTO booking VALUES (?,?,?,?,?,?,?,?);", row)
                            # print(order2)
                        conn.commit()
                    messagebox.showinfo("Information", "The order has been received")
                    opencsv.destroy()

               # for t in creader:
               #  c.execute("INSERT INTO order_table VALUES (?,?,?,?,?,?,?,?,?,?);", t)

                opencsv = Toplevel(root)
                opencsv.geometry('480x200')
                opencsv.title('Import CSV')
                opencsv.config(bg='cyan')

                csv_lb = tk.Label(opencsv, text="Location:", height=1, width=8, bg="cyan")
                csv_lb.place(x=20, y=10)
                csv_ey = Text(opencsv, height=1, width=45, bd=5)
                csv_ey.place(x=100, y=10)
                csv_ey.bind("<Key>", lambda e: "break")
                load_bt = Button(opencsv, text="Load", height=1, width=10, command=load)
                load_bt.place(x=300, y=50)

                import_bt = Button(opencsv, text="Import CSV", height=1, width=10, command=import1)
                import_bt.place(x=200, y=50)
                #orderPage
            columns = ('Product ID', 'Name', 'Remaining', 'Price', 'Weight', 'Description')
            tree = ttk.Treeview(Frame, columns=columns, height=20, show="headings")
            tree.heading('#1', text='ID')
            tree.heading('#2', text='Name')
            tree.heading('#3', text='Remaining')
            tree.heading('#4', text='Price')
            tree.heading('#5', text='Weight')
            tree.heading('#6', text='Description')
            tree.column('#6', width=200, anchor=tk.CENTER)
            tree.column('#5', width=60, anchor=tk.CENTER)
            tree.column('#4', width=60, anchor=tk.CENTER)
            tree.column('#3', width=80, anchor=tk.CENTER)
            tree.column('#2', width=120, anchor=tk.CENTER)
            tree.column('#1', width=80, anchor=tk.CENTER)
            tree.place(x=10, y=120)
            showproduct()
            tree.bind("<<TreeviewSelect>>", on_tree_select)

            searchp_lb = tk.Label(Frame, text="Search Item:", height=1, width=15, bg="cyan")
            searchp_lb.place(x=10, y=15)
            searchp_ey = tk.Entry(Frame, width=15, bd=5)
            searchp_ey.place(x=120, y=10)
            searchp_bt = Button(Frame, text="Search", height=1, width=12, command=searchitem)
            searchp_bt.place(x=260, y=10)
            showall_bt = Button(Frame, text="Show all", height=1, width=12, command=showitems)
            showall_bt.place(x=365, y=10)
            import_bt = Button(Frame, text="Import CSV", height=1, width=12, command = csv)
            import_bt.place(x=600, y=10)
            selected_lb = tk.Label(Frame, text="Item ID:", height=1, width=15, bg="cyan")
            selected_lb.place(x=10, y=55)
            selected_ey = tk.Entry(Frame, width=15, bd=5)
            selected_ey.place(x=120, y=50)
            qty_lb = tk.Label(Frame, text="Quantity:", height=1, width=10, bg="cyan")
            qty_lb.place(x=250, y=50)
            user_lb = tk.Label(Frame, text="HI  "+userac2, height=1, width=10, bg="cyan")
            user_lb.place(x=480, y=50)
            qty_ey = tk.Entry(Frame, width=12, bd=5)
            qty_ey.place(x=320, y=50)
            buy_bt = Button(Frame, text="Purchase", height=1, width=12, command=purchasing)
            buy_bt.place(x=600, y=45)
            # stock function
            def clear():
                var.set(1)
                search_ey.delete(0, END)
                search_bt.config(state='normal')
                search_bt1.config(state='disable')

                for i in tree1.get_children():
                    tree1.delete(i)

            def treeview_sort_column(tv, col, reverse):
                l = [(tv.set(k, col), k) for k in tv.get_children('')]
                l.sort(reverse=reverse)
                for index, (val, k) in enumerate(l):
                    tv.move(k, '', index)
                    tv.heading(col, command=lambda: \
                        treeview_sort_column(tv, col, not reverse))

            def search():
                itemname = str(search_ey.get())
                c.execute("SELECT item_id,item_name,remaining FROM products where item_name like'%" + itemname + "%'")
                itemname1 = c.fetchall()
                for i in tree1.get_children():
                    tree1.delete(i)
                for item in itemname1:
                    tree1.insert('', 0, values=(item))

            def search1():
                c.execute("SELECT item_id,item_name,remaining FROM products")
                allitem = c.fetchall()
                for i in tree1.get_children():
                    tree1.delete(i)
                for item in allitem:
                    tree1.insert('', 0, values=(item))

            def sel():
                selection = var.get()
                if selection == 1:
                    search_bt1.config(state='disable')
                    search_ey.config(state='normal')
                    search_bt.config(state='normal')
                else:
                    search_ey.config(state='disable')
                    search_bt.config(state='disable')
                    search_bt1.config(state='normal')
            #stockPage
            columns = ('Item ID', 'Item Name', 'Remaining')
            tree1 = ttk.Treeview(Frame1, columns=columns, height=20, show="headings")
            tree1.heading('#1', text='Item ID')
            tree1.heading('#2', text='Item Name')
            tree1.heading('#3', text='Remaining')
            tree1.column('#3', width=250, anchor=tk.CENTER)
            tree1.column('#2', width=250, anchor=tk.CENTER)
            tree1.column('#1', width=70, anchor=tk.CENTER)
            tree1.place(x=10, y=120)
            for col in columns:
                tree1.heading(col, text=col, command=lambda _col=col: \
                    treeview_sort_column(tree1, _col, False))

            var = IntVar()
            R1 = Radiobutton(Frame1, text="", variable=var, value=1, bg="cyan", command=sel)
            R1.place(x=3, y=10)
            var.set(1)
            R2 = Radiobutton(Frame1, text="", variable=var, value=2, bg="cyan", command=sel)
            R2.place(x=3, y=40)

            search_lb = tk.Label(Frame1, text="Search Item Name:", height=1, width=15, bg="cyan")
            search_lb.place(x=20, y=10)
            search_ey = tk.Entry(Frame1, width=15, bd=5)
            search_ey.place(x=140, y=10)
            search_bt = Button(Frame1, text="Search", height=1, width=12, command=search)
            search_bt.place(x=270, y=10)
            search_bt1 = Button(Frame1, text="Search all item", height=1, width=12, command=search1)
            search_bt1.place(x=30, y=40)
            search_bt1.config(state='disable')
            clear_bt = Button(Frame1, text="Clear", height=1, width=8, command=clear)
            clear_bt.place(x=600, y=520)

            # Order Track

            # Order ID', 'Item Name', 'Qty', 'Total', 'Order Date', 'Receive Address', 'Deliver Status
            def order_record():
                print(userac_ey.get())
                account = userac_ey.get()
                c.execute(
                    "SELECT order_table.Order_ID,order_table.Item_Name,order_table.Item_Qty, order_table.Total_price, order_table.Order_date, order_table.Destination_address, status.Deilvered, status.deil_date FROM order_table inner join status on order_table.Order_ID = status.Order_ID WHERE order_table.retailer_id = '" + account+"' ORDER BY order_table.Order_ID DESC")
                allitem = c.fetchall()
                for i in tree2.get_children():
                    tree2.delete(i)
                for item in allitem:
                    tree2.insert('', 0, values=(item))

            def export_all():
                print(userac_ey.get())
                account = userac_ey.get()
                csvWriter = csv1.writer(open("abc_manu_order_record.csv", "w", newline=''))
                c.execute("SELECT * FROM order_table WHERE order_table.retailer_id = '" + account+"'")
                allitem = c.fetchall()
                fields = ['Order_ID', 'Order_date', 'Item_ID', 'Item_Name', 'Item_Qty', 'Total_price', 'retailer_id',
                          'retailer_name', 'retailer_tel', 'Destination_address']
                csvWriter.writerow(fields)
                for item in allitem:
                    print(item)
                    csvWriter.writerow(item)
                messagebox.showinfo("Information","Order record exported.")

            def export_sel():
                csvWriter = csv1.writer(open("abc_manu_order_record.csv", "w", newline=''))
                selected = tree2.selection()
                print(selected)
                list = []
                for items in selected:
                    print(tree2.item(items)['values'][0])
                    list.append(tree2.item(items)['values'][0])

                where = ""
                for item in list:
                    where += "order_id = '" + item + "' or "
                print("SELECT * FROM order_table WHERE " + where + "1=2")
                c.execute("SELECT * FROM order_table WHERE " + where + "1=2")
                allitems = c.fetchall()
                # fields = ['Order_ID', 'Order_date', 'Item_ID', 'Item_Name', 'Item_Qty', 'Total_price', 'retailer_id',
                #           'retailer_name', 'retailer_tel', 'Destination_address']
                # csvWriter.writerow(fields)
                for item in allitems:
                    print(item)
                    csvWriter.writerow(item)
                messagebox.showinfo("Information", "Order record exported.")

            columns = ('Order ID', 'Item Name', 'Qty', 'Total', 'Order Date', 'Receive Address', 'Deliver Status')
            tree2 = ttk.Treeview(Frame2, columns=columns, height=20, show="headings")
            tree2.heading('#1', text='Order ID')
            tree2.heading('#2', text='Item Name')
            tree2.heading('#3', text='Qty')
            tree2.heading('#4', text='Total')
            tree2.heading('#5', text='Order Date')
            tree2.heading('#6', text='Receive Address')
            tree2.heading('#7', text='Deliver Status')
            tree2.column('#7', width=120, anchor=tk.CENTER)
            tree2.column('#6', width=120, anchor=tk.CENTER)
            tree2.column('#5', width=100, anchor=tk.CENTER)
            tree2.column('#4', width=60, anchor=tk.CENTER)
            tree2.column('#3', width=40, anchor=tk.CENTER)
            tree2.column('#2', width=100, anchor=tk.CENTER)
            tree2.column('#1', width=80, anchor=tk.CENTER)
            tree2.place(x=10, y=100)

            export_all_btn = Button(Frame2, text="Export All Orders", height=1, width=14, command=export_all)
            export_all_btn.place(x=30, y=40)
            export_sel_btn = Button(Frame2, text="Export Selected Orders", height=1, width=20, command=export_sel)
            export_sel_btn.place(x=200, y=40)
            refresh_btn = Button(Frame2, text="Refresh", height=1, width=10, command=order_record)
            refresh_btn.place(x=30, y=70)

            for col in columns:
                tree2.heading(col, text=col, command=lambda _col=col: \
                    treeview_sort_column(tree2, _col, False))

            Frame2.selection_handle(command=order_record())
            Frame1.selection_handle(command=search1())

            # feedback
            def clear_fb():
                feedback_ey.delete("1.0", END)

            def upload_fb():
                account = userac_ey.get()
                if feedback_ey.get("1.0", END) !=  "\n":
                    row = (account, str(datetime.date.today()), feedback_ey.get("1.0", END))
                    c.execute("INSERT INTO feedbacks VALUES (?,?,?);", row)
                    conn.commit()
                    messagebox.showinfo("Info", "Feedback has been sent.")
                    clear_fb()
                else:
                    messagebox.showerror("Error", "Please type in something before submit.")


            announce_lb = tk.Label(Frame3, text="Please give us feedback and help us perform better.", height=1,
                                   width=50, bg="cyan", anchor='w')
            announce_lb.place(x=20, y=10)
            feedback_lb = tk.Label(Frame3, text="Feedback:", height=1, width=15, bg="cyan", anchor='w')
            feedback_lb.place(x=20, y=30)
            feedback_ey = tk.Text(Frame3, width=100, height=30)
            feedback_ey.place(x=20, y=50)
            fb_sub_btn = tk.Button(Frame3, text="Submit", width=10, command=upload_fb)
            fb_sub_btn.place(x=20, y=500)
            fb_reset_btn = tk.Button(Frame3, text="Reset", width=10, command=clear_fb)
            fb_reset_btn.place(x=100, y=500)

        def createac():
            createac1 = Toplevel(root)
            createac1.geometry('500x400')
            createac1.title('Create Account Page')
            createac1.config(bg='cyan')

            def create():
                user_id = acnum_ey.get()
                user_name = acname_ey.get()
                user_pw = password_ey.get()
                user_tel = phone_ey.get()
                user_address = con_address_ey.get()

                if user_id == "":
                    messagebox.showerror("Error", "Please type in account number.")
                elif user_name == "":
                    messagebox.showerror("Error", "Please type in Username")
                elif user_pw == "":
                    messagebox.showerror("Error", "Please type in Password.")
                elif user_tel == "":
                    messagebox.showerror("Error", "Please type in phone number.")
                elif user_address == "":
                    messagebox.showerror("Error", "Please type in address.")
                else:
                    user_info = (user_id, user_pw, user_name, user_tel, user_address)
                    print(user_info)
                    c.execute("INSERT INTO users VALUES (?,?,?,?,?);", user_info)
                    conn.commit()
                    messagebox.showinfo("Information", "Account have been created.")

            def close():
                createac1.withdraw()



            acnum_lb = Label(createac1, text="Account No.:", height=1, width=10, bg="cyan")
            acnum_lb.place(x=10, y=20)
            acnum_lb.config(font=(30))
            acnum_ey = tk.Entry(createac1, width=30, bd=5)
            acnum_ey.place(x=115, y=20)

            acname_lb = Label(createac1, text="Name:", height=1, width=10, bg="cyan")
            acname_lb.place(x=10, y=70)
            acname_lb.config(font=(30))
            acname_ey = tk.Entry(createac1, width=30, bd=5)
            acname_ey.place(x=115, y=70)

            password_lb = Label(createac1, text="Password:", height=1, width=10, bg="cyan")
            password_lb.place(x=10, y=120)
            password_lb.config(font=(30))
            password_ey = tk.Entry(createac1, width=30, bd=5)
            password_ey.place(x=115, y=120)

            phone_lb = Label(createac1, text="Phone Number:", height=1, width=10, bg="cyan")
            phone_lb.place(x=10, y=170)
            phone_lb.config(font=(30))
            phone_ey = tk.Entry(createac1, width=30, bd=5)
            phone_ey.place(x=115, y=170)

            con_address_lb = Label(createac1, text="Contact address:", height=1, width=12, bg="cyan")
            con_address_lb.place(x=5, y=220)
            con_address_lb.config(font=(30))
            con_address_ey = tk.Entry(createac1, width=30, bd=5)
            con_address_ey.place(x=115, y=220)

            exit_bt = Button(createac1, text="Exit", height=1, width=7, command=close)
            exit_bt.place(x=10, y=350)

            sumbit_bt = Button(createac1, text="Submit", height=1, width=7, command=create)
            sumbit_bt.place(x=400, y=350)

        def login():
            userac1 = userac_ey.get()
            userpw1 = userpw_ey.get()

            find_user = "select * from users where user_id ='{0}' and user_pw ='{1}'".format(
                userac1, userpw1)

            c.execute(find_user)

            results = c.fetchall()

            if results:
                global userac2
                userac2 = userac_ey.get()
                account = userac2
                userpage()
                root.withdraw()
                # if variable.get() ==user:
                #     global userac2
                #     userac2 = userac_ey.get()
                #     userpage()
                #
                # elif variable.get() ==staff:
                #     staffpage()

                # for i in results:

                # messagebox.showinfo(title='Welcome', message='How are you? ' + i[2])
                # userpage()
            else:
                messagebox.showerror(message='Error, your password is wrong, try again.')

        self.master.title('Login Page')
        self.pack(fill=BOTH, expand=1)
        self.config(bg='cyan')

        userac_lb = Label(self, text="User Account:", height=1, width=10, bg="cyan")
        userac_lb.place(x=10, y=20)
        userac_lb.config(font=(30))
        userpw_lb = Label(self, text="Password:", height=1, width=10, bg="cyan")
        userpw_lb.place(x=10, y=60)
        userpw_lb.config(font=(30))

        userac_ey = tk.Entry(self, width=20, bd=5)
        userac_ey.place(x=110, y=20)

        userpw_ey = tk.Entry(self, width=20, bd=5)
        userpw_ey.place(x=110, y=60)
        userpw_ey.config(show='*')

        exit_bt = Button(self, text="Exit", height=1, width=7)
        exit_bt.place(x=10, y=200)

        login_bt = Button(self, text="Login", height=1, width=7, command=login)
        login_bt.place(x=160, y=200)

        createac_bt = Button(self, text="Create Account", height=1, width=15, command=createac)
        createac_bt.place(x=230, y=200)


app = Window(root)
root.mainloop()
conn.close()
