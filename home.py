from tkinter import Tk, messagebox, ttk
from tkinter import *
from PIL import Image, ImageTk
from time import strftime
import numpy as np
import imagehash
from PIL import Image
import cv2
import sys
import os
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib
from datetime import datetime
from sample_data import student
import smtplib
import ar_master
mm = ar_master.master_flask_code()
class smoke_detection:
    name=""
    head=""
    def __init__(self):
        self.master = 'ar_master'
        self.title = 'Smoke Detection'
        self.titlec = 'SMOKE DETECTION'
        self.backround_color = '#2F4F4F'
        # self.text_color ='#c0c0c0'
        self.text_color = '#FFF'
        self.backround_image = 'images/background_hd1.jpg'
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
        canvas.create_text(390, 50, text=self.titlec, font=("Times New Roman", 24), fill=self.text_color)
        def admin_login():
            tt = smoke_detection()
            tt.head_login()
        def user_login():
            tt = smoke_detection()
            tt.user_login()
        def camera():
            tt = smoke_detection()
            tt.camera_test()

        b1 = Button(canvas, text="HEAD", command=admin_login, font=('times', 15, ' bold '),width=20)
        canvas.create_window(400, 150, window=b1)
        b1 = Button(canvas, text="USER", command=user_login, font=('times', 15, ' bold '),width=20)
        canvas.create_window(400, 250, window=b1)
        b1 = Button(canvas, text="CAMERA", command=camera, font=('times', 15, ' bold '), width=20)
        canvas.create_window(400, 350, window=b1)
        root.mainloop()
    def head_login(self):
        head_login_root =Toplevel()
        head_login_root.attributes('-topmost', 'true')
        get_data=smoke_detection()
        w = 780
        h = 500
        ws = head_login_root.winfo_screenwidth()
        hs = head_login_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        head_login_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        head_login_root.resizable(False, False)
        canvas1 = Canvas(head_login_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        # canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 30), fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 100, text="HEAD LOGIN", font=("Times New Roman", 24), fill=get_data.get_text_color())
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
                messagebox.showinfo(title="Alert", message="Enter Username", parent=head_login_root)
            elif (b == ""):
                messagebox.showinfo(title="Alert", message="Enter Password", parent=head_login_root)
            else:
                data = mm.select_direct_query("select * from head_details where name='" + str(a) + "' and password='" + str(b) + "'")
                if len(data) > 0:
                    smoke_detection.head=a
                    # print(smoke_detection.head)
                    messagebox.showinfo("Result", "Login Success", parent=head_login_root)
                    head_login_root.destroy()
                    tt = smoke_detection()
                    tt.head_home()
                else:
                    messagebox.showinfo("Result", "Login Failed", parent=head_login_root)
        b1=Button(canvas1, text="Login", command=exit_program, font=('times', 15, ' bold '))
        canvas1.create_window(470, 400, window=b1)
        def clickHandler1(event):
            tt = smoke_detection()
            tt.head_registration()
        new_register_id = canvas1.create_text(440, 450, text="New Registration Here...", font=("Times New Roman", 24),fill=get_data.get_text_color())
        canvas1.tag_bind(new_register_id, "<1>", clickHandler1)
        head_login_root.mainloop()
    def head_registration(self):
        head_registration_root = Toplevel()
        head_registration_root.attributes('-topmost', 'true')
        get_data = smoke_detection()
        w = 780
        h = 500
        ws = head_registration_root.winfo_screenwidth()
        hs = head_registration_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        head_registration_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        head_registration_root.resizable(False, False)
        canvas1 = Canvas(head_registration_root, width=200, height=300)
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
        admin_id2 = canvas1.create_text(300, 270, text="Position", font=("Times New Roman", 24),
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
            import re
            def validate_contact(contact):
                pattern = r"^\+91\d{10}$|^\d{10}$|^[0-9]{2}-\d{10}$|^[0-9]{2}\s\d{10}$"
                if re.match(pattern, contact):
                    return True
                else:
                    return False
            def validate_email(email):
                pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
                if re.match(pattern, email):
                    return True
                else:
                    return False
            def is_strong_password(password):
                pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()\-+]).{8,}$"
                if re.match(pattern, password):
                    return True
                else:
                    return False
            name = e1.get()
            contact = e2.get()
            email = e3.get()
            address = e4.get()
            username = e5.get()
            password = e6.get()
            contact_valid=validate_contact(contact)
            validate_email=validate_email(email)
            validate_password=is_strong_password(password)
            if (name == ""):
                messagebox.showinfo(title="Alert", message="Enter Name", parent=head_registration_root)
            elif (contact == ""):
                messagebox.showinfo(title="Alert", message="Enter Contact", parent=head_registration_root)
            elif (contact_valid == False):
                messagebox.showinfo(title="Alert", message="Enter Valid Contact", parent=head_registration_root)
            elif (email == ""):
                messagebox.showinfo(title="Alert", message="Enter Email", parent=head_registration_root)
            elif (validate_email ==False):
                messagebox.showinfo(title="Alert", message="Enter Valid Email", parent=head_registration_root)
            elif (address == ""):
                messagebox.showinfo(title="Alert", message="Enter Address", parent=head_registration_root)
            elif (username == ""):
                messagebox.showinfo(title="Alert", message="Enter Position", parent=head_registration_root)
            elif (password == ""):
                messagebox.showinfo(title="Alert", message="Enter Password", parent=head_registration_root)
            elif(validate_password==False):
                messagebox.showinfo(title="Alert", message="Enter Valid Password\nChecks if a password meets the following criteria:\n- At least 8 characters long\n- Contains at least one lowercase letter\n- Contains at least one uppercase letter\n- Contains at least one digit\n- Contains at least one special character (!@#$%^&*()-+)", parent=head_registration_root)
            else:
                maxin = mm.find_max_id("head_details")
                qry = ("insert into head_details values('" + str(maxin) + "','" + str(name) + "','" + str(
                    contact) + "','" + str(email) + "','" + str(address) + "','" + str(username) + "','" + str(
                    password) + "','0','0')")
                result = mm.insert_query(qry)
                messagebox.showinfo(title="Alert", message="Registration Success", parent=head_registration_root)
                head_registration_root.destroy()
        b1 = Button(canvas1, text="Register", command=exit_program, font=('times', 15, ' bold '))
        canvas1.create_window(470, 400, window=b1)
        head_registration_root.mainloop()
    def add_user(self):
        head_add_user_root = Toplevel()
        head_add_user_root.attributes('-topmost', 'true')
        get_data = smoke_detection()
        w = 780
        h = 500
        ws = head_add_user_root.winfo_screenwidth()
        hs = head_add_user_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        head_add_user_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        head_add_user_root.resizable(False, False)
        canvas1 = Canvas(head_add_user_root, width=200, height=300)
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
        admin_id2 = canvas1.create_text(300, 370, text="HEAD NAME", font=("Times New Roman", 24),
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
        import tkinter as tk
        e7 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(550, 370, window=e7)
        # print(smoke_detection.head)
        e7.insert(0, smoke_detection.head)
        e7.config(state=tk.DISABLED)

        e8 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(550, 420, window=e8)

        def exit_program():
            import re
            def validate_contact(contact):
                pattern = r"^\+91\d{10}$|^\d{10}$|^[0-9]{2}-\d{10}$|^[0-9]{2}\s\d{10}$"
                if re.match(pattern, contact):
                    return True
                else:
                    return False

            def validate_email(email):
                pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
                if re.match(pattern, email):
                    return True
                else:
                    return False

            def is_strong_password(password):
                pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()\-+]).{8,}$"
                if re.match(pattern, password):
                    return True
                else:
                    return False

            a = e1.get()
            b = e2.get()
            c = e3.get()
            d = e4.get()
            e = e5.get()
            f = e6.get()
            g = e7.get()
            h = e8.get()
            contact_valid = validate_contact(c)
            validate_email = validate_email(d)
            validate_password = is_strong_password(h)
            if (a == ""):
                messagebox.showinfo('Alert', "Enter Name", parent=head_add_user_root)
            elif (b == ""):
                messagebox.showinfo('Alert', "Enter Father Name", parent=head_add_user_root)
            elif (c == ""):
                messagebox.showinfo('Alert', "Enter Contact", parent=head_add_user_root)
            elif (d == ""):
                messagebox.showinfo('Alert', "Enter Email", parent=head_add_user_root)
            elif (e == ""):
                messagebox.showinfo('Alert', "Enter Address", parent=head_add_user_root)
            elif (f == ""):
                messagebox.showinfo('Alert', "Enter Pincode", parent=head_add_user_root)
            elif (g == ""):
                messagebox.showinfo('Alert', "Invalid Head Name", parent=head_add_user_root)
            elif (h == ""):
                messagebox.showinfo('Alert', "Enter Password", parent=head_add_user_root)
            elif (contact_valid == False):
                messagebox.showinfo(title="Alert", message="Enter Valid Contact", parent=head_add_user_root)

            elif (validate_email == False):
                messagebox.showinfo(title="Alert", message="Enter Valid Email", parent=head_add_user_root)

            elif (validate_password == False):
                messagebox.showinfo(title="Alert",
                                    message="Enter Valid Password\nChecks if a password meets the following criteria:\n- At least 8 characters long\n- Contains at least one lowercase letter\n- Contains at least one uppercase letter\n- Contains at least one digit\n- Contains at least one special character (!@#$%^&*()-+)",
                                    parent=head_add_user_root)
            else:
                maxid = mm.find_max_id("user_details")
                sql = "insert into user_details values('" + str(maxid) + "','" + str(a) + "','" + str(b) + "','" + str(
                    c) + "','" + str(d) + "','" + str(e) + "','" + str(f) + "','" + str(g) + "','" + str(
                    h) + "','0','0')"
                mm.insert_query(sql)
                messagebox.showinfo('Success', "Registered Successfully", parent=head_add_user_root)
                head_add_user_root.destroy()
                import cv2
                import os
                from sample_data import student
                cascPath = "data/haarcascades/haarcascade_frontalface_default.xml"
                face_cascade = cv2.CascadeClassifier(cascPath)
                video_capture = cv2.VideoCapture(0)
                name = "train"
                if os.path.exists(name):
                    h = 0;
                else:
                    os.mkdir(name)
                name1 = "train\\" + a
                if os.path.exists(name1):
                    j = 0;
                else:
                    os.mkdir(name1)
                k = 0
                while True:
                    ret, frame = video_capture.read()
                    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    if (frame is None):
                        print("Can't open image file")
                    faces = face_cascade.detectMultiScale(frame, 1.1, 3, minSize=(100, 100))
                    if (faces is None):
                        print('Failed to detect face')
                    if (True):
                        for (x, y, w, h) in faces:
                            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    facecnt = len(faces)
                    print("Detected faces: %d" % facecnt)
                    i = 0

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
                            str1 = name1 + '\\%d.jpg' % k
                            cv2.imwrite(str1, lastimg)
                    if k >= 50:
                        break
                    cv2.imshow('Video', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                video_capture.release()
                cv2.destroyAllWindows()
        b1 = Button(canvas1, text="ADD USER", command=exit_program, font=('times', 15, ' bold '))
        canvas1.create_window(470, 470, window=b1)
        head_add_user_root.mainloop()
    def view_user(self):
        view_user = Toplevel()
        def view_data():
            date_list = []
            TableMargin1 = Frame(view_user, width=700)
            TableMargin1.place(x=75, y=150, width=700, height=355)
            scrollbarx1 = Scrollbar(TableMargin1, orient=HORIZONTAL)
            scrollbary1 = Scrollbar(TableMargin1, orient=VERTICAL)
            tree1 = ttk.Treeview(TableMargin1, columns=("name", "contact", "email", "address"), height=400,selectmode="extended", yscrollcommand=scrollbary1.set, xscrollcommand=scrollbarx1.set)
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
            if 1 == 2:
                messagebox.showinfo('Alert', "Enter User Id", parent=view_user)
            else:
                data = mm.select_direct_query("select * from user_details where head_name='"+str(smoke_detection.head)+"'")
                for x in data:
                    tree1.insert("", 0, values=(str(x[1]), str(x[2]), str(x[3]), str(x[4])))
                    date_list.append(str(x[5]))
        view_user.attributes('-topmost', 'true')
        get_data = smoke_detection()
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
        canvas1 = Canvas(view_user, width=230, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        admin_id2 = canvas1.create_text(450, 50, text="USER DETAILS", font=("Times New Roman", 24),fill=get_data.get_text_color())
        view_data()
        view_user.mainloop()
    def view_head_fine_details(self):
        def view_data():
            date_list=[]
            TableMargin1 = Frame(view_head_fine, width=650)
            TableMargin1.place(x=100, y=150, width=650, height=255)
            scrollbarx1 = Scrollbar(TableMargin1, orient=HORIZONTAL)
            scrollbary1 = Scrollbar(TableMargin1, orient=VERTICAL)
            tree1 = ttk.Treeview(TableMargin1, columns=("User","Date","Time"), height=400,
                                selectmode="extended", yscrollcommand=scrollbary1.set, xscrollcommand=scrollbarx1.set)
            scrollbary1.config(command=tree1.yview)
            scrollbary1.pack(side=RIGHT, fill=Y)
            scrollbarx1.config(command=tree1.xview)
            scrollbarx1.pack(side=BOTTOM, fill=X)
            tree1.heading('User', text="User", anchor=W)
            tree1.heading('Date', text="Date", anchor=W)
            tree1.heading('Time', text="Time", anchor=W)

            tree1.column('#0', stretch=NO, minwidth=0, width=0)
            tree1.column('#1', stretch=NO, minwidth=0, width=200)
            tree1.column('#2', stretch=NO, minwidth=0, width=200)
            tree1.pack()
            try:
                my_conn = []
                path=os.path.join("fine",smoke_detection.head)
                for filename in os.listdir(path):
                    file_path = os.path.join(path, filename)
                    file_path=os.path.splitext(file_path)[0]
                    kk=os.path.basename(file_path)
                    items=kk.split("_")
                    items1=kk.split("__")
                    tree1.insert("", 0, values=(items[0],items[1]+"_"+items[2]+"_"+items[3],items1[1]))
            except:
                pass
        view_head_fine = Toplevel()
        view_head_fine.attributes('-topmost', 'true')
        get_data = smoke_detection()
        w = 880
        h = 600
        ws = view_head_fine.winfo_screenwidth()
        hs = view_head_fine.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        view_head_fine.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        view_head_fine.resizable(False, False)
        canvas1 = Canvas(view_head_fine, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        admin_id2 = canvas1.create_text(390, 20, text="SMOKE DETAILS", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        view_data()
        view_head_fine.mainloop()

    def head_home(self):
        head_home_root = Toplevel()
        # head_home_root.attributes('-topmost', 'true')
        get_data = smoke_detection()
        w = 780
        h = 500
        ws = head_home_root.winfo_screenwidth()
        hs = head_home_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        head_home_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        head_home_root.resizable(False, False)
        canvas1 = Canvas(head_home_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        admin_id2 = canvas1.create_text(390, 80, text="HEAD HOME", font=("Times New Roman", 24),fill=get_data.get_text_color())
        def head_add_user():
            dd=smoke_detection()
            dd.add_user()
        b1 = Button(canvas1, text="Add User", command=head_add_user, font=('times', 15, ' bold '),width=30)
        canvas1.create_window(400, 150, window=b1)
        def head_view_user():
            dd=smoke_detection()
            dd.view_user()
        b1 = Button(canvas1, text="View User", command=head_view_user, font=('times', 15, ' bold '),width=30)
        canvas1.create_window(400, 200, window=b1)
        def head_fine_details():
            dd = smoke_detection()
            dd.view_head_fine_details()
        b1 = Button(canvas1, text="Smoke Details", command=head_fine_details, font=('times', 15, ' bold '),width=30)
        canvas1.create_window(400, 250, window=b1)
        def logout():
            head_home_root.destroy()
        b1 = Button(canvas1, text="Logout", command=logout, font=('times', 15, ' bold '),width=30)
        canvas1.create_window(400, 300, window=b1)
        head_home_root.mainloop()
    def camera_test(self):
        user_details=mm.select_direct_query("select * from user_details")
        head_details=mm.select_direct_query("select user_details.name,head_details.email from user_details,head_details where user_details.head_name=head_details.name")

        user_mail={}
        head_mail={}
        for xx in user_details:
            user_mail[xx[1]]=xx[4]

        for xx in head_details:
            head_mail[xx[0]]=xx[1]
        # print(head_mail)
        # print(user_mail)
        data=mm.select_direct_query("select name,head_name from user_details")
        # print(data)
        net = cv2.dnn.readNet('nm.onnx')
        def format_yolov5(frame):
            row, col, _ = frame.shape
            _max = max(col, row)
            result = np.zeros((_max, _max, 3), np.uint8)
            result[0:row, 0:col] = frame
            return result
        def image_matching(a, b):
            i1 = Image.open(a)
            i2 = Image.open(b)
            assert i1.mode == i2.mode, "Different kinds of images."
            i2 = i2.resize(i1.size)
            pairs = zip(i1.getdata(), i2.getdata())
            if len(i1.getbands()) == 1:
                dif = sum(abs(p1 - p2) for p1, p2 in pairs)
            else:
                dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))
            ncomponents = i1.size[0] * i1.size[1] * 3
            xx = (dif / 255.0 * 100) / ncomponents
            return xx
        def match_templates(in_image):
            name = []
            values = []
            entries = os.listdir('train/')
            folder_lenght = len(entries)
            i = 0
            for x in entries:
                val = 100
                directory = x
                name.append(x)
                x1 = "train/" + x
                arr = os.listdir(x1)
                for x2 in arr:
                    path = x1 + "/" + str(x2)
                    find = image_matching(path, in_image)
                    hash0 = imagehash.average_hash(Image.open(path))
                    hash1 = imagehash.average_hash(Image.open(in_image))
                    cc1 = hash0 - hash1
                    find = cc1
                    if (find < val):
                        val = find
                values.append(val)
            values_lenght = len(values)
            pos = 0
            pos_val = 100
            for x in range(0, values_lenght):
                if values[x] < pos_val:
                    pos = x
                    pos_val = values[x]
                    print("Best match value:", pos_val)

                    if (pos_val < 61):
                        return name[pos]
                    else:
                        return "unknown"
        cascPath = "data/haarcascades/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)
        train = True
        video_capture = cv2.VideoCapture(0)
        name = "testing"
        if os.path.exists(name):
            h = 0;
        else:
            os.mkdir(name)
        e_mail = 0
        arn=0
        while True:
            ret, frame = video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if (frame is None):
                print("Can't open image file")
            face_cascade = cv2.CascadeClassifier(cascPath)
            faces = face_cascade.detectMultiScale(frame, 1.1, 3, minSize=(100, 100))
            if (faces is None):
                print('Failed to detect face')
            if (True):
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            facecnt = len(faces)
            if facecnt < 1:
                img = frame
                height, width = frame.shape[:2]
                cv2.rectangle(frame, (0, 0), (width, height), (0, 0, 0), 3)
            else:
                input_image = format_yolov5(frame)  # making the image square
                blob = cv2.dnn.blobFromImage(input_image, 1 / 255.0, (640, 640), swapRB=True)
                net.setInput(blob)
                predictions = net.forward()
                class_ids = []
                confidences = []
                boxes = []
                output_data = predictions[0]
                image_width, image_height, _ = input_image.shape
                x_factor = image_width / 640
                y_factor = image_height / 640
                for r in range(25200):
                    row = output_data[r]
                    confidence = row[4]
                    # print("confidence",confidence)
                    if confidence >= 0.18:
                        classes_scores = row[5:]
                        _, _, _, max_indx = cv2.minMaxLoc(classes_scores)
                        class_id = max_indx[1]
                        if (classes_scores[class_id] > .18):
                            confidences.append(confidence)
                            class_ids.append(class_id)
                            x, y, w, h = row[0].item(), row[1].item(), row[2].item(), row[3].item()
                            left = int((x - 0.5 * w) * x_factor)
                            top = int((y - 0.5 * h) * y_factor)
                            width = int(w * x_factor)
                            height = int(h * y_factor)
                            box = np.array([left, top, width, height])
                            boxes.append(box)
                class_list = ['smoking']
                indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.18, 0.18)
                result_class_ids = []
                result_confidences = []
                result_boxes = []
                for i in indexes:
                    result_confidences.append(confidences[i])
                    result_class_ids.append(class_ids[i])
                    result_boxes.append(boxes[i])
                for i in range(len(result_class_ids)):

                    class_id = result_class_ids[i]
                    # confi= str(result_confidences[i]+0.4)

                    ddd = int(100 * result_confidences[i].round(2) + 40)
                    print("ddd",ddd)

                    if int(ddd) >= 100:
                        box = result_boxes[i]
                        confi = str(100 * result_confidences[i].round(2) + 40) + "%"
                        cv2.rectangle(frame, box, (0, 255, 255), 2)
                        cv2.rectangle(frame, (box[0], box[1] - 20), (box[0] + box[2], box[1]), (0, 255, 255), -1)
                        cv2.putText(frame, class_list[class_id] + " " + confi, (box[0], box[1] - 10),
                                    cv2.FONT_HERSHEY_SIMPLEX, .5,
                                    (0, 0, 0))
                        for (x, y, w, h) in faces:
                            r = max(w, h) / 2
                            centerx = x + w / 2
                            centery = y + h / 2
                            nx = int(centerx - r)
                            ny = int(centery - r)
                            nr = int(r * 2)
                            faceimg = frame[ny:ny + nr, nx:nx + nr]
                            font = cv2.FONT_HERSHEY_SIMPLEX
                            namez="testing"
                            str1 = namez + '\\tt.jpg'
                            lastimg = cv2.resize(faceimg, (100, 100))
                            cv2.imwrite(str1, lastimg)
                            ar = match_templates(str1)
                            print(ar)
                            if ar == "unknown":
                                e_mail = 0
                            else:
                                e_mail = e_mail + 1
                            # print("email : ",e_mail)

                            namez = "frame"
                            str1 = 'frame/%d.jpg' % arn
                            lastimg = cv2.resize(frame, (250,250))
                            cv2.imwrite(str1, lastimg)
                            now = datetime.now()
                            dt_string = now.strftime("%Y_%m_%d")
                            current_time_str = now.strftime("%H_%M")

                            if e_mail >= 1:
                                msg = str(ar) + "- Smoke detected."+str(dt_string)+"  -  "+str(current_time_str)
                                cc = 'frame/%d.jpg' % arn
                                arn+=1
                                email=user_mail[ar]
                                mm.send_email_without_attachment(email, msg,cc)
                                email = head_mail[ar]
                                mm.send_email_without_attachment(email, msg, cc)
                                e_mail = 0
                            cv2.putText(faceimg, (ar), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2,
                                        cv2.LINE_AA)


                            tmp_head="no"

                            for xx in data:
                                if xx[0]==ar:
                                    tmp_head=xx[1]

                            name = "fine"
                            if os.path.exists(name):
                                h = 0
                            else:
                                os.mkdir(name)

                            name1 = os.path.join("fine",tmp_head)
                            if os.path.exists(name1):
                                h = 0
                            else:
                                os.mkdir(name1)

                            file1 = os.path.join(name1 , ar+"_"+dt_string+"__"+current_time_str + '.txt')
                            # print(file1)

                            with open((file1), 'w') as f:
                                f.writelines(ar)
                            f.close()
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        video_capture.release()
        cv2.destroyAllWindows()

    def user_login(self):
        user_login_root = Toplevel()
        get_data = smoke_detection()
        w = 580
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
        admin_id2 = canvas1.create_text(290, 100, text="USER LOGIN", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(200, 200, text="Username", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(200, 270, text="Password", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        e1 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(370, 200, window=e1)
        e2 = Entry(canvas1, font=('times', 15, ' bold '), show="*")
        canvas1.create_window(370, 270, window=e2)
        def exit_program():
            a = e1.get()
            b = e2.get().strip()
            smoke_detection.name = a
            if (a == ""):
                messagebox.showinfo(title="Alert", message="Enter Username", parent=user_login_root)
            elif (b == ""):
                messagebox.showinfo(title="Alert", message="Enter Password", parent=user_login_root)
            else:
                qry="select * from user_details where name='" + str(a) + "' and password='" + str(b) + "'"
                # print(qry)
                data = mm.select_direct_query(qry)
                if len(data) > 0:
                    messagebox.showinfo("Result", "Login Success", parent=user_login_root)
                    user_login_root.destroy()
                    tt = smoke_detection()
                    tt.user_home()
                else:
                    messagebox.showinfo("Result", "Login Failed", parent=user_login_root)
        b1 = Button(canvas1, text="Login", command=exit_program, font=('times', 15, ' bold '))
        canvas1.create_window(370, 350, window=b1)
        user_login_root.mainloop()
    def user_home(self):

        user_home = Toplevel()
        def view_data():
            date_list=[]
            TableMargin1 = Frame(user_home, width=650)
            TableMargin1.place(x=100, y=150, width=650, height=255)
            scrollbarx1 = Scrollbar(TableMargin1, orient=HORIZONTAL)
            scrollbary1 = Scrollbar(TableMargin1, orient=VERTICAL)
            tree1 = ttk.Treeview(TableMargin1, columns=("Name","Date","Time"), height=400,
                                selectmode="extended", yscrollcommand=scrollbary1.set, xscrollcommand=scrollbarx1.set)
            scrollbary1.config(command=tree1.yview)
            scrollbary1.pack(side=RIGHT, fill=Y)
            scrollbarx1.config(command=tree1.xview)
            scrollbarx1.pack(side=BOTTOM, fill=X)
            tree1.heading('Name', text="Name", anchor=W)
            tree1.heading('Date', text="Date", anchor=W)
            tree1.heading('Time', text="Time", anchor=W)
            tree1.column('#0', stretch=NO, minwidth=0, width=0)
            tree1.column('#1', stretch=NO, minwidth=0, width=200)
            tree1.column('#2', stretch=NO, minwidth=0, width=200)
            tree1.pack()
            try:
                my_conn = []
                directory="fine"
                files = []
                import os
                root = "fine"
                file_list = []
                for path, subdirs, files in os.walk(root):
                    for name in files:
                        tmp = (os.path.join(path, name))
                        file_list.append(os.path.basename(tmp))
                # print(file_list)
                for xx in file_list:
                    data = (xx.split("_"))
                    data1 = (xx.split("__"))
                    name2 = str(data[0]).strip()
                    date = data[1] + "_" + data[2] + "_" + data[3]
                    time = data1[1]
                    time = time.replace(".txt", "")



                    if name2==str(smoke_detection.name).strip():
                        my_conn.append([name2, date, time])
                for xx in my_conn:
                    tree1.insert("", 0, values=xx)
            except:
                pass

        user_home.attributes('-topmost', 'true')
        get_data = smoke_detection()
        w = 850
        h = 550
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
        admin_id2 = canvas1.create_text(390, 20, text="SMOKE DETAILS", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        view_data()
        user_home.mainloop()
ar=smoke_detection()
root=ar.set_window_design()