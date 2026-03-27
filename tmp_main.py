import time
from tkinter import Tk, messagebox, ttk
from tkinter import *
from tkinter.messagebox import askyesno
import cv2
import pymysql
from PIL import Image, ImageTk
import numpy as np
import os
import main_add_student
import sample
import pyttsx3
from PIL import ImageTk
import ar_master
from sample_data import student
store_data=sample.demo
mm= ar_master.master_flask_code()
class tk_master:
    global uid
    user=''
    def __init__(self):
        self.master='ar_master'
        self.title ='Smoke Detection'
        self.titlec ='SMOKE DETECTION'
        self.backround_color ='#2F4F4F'
        # self.text_color ='#c0c0c0'
        self.text_color ='#FFF'
        self.backround_image='images/background_hd1.jpg'
    def get_title(self):
        return self.title
    def get_titlec(self):
        return self.titlec
    def get_backround_color(self):
        return self.backround_color
    def get_text_color(self):
        return self.text_color
    def get_backround_image(self):
        return self.backround_image
    def user_home(self):
        user_home = Toplevel()
        def view_data():
            date_list=[]
            def SpeakText(command):
                engine = pyttsx3.init()
                engine.say(command)
                engine.runAndWait()
                engine.stop()
            def selectItem(a):
                total = 0
                curItem = tree1.focus()
                data = (tree1.item(curItem))
                data1 = (data['values'])
                file_name = (data1[0])
            TableMargin1 = Frame(user_home, width=300)
            TableMargin1.place(x=50, y=150, width=300, height=255)
            scrollbarx1 = Scrollbar(TableMargin1, orient=HORIZONTAL)
            scrollbary1 = Scrollbar(TableMargin1, orient=VERTICAL)
            tree1 = ttk.Treeview(TableMargin1, columns=("fine"), height=400,
                                selectmode="extended", yscrollcommand=scrollbary1.set, xscrollcommand=scrollbarx1.set)
            scrollbary1.config(command=tree1.yview)
            scrollbary1.pack(side=RIGHT, fill=Y)
            scrollbarx1.config(command=tree1.xview)
            scrollbarx1.pack(side=BOTTOM, fill=X)
            tree1.heading('fine', text="fine")
            # tree1.heading('author', text="author", anchor=W)
            # tree1.heading('publication', text="publication", anchor=W)
            # tree1.heading('count', text="count", anchor=W)
            # tree1.heading('year', text="year", anchor=W)
            # tree1.heading('navigation', text="navigation", anchor=W)
            tree1.bind('<ButtonRelease-1>', selectItem)
            tree1.column('#0', stretch=NO, minwidth=0, width=0)
            # tree1.column('#1', stretch=NO, minwidth=0, width=200)
            # tree1.column('#2', stretch=NO, minwidth=0, width=200)
            # tree1.column('#3', stretch=NO, minwidth=0, width=200)
            # tree1.column('#4', stretch=NO, minwidth=0, width=200)
            # tree1.column('#5', stretch=NO, minwidth=0, width=200)
            tree1.pack()
            try:
                my_conn = []
                for filename in os.listdir('fine'):
                    file_path = os.path.join("fine", filename)
                    # print(file_path,filename)
                    # file1 = open(file_path, 'r')
                    file1 = open(file_path, 'r', encoding='cp856')
                    Lines = file1.readlines()
                    ar1, ar2 = (str(Lines[0].strip()), str(sample.demo.udi).strip())
                    if (ar1 == ar2):
                        dd=filename.split(".")
                        tree1.insert("", 0, values=dd[0])
                # print(my_conn)
                # for hr_addsalary in my_conn:
                #     tree1.insert("", 0, values=hr_addsalary)
            except:
                pass
        user_home.attributes('-topmost', 'true')
        get_data = tk_master()
        w = 880
        h = 600
        ws = user_home.winfo_screenwidth()
        hs = user_home.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        user_home.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        user_home.resizable(False, False)
        canvas1 = Canvas(user_home, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        # canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 30),
        #                     fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 20, text="FINE DETAILS", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        view_data()
        user_home.mainloop()

    def set_window_design(self):
        root = Tk()
        w = 780
        h = 500
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open("images/background_hd1.jpg")
        resized = image.resize((w, h), Image.Resampling.LANCZOS)
        image2 = ImageTk.PhotoImage(resized)
        canvas = Canvas(root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=image2, anchor=NW)
        canvas.create_text(390, 20, text=self.title, font=("Times New Roman", 24), fill=self.text_color)
        def admin_login():
            tt = tk_master()
            tt.admin_login()
        def user_login():
            tt = tk_master()
            tt.user_login()

        b1 = Button(canvas, text="ADMIN", command=admin_login, font=('times', 15, ' bold '),width=20)
        canvas.create_window(400, 150, window=b1)
        b1 = Button(canvas, text="USER", command=user_login, font=('times', 15, ' bold '),width=20)
        canvas.create_window(400, 250, window=b1)

        root.mainloop()
    # def help_desk_login(self):
    #     help_desk_login =Toplevel()
    #     help_desk_login.attributes('-topmost', 'true')
    #     get_data=tk_master()
    #     w = 780
    #     h = 500
    #     ws = help_desk_login.winfo_screenwidth()
    #     hs = help_desk_login.winfo_screenheight()
    #     x = (ws / 2) - (w / 2)
    #     y = (hs / 2) - (h / 2)
    #     help_desk_login.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #     image = Image.open('images/background_hd1.png')
    #     img = image.resize((w, h))
    #     my_img = ImageTk.PhotoImage(img)
    #     help_desk_login.resizable(False, False)
    #     canvas1 = Canvas(help_desk_login, width=200, height=300)
    #     canvas1.create_image(0, 0, image=my_img, anchor=NW)
    #     canvas1.pack(fill="both", expand=True)
    #     canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 30), fill=get_data.get_text_color())
    #     ##
    #     admin_id2 = canvas1.create_text(390, 100, text="HELP DESK LOGIN", font=("Times New Roman", 24), fill=get_data.get_text_color())
    #     admin_id2 = canvas1.create_text(300, 200, text="Username", font=("Times New Roman", 24), fill=get_data.get_text_color())
    #     admin_id2 = canvas1.create_text(300, 300, text="Password", font=("Times New Roman", 24), fill=get_data.get_text_color())
    #     e1 = Entry(canvas1,font=('times', 15, ' bold '))
    #     canvas1.create_window(470, 200, window=e1)
    #     e2 = Entry(canvas1, font=('times', 15, ' bold '),show="*")
    #     canvas1.create_window(470, 300, window=e2)
    #     def exit_program():
    #         a=e1.get()
    #         b=e2.get()
    #         if (a == ""):
    #             messagebox.showinfo(title="Alert", message="Enter Username", parent=help_desk_login)
    #         elif (b == ""):
    #             messagebox.showinfo(title="Alert", message="Enter Password", parent=help_desk_login)
    #         else:
    #             data=mm.select_direct_query("select * from help_desk_details where username='"+str(a)+"' and password='"+str(b)+"'")
    #             if len(data)>0:
    #                 messagebox.showinfo("Result","Login Success", parent=help_desk_login)
    #                 help_desk_login.destroy()
    #                 tt = tk_master()
    #                 tt.help_desk_home()
    #             else:
    #                 messagebox.showinfo("Result","Login Failed", parent=help_desk_login)
    #     b1=Button(canvas1, text="Login", command=exit_program, font=('times', 15, ' bold '))
    #     canvas1.create_window(470, 400, window=b1)
    #     help_desk_login.mainloop()
    def admin_login(self):
        admin_login_root =Toplevel()
        admin_login_root.attributes('-topmost', 'true')
        get_data=tk_master()
        w = 780
        h = 500
        ws = admin_login_root.winfo_screenwidth()
        hs = admin_login_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        admin_login_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        admin_login_root.resizable(False, False)
        canvas1 = Canvas(admin_login_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 30), fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 100, text="ADMIN LOGIN", font=("Times New Roman", 24), fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 200, text="Username", font=("Times New Roman", 24), fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 300, text="Password", font=("Times New Roman", 24), fill=get_data.get_text_color())
        e1 = Entry(canvas1,font=('times', 15, ' bold '))
        canvas1.create_window(470, 200, window=e1)
        e2 = Entry(canvas1, font=('times', 15, ' bold '),show="*")
        canvas1.create_window(470, 300, window=e2)
        def exit_program():
            a=e1.get()
            b=e2.get()
            if (a == ""):
                messagebox.showinfo(title="Alert", message="Enter Username", parent=admin_login_root)
            elif (b == ""):
                messagebox.showinfo(title="Alert", message="Enter Password", parent=admin_login_root)
            elif((a=="admin")and(b=="admin")):
                messagebox.showinfo("Result","Login Success", parent=admin_login_root)
                admin_login_root.destroy()
                tt = tk_master()
                tt.admin_home()
            else:
                messagebox.showinfo("Result","Login Failed", parent=admin_login_root)
        b1=Button(canvas1, text="Login", command=exit_program, font=('times', 15, ' bold '))
        canvas1.create_window(470, 400, window=b1)
        admin_login_root.mainloop()
    def admin_home(self):
        admin_home_root = Toplevel()
        admin_home_root.attributes('-topmost', 'true')
        get_data = tk_master()
        w = 780
        h = 500
        ws = admin_home_root.winfo_screenwidth()
        hs = admin_home_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        admin_home_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        admin_home_root.resizable(False, False)
        canvas1 = Canvas(admin_home_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 24),fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 80, text="ADMIN HOME", font=("Times New Roman", 24),fill=get_data.get_text_color())
        def add_help_desk():
            add_help_desk_root = Toplevel()
            add_help_desk_root.attributes('-topmost', 'true')
            get_data = tk_master()
            w = 780
            h = 500
            ws = add_help_desk_root.winfo_screenwidth()
            hs = add_help_desk_root.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            add_help_desk_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
            image = Image.open('images/background_hd1.jpg')
            img = image.resize((w, h))
            my_img = ImageTk.PhotoImage(img)
            add_help_desk_root.resizable(False, False)
            canvas1 = Canvas(add_help_desk_root, width=200, height=300)
            canvas1.create_image(0, 0, image=my_img, anchor=NW)
            canvas1.pack(fill="both", expand=True)
            # canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 24),
            #                     fill=get_data.get_text_color())
            ##
            admin_id2 = canvas1.create_text(390, 20, text="ADD HELP DESK", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(300, 70, text="NAME", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(300, 120, text="FATHER NAME", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(300, 170, text="CONTACT", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(300, 220, text="EMAIL", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(300, 270, text="ADDRESS", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(300, 320, text="PINCODE", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(300, 370, text="USERNAME", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(300, 420, text="PASSWORD", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())

            e1 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(550, 70, window=e1)
            e2 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(550, 120, window=e2)
            e3 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(550, 170, window=e3)
            e4 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(550, 220, window=e4)
            e5 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(550, 270, window=e5)
            e6= Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(550, 320, window=e6)
            e7 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(550, 370, window=e7)
            e8 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(550, 420, window=e8)

            def exit_program():
                a = e1.get()
                b = e2.get()
                c = e3.get()
                d = e4.get()
                e = e5.get()
                f = e6.get()
                g = e7.get()
                h = e8.get()
                if (a == ""):
                    messagebox.showinfo('Alert', "Enter Name")
                elif (b == ""):
                    messagebox.showinfo('Alert', "Enter Father Name")
                elif (c == ""):
                    messagebox.showinfo('Alert', "Enter Contact")
                elif (d == ""):
                    messagebox.showinfo('Alert', "Enter Email")
                elif (e == ""):
                    messagebox.showinfo('Alert', "Enter Address")
                elif (f == ""):
                    messagebox.showinfo('Alert', "Enter Pincode")

                elif (g == ""):
                    messagebox.showinfo('Alert', "Enter Username")
                elif (h == ""):
                    messagebox.showinfo('Alert', "Enter Password")
                else:
                    maxid=mm.find_max_id("help_desk_details")

                    sql = "insert into help_desk_details values('" + str(maxid) + "','" + a + "','" + b + "','" + c + "','" + d + "','" + e + "','" + f + "','" + g + "','" + h + "','0','0')"
                    mm.insert_query(sql)
                    messagebox.showinfo('Success', "Registered Successfully",parent=add_help_desk_root)
                    add_help_desk_root.destroy()

            b1 = Button(canvas1, text="ADD HELP DESK", command=exit_program, font=('times', 15, ' bold '))
            canvas1.create_window(470, 470, window=b1)
            add_help_desk_root.mainloop()

        def update_product():
            update_product_root = Toplevel()
            update_product_root.attributes('-topmost', 'true')
            get_data = tk_master()
            w = 780
            h = 500
            ws = update_product_root.winfo_screenwidth()
            hs = update_product_root.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            update_product_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
            image = Image.open('images/background_hd1.jpg')
            img = image.resize((w, h))
            my_img = ImageTk.PhotoImage(img)
            update_product_root.resizable(False, False)
            canvas1 = Canvas(update_product_root, width=200, height=300)
            canvas1.create_image(0, 0, image=my_img, anchor=NW)
            canvas1.pack(fill="both", expand=True)
            # canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 24),
            #                     fill=get_data.get_text_color())
            ##
            admin_id2 = canvas1.create_text(390, 20, text="UPDATE PRODUCT", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(300, 70, text="PRODUCT NAME", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(300, 120, text="PRICE", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(300, 170, text="QUANTITY", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(300, 220, text="OFFER", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())

            e1 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(550, 70, window=e1)
            e2 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(550, 120, window=e2)
            e3 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(550, 170, window=e3)
            e4 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(550, 220, window=e4)

            def exit_program():
                a = e1.get()
                b = e2.get()
                c = e3.get()
                d = e4.get()
                if (a == ""):
                    messagebox.showinfo('Alert', "Enter Product Name")
                elif (b == ""):
                    messagebox.showinfo('Alert', "Enter Price")
                elif (c == ""):
                    messagebox.showinfo('Alert', "Enter Quantity")
                else:
                    sql = "update product_details set price='"+str(b)+"',quantity='"+str(c)+"',offer='"+str(d)+"' where product_name='"+str(a)+"'"
                    try:
                        mm.insert_query(sql)
                        messagebox.showinfo('Success', "Updated Successfully",parent=update_product_root)
                        update_product_root.destroy()
                    except:
                        msg = messagebox.showinfo('Failed', "Failed",parent=update_product_root)
                    update_product_root.destroy()

            b1 = Button(canvas1, text="Update", command=exit_program, font=('times', 15, ' bold '))
            canvas1.create_window(470, 270, window=b1)
            update_product_root.mainloop()
        def add_user():
            add_user_root = Toplevel()
            add_user_root.attributes('-topmost', 'true')
            get_data = tk_master()
            w = 780
            h = 500
            ws = add_user_root.winfo_screenwidth()
            hs = add_user_root.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            add_user_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
            image = Image.open('images/background_hd1.jpg')
            img = image.resize((w, h))
            my_img = ImageTk.PhotoImage(img)
            add_user_root.resizable(False, False)
            canvas1 = Canvas(add_user_root, width=200, height=300)
            canvas1.create_image(0, 0, image=my_img, anchor=NW)
            canvas1.pack(fill="both", expand=True)
            # canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 24),
            #                     fill=get_data.get_text_color())
            ##
            admin_id2 = canvas1.create_text(390, 20, text="ADD USER", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(300, 70, text="NAME", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(300, 120, text="FATHER NAME", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(300, 170, text="CONTACT", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(300, 220, text="EMAIL", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(300, 270, text="ADDRESS", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(300, 320, text="PINCODE", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(300, 370, text="USERNAME", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(300, 420, text="PASSWORD", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())

            e1 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(550, 70, window=e1)
            e2 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(550, 120, window=e2)
            e3 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(550, 170, window=e3)
            e4 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(550, 220, window=e4)
            e5 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(550, 270, window=e5)
            e6 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(550, 320, window=e6)
            e7 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(550, 370, window=e7)
            e8 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(550, 420, window=e8)

            def exit_program():
                a = e1.get()
                b = e2.get()
                c = e3.get()
                d = e4.get()
                e = e5.get()
                f = e6.get()
                g = e7.get()
                h = e8.get()
                if (a == ""):
                    messagebox.showinfo('Alert', "Enter Name")
                elif (b == ""):
                    messagebox.showinfo('Alert', "Enter Father Name")
                elif (c == ""):
                    messagebox.showinfo('Alert', "Enter Contact")
                elif (d == ""):
                    messagebox.showinfo('Alert', "Enter Email")
                elif (e == ""):
                    messagebox.showinfo('Alert', "Enter Address")
                elif (f == ""):
                    messagebox.showinfo('Alert', "Enter Pincode")

                elif (g == ""):
                    messagebox.showinfo('Alert', "Enter Username")
                elif (h == ""):
                    messagebox.showinfo('Alert', "Enter Password")
                else:
                    maxid = mm.find_max_id("user_details")
                    uid=maxid+100

                    sql = "insert into user_details values('" + str(maxid) + "','" + a + "','" + b + "','" + c + "','" + d + "','" + e + "','" + f + "','" + g + "','" + h + "','0','"+str(uid)+"')"
                    mm.insert_query(sql)
                    # messagebox.showinfo('Success', "Registered Successfully", parent=add_user_root)
                    messagebox.showinfo('Success', "Registered Successfully \n user ID : " + str(uid), parent=add_user_root)
                    add_user_root.destroy()

            b1 = Button(canvas1, text="ADD USER", command=exit_program, font=('times', 15, ' bold '))
            canvas1.create_window(470, 470, window=b1)
            add_user_root.mainloop()

        def add_product():
            add_product = Toplevel()
            add_product.attributes('-topmost', 'true')
            def del_sc1():
                sc1.destroy()

            def err_screen():
                global sc1
                sc1 = Tk()
                sc1.geometry('200x80')
                sc1.title('Warning!!')
                sc1.configure(background='snow')
                Label(sc1, text='Enrollment & Name required!!!', fg='#f5427e', bg='white',
                      font=('times', 16, ' bold ')).pack()
                Button(sc1, text='OK', command=del_sc1, fg="black", bg="#42bcf5", width=9, height=1,
                       activebackground="Red", font=('times', 15, ' bold ')).place(x=90, y=50)

            def clear():
                txt.delete(first=0, last=22)

            def training():
                a = txt.get()
                if (a == ""):
                    messagebox.showinfo(title="Alert", message="Enter Your Name")
                else:
                    d = 0
                    s1 = student;
                    s1.name = a
                    tt = tk_master()
                    tt.test()
            def testing():
                import test_1

            w = 780
            h = 500
            ws = add_product.winfo_screenwidth()
            hs = add_product.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            add_product.geometry('%dx%d+%d+%d' % (w, h, x, y))
            add_product.title("SMOKE DETECTION")
            message = Label(add_product, text="SMOKE DETECTION & FACE RECOGNITION", fg="#004080", width=45, height=3,
                            font=('times', 20, 'italic bold '))
            message.place(x=12, y=20)

            lbl = Label(add_product, text="USERNAME", width=20, height=2, fg="black", font=('times', 15, ' bold '))
            lbl.place(x=30, y=200)

            txt = Entry(add_product, validate="key", width=20, font=('times', 25, ' bold '))
            txt.place(x=300, y=200)

            compare_dataset = Button(add_product, text="TRAINING", width=15, height=1, fg="#FFF", bg="#004080",
                                     command=training, activebackground="orange", activeforeground="white",
                                     font=('times', 15, ' bold '))
            compare_dataset.place(x=250, y=350)

            resust_dataset = Button(add_product, text="TESTING", width=15, height=1, fg="#FFF", bg="#004080", command=testing,
                                    activebackground="orange", activeforeground="white", font=('times', 15, ' bold '))
            resust_dataset.place(x=450, y=350)
            add_product.mainloop()

        b1 = Button(canvas1, text="Add Student", command=add_product, font=('times', 15, ' bold '))
        canvas1.create_window(400, 150, window=b1)
        def view_user():
            tt = tk_master()
            tt.view_user()
        b1 = Button(canvas1, text="View User", command=view_user, font=('times', 15, ' bold '))
        canvas1.create_window(400, 200, window=b1)
        def logout1():
            tt = tk_master()
            tt.admin_fine()
        b1 = Button(canvas1, text="Fine", command=logout1,  font=('times', 15, ' bold '))
        canvas1.create_window(400, 250, window=b1)

        def logout():
            admin_home_root.destroy()

        b1 = Button(canvas1, text="Logout", command=logout, font=('times', 15, ' bold '))
        canvas1.create_window(400, 300, window=b1)

        admin_home_root.mainloop()
    def test(self):
        import cv2
        import os

        from sample_data import student

        cascPath = "data/haarcascades/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)
        train = True
        # video_capture = cv2.VideoCapture(0)
        video_capture = cv2.VideoCapture(0)
        # video_capture = cv2.VideoCapture('http://192.168.1.12:8080/video')
        name = "train"
        if os.path.exists(name):
            h = 0;
        else:
            os.mkdir(name)

        s1 = student;
        print(s1.name)
        name1 = "train\\" + s1.name
        if os.path.exists(name1):
            j = 0;
        else:
            os.mkdir(name1)
        k = 0
        while True:
            # Capture frame-by-frame
            ret, frame = video_capture.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ######
            if (frame is None):
                print("Can't open image file")
            face_cascade = cv2.CascadeClassifier(cascPath)
            faces = face_cascade.detectMultiScale(frame, 1.1, 3, minSize=(100, 100))
            if (faces is None):
                print('Failed to detect face')

            if (True):
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    # lastimg = cv2.resize(frame, (32, 32))
                # cv2.imshow('img', frame)

            facecnt = len(faces)
            print("Detected faces: %d" % facecnt)
            i = 0
            height, width = frame.shape[:2]

            for (x, y, w, h) in faces:
                r = max(w, h) / 2
                centerx = x + w / 2
                centery = y + h / 2
                nx = int(centerx - r)
                ny = int(centery - r)
                nr = int(r * 2)

                faceimg = frame[ny:ny + nr, nx:nx + nr]
                lastimg = cv2.resize(faceimg, (100, 100))
                i += 1
                k += 1
                if ((k < 20) & (k >= 5)):
                    str = name1 + '\\%d.jpg' % k
                    cv2.imwrite(str, lastimg)

            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()

    def view_user(self):

        view_user = Toplevel()

        def view_data():

            date_list = []
            TableMargin1 = Frame(view_user, width=700)
            TableMargin1.place(x=50, y=150, width=700, height=355)
            scrollbarx1 = Scrollbar(TableMargin1, orient=HORIZONTAL)
            scrollbary1 = Scrollbar(TableMargin1, orient=VERTICAL)
            tree1 = ttk.Treeview(TableMargin1, columns=("name", "contact", "email", "address"), height=400,
                                 selectmode="extended", yscrollcommand=scrollbary1.set, xscrollcommand=scrollbarx1.set)
            scrollbary1.config(command=tree1.yview)
            scrollbary1.pack(side=RIGHT, fill=Y)
            scrollbarx1.config(command=tree1.xview)
            scrollbarx1.pack(side=BOTTOM, fill=X)
            tree1.heading('name', text="name", anchor=W)
            tree1.heading('contact', text="contact", anchor=W)
            tree1.heading('email', text="email", anchor=W)
            tree1.heading('address', text="address", anchor=W)
            tree1.column('#0', stretch=NO, minwidth=0, width=0)
            tree1.column('#1', stretch=NO, minwidth=0, width=200)
            tree1.column('#2', stretch=NO, minwidth=0, width=200)
            tree1.column('#3', stretch=NO, minwidth=0, width=200)
            tree1.column('#4', stretch=NO, minwidth=0, width=200)
            tree1.pack()

            # tree1.bind('<Button-1>', selectItem)


            if 1 == 2:
                messagebox.showinfo('Alert', "Enter User Id", parent=view_user)
            else:
                data = mm.select_direct_query(
                    "select * from user_details")
                # print(data)
                for x in data:
                    tree1.insert("", 0, values=(str(x[1]), str(x[2]), str(x[3]), str(x[4])))
                    date_list.append(str(x[5]))
            # print(date_list)




        view_user.attributes('-topmost', 'true')
        get_data = tk_master()
        w = 880
        h = 600
        ws = view_user.winfo_screenwidth()
        hs = view_user.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        view_user.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        view_user.resizable(False, False)
        canvas1 = Canvas(view_user, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        # canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 30),
        #                     fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 20, text="USER DETAILS", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())


        view_data()
        view_user.mainloop()

    def help_desk_home(self):

        help_desk_home = Toplevel()
        def view_data():

            date_list=[]
            TableMargin1 = Frame(help_desk_home, width=400)
            TableMargin1.place(x=50, y=300, width=400, height=255)
            scrollbarx1 = Scrollbar(TableMargin1, orient=HORIZONTAL)
            scrollbary1 = Scrollbar(TableMargin1, orient=VERTICAL)
            tree1 = ttk.Treeview(TableMargin1, columns=("Product", "Price", "Quantity", "Offer"), height=400,
                                selectmode="extended", yscrollcommand=scrollbary1.set, xscrollcommand=scrollbarx1.set)
            scrollbary1.config(command=tree1.yview)
            scrollbary1.pack(side=RIGHT, fill=Y)
            scrollbarx1.config(command=tree1.xview)
            scrollbarx1.pack(side=BOTTOM, fill=X)
            tree1.heading('Product', text="Product", anchor=W)
            tree1.heading('Price', text="Price", anchor=W)
            tree1.heading('Quantity', text="Quantity", anchor=W)
            tree1.heading('Offer', text="Offer", anchor=W)
            tree1.column('#0', stretch=NO, minwidth=0, width=0)
            tree1.column('#1', stretch=NO, minwidth=0, width=200)
            tree1.column('#2', stretch=NO, minwidth=0, width=200)
            tree1.column('#3', stretch=NO, minwidth=0, width=200)
            tree1.pack()


            # tree1.bind('<Button-1>', selectItem)

            id=e1.get()
            if id=="":
                messagebox.showinfo('Alert', "Enter User Id", parent=help_desk_home)
            else:
                data=mm.select_direct_query("select * from purchase_details where uid='"+str(id)+"' and status='0'")
                # print(data)
                for x in data:
                    tree1.insert("", 0, values=(str(x[1]), str(x[2]), str(x[3]), str(x[4])))
                    date_list.append(str(x[5]))
            # print(date_list)
            res = []
            [res.append(x) for x in date_list if x not in res]

            TableMargin = Frame(help_desk_home, width=400)
            TableMargin.place(x=50, y=150, width=400, height=100)
            scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
            scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
            tree = ttk.Treeview(TableMargin, columns=("name", "contact", "address", "pincode"), height=400,
                                selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            tree.heading('name', text="name", anchor=W)
            tree.heading('contact', text="contact", anchor=W)
            tree.heading('address', text="address", anchor=W)
            tree.heading('pincode', text="pincode", anchor=W)
            tree.column('#0', stretch=NO, minwidth=0, width=0)
            tree.column('#1', stretch=NO, minwidth=0, width=200)
            tree.column('#2', stretch=NO, minwidth=0, width=200)
            tree.column('#3', stretch=NO, minwidth=0, width=200)
            tree.pack()
            id = e1.get()
            if id == "":
                messagebox.showinfo('Alert', "Enter User Id", parent=help_desk_home)
            else:
                data = mm.select_direct_query(
                    "select id,name,contact,address,pincode from user_details where report='" + str(id) + "'")
                # print(data)
                for x in data:
                    tree.insert("", 0, values=(str(x[1]), str(x[2]), str(x[3]), str(x[4])))
            def selectItem(a):

                curItem = tree.focus()

                dd=tree.item(curItem).get(curItem)
                print(dd)
            TableMargin = Frame(help_desk_home, width=200)
            TableMargin.place(x=550, y=150, width=200, height=300)
            scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
            scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
            tree = ttk.Treeview(TableMargin, columns=("date"), height=300,
                                selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            tree.heading('date', text="date", anchor=W)

            tree.column('#0', stretch=NO, minwidth=0, width=0)
            tree.bind('<ButtonRelease-1>', selectItem)
            tree.pack()
            for x in res:
                tree.insert("", 0, values=(str(x)))




        help_desk_home.attributes('-topmost', 'true')
        get_data = tk_master()
        w = 880
        h = 600
        ws = help_desk_home.winfo_screenwidth()
        hs = help_desk_home.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        help_desk_home.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        help_desk_home.resizable(False, False)
        canvas1 = Canvas(help_desk_home, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        # canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 30),
        #                     fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 20, text="DELIVERY DETAILS", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(100, 100, text="User Id", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        e1 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(280, 100, window=e1)

        b1 = Button(canvas1, text="Search", command=view_data, font=('times', 15, ' bold '))
        canvas1.create_window(490, 100, window=b1)
        help_desk_home.mainloop()
    def user_registration(self):
        user_registration_root = Toplevel()
        user_registration_root.attributes('-topmost', 'true')
        get_data = tk_master()
        w = 780
        h = 500
        ws = user_registration_root.winfo_screenwidth()
        hs = user_registration_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        user_registration_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        user_registration_root.resizable(False, False)
        canvas1 = Canvas(user_registration_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        # canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 24),
        #                     fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 20, text="USER REGISTRATION", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 70, text="Name", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 120, text="Contact", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 170, text="Email", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 220, text="Address", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 270, text="Username", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 320, text="Password", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())

        e1 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 70, window=e1)
        e2 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 120, window=e2)
        e3 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 170, window=e3)
        e4 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 220, window=e4)
        e5 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 270, window=e5)
        e6 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 320, window=e6)

        def exit_program():
            name = e1.get()
            contact = e2.get()
            email = e3.get()
            address = e4.get()
            username = e5.get()
            password = e6.get()
            if (name == ""):
                messagebox.showinfo(title="Alert", message="Enter Name", parent=user_registration_root)
            elif (contact == ""):
                messagebox.showinfo(title="Alert", message="Enter Contact", parent=user_registration_root)
            elif (email == ""):
                messagebox.showinfo(title="Alert", message="Enter Email", parent=user_registration_root)
            elif (address == ""):
                messagebox.showinfo(title="Alert", message="Enter Address", parent=user_registration_root)
            elif (username == ""):
                messagebox.showinfo(title="Alert", message="Enter Username", parent=user_registration_root)
            elif (password == ""):
                messagebox.showinfo(title="Alert", message="Enter Password", parent=user_registration_root)
            else:
                maxin = mm.find_max_id("user_details")
                qry = ("insert into user_details values('" + str(maxin) + "','" + str(name) + "','" + str(
                    contact) + "','" + str(email) + "','" + str(address) + "','" + str(username) + "','" + str(
                    password) + "','0','0')")
                result = mm.insert_query(qry)
                messagebox.showinfo(title="Alert", message="Registration Success", parent=user_registration_root)
                user_registration_root.destroy()
        b1 = Button(canvas1, text="Register", command=exit_program, font=('times', 15, ' bold '))
        canvas1.create_window(470, 400, window=b1)
        user_registration_root.mainloop()
    def user_login(self):
        user_login_root =Toplevel()
        user_login_root.attributes('-topmost', 'true')
        get_data=tk_master()
        w = 780
        h = 500
        ws = user_login_root.winfo_screenwidth()
        hs = user_login_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        user_login_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        user_login_root.resizable(False, False)
        canvas1 = Canvas(user_login_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 24), fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 100, text="USER LOGIN", font=("Times New Roman", 24), fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 200, text="Username", font=("Times New Roman", 24), fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 300, text="Password", font=("Times New Roman", 24), fill=get_data.get_text_color())
        def clickHandler1(event):
            tt = tk_master()
            tt.user_registration()
        new_register_id = canvas1.create_text(440, 450, text="New Registration Here...", font=("Times New Roman", 24),fill=get_data.get_text_color())
        canvas1.tag_bind(new_register_id, "<1>", clickHandler1)
        e1 = Entry(canvas1,font=('times', 15, ' bold '))
        canvas1.create_window(470, 200, window=e1)
        e2 = Entry(canvas1, font=('times', 15, ' bold '),show="*")
        canvas1.create_window(470, 300, window=e2)
        def exit_program():
            a=e1.get()
            b=e2.get()
            if (a == ""):
                messagebox.showinfo(title="Alert", message="Enter Username", parent=user_login_root)
            elif (b == ""):
                messagebox.showinfo(title="Alert", message="Enter Password", parent=user_login_root)
            else:
                sample.demo.udi=a
                qry = "SELECT * from user_details where username='" +str(a)+ "' and password='"+ str(b)+ "'"
                result = mm.select_login(qry)
                if result == "no":
                    messagebox.showinfo("Result","Login Failed", parent=user_login_root)
                else:
                    tt = tk_master()
                    tt.care_taker=str(a)
                    messagebox.showinfo("Result","Login Success", parent=user_login_root)
                    user_login_root.destroy()

                    tt.user_home()
        b1=Button(canvas1, text="Login", command=exit_program, font=('times', 15, ' bold '))
        canvas1.create_window(470, 400, window=b1)
        user_login_root.mainloop()



    def admin_fine(self):

        admin_fine = Toplevel()
        def view_data():

            date_list=[]
            def SpeakText(command):
                engine = pyttsx3.init()
                engine.say(command)
                engine.runAndWait()
                engine.stop()
            def selectItem(a):
                total = 0
                curItem = tree1.focus()
                data = (tree1.item(curItem))
                data1 = (data['values'])
                file_name = (data1[0])


            TableMargin1 = Frame(admin_fine, width=300)
            TableMargin1.place(x=50, y=150, width=300, height=255)
            scrollbarx1 = Scrollbar(TableMargin1, orient=HORIZONTAL)
            scrollbary1 = Scrollbar(TableMargin1, orient=VERTICAL)
            tree1 = ttk.Treeview(TableMargin1, columns=("fine","user"), height=400,
                                selectmode="extended", yscrollcommand=scrollbary1.set, xscrollcommand=scrollbarx1.set)
            scrollbary1.config(command=tree1.yview)
            scrollbary1.pack(side=RIGHT, fill=Y)
            scrollbarx1.config(command=tree1.xview)
            scrollbarx1.pack(side=BOTTOM, fill=X)
            tree1.heading('fine', text="fine")
            tree1.heading('user', text="user")
            # tree1.heading('author', text="author", anchor=W)
            # tree1.heading('publication', text="publication", anchor=W)
            # tree1.heading('count', text="count", anchor=W)
            # tree1.heading('year', text="year", anchor=W)
            # tree1.heading('navigation', text="navigation", anchor=W)
            tree1.bind('<ButtonRelease-1>', selectItem)
            tree1.column('#0', stretch=NO, minwidth=0, width=0)
            tree1.column('#1', stretch=NO, minwidth=0, width=200)
            # tree1.column('#2', stretch=NO, minwidth=0, width=200)
            # tree1.column('#3', stretch=NO, minwidth=0, width=200)
            # tree1.column('#4', stretch=NO, minwidth=0, width=200)
            # tree1.column('#5', stretch=NO, minwidth=0, width=200)
            tree1.pack()
            try:
                my_conn = []
                for filename in os.listdir('fine'):
                    file_path = os.path.join("fine", filename)
                    # print(file_path,filename)
                    # file1 = open(file_path, 'r')

                    file1 = open(file_path, 'r', encoding='cp856')
                    Lines = file1.readlines()
                    ar1, ar2 = (str(Lines[0].strip()), str(sample.demo.udi).strip())
                    if (ar1 == ar1):
                        dd=filename.split(".")
                        tree1.insert("", 0, values=(dd[0],ar1))

            except:
                pass



        admin_fine.attributes('-topmost', 'true')
        get_data = tk_master()
        w = 880
        h = 600
        ws = admin_fine.winfo_screenwidth()
        hs = admin_fine.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        admin_fine.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        admin_fine.resizable(False, False)
        canvas1 = Canvas(admin_fine, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        # canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 30),
        #                     fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 20, text="FINE DETAILS", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())


        view_data()
        admin_fine.mainloop()


ar=tk_master()
# root=ar.help_desk_home()
root=ar.set_window_design()