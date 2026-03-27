import os
from tkinter import *
from tkinter import messagebox

from sample_data import student
class main_add_student:
    def add(self):


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
            Button(sc1, text='OK', command=del_sc1, fg="black", bg="#42bcf5", width=9, height=1, activebackground="Red",
                   font=('times', 15, ' bold ')).place(x=90, y=50)

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
                import test

        def testing():
            import test_1

        root = Tk()
        w = 780
        h = 500
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root.title("SMOKE DETECTION")
        message = Label(root, text="SMOKE DETECTION & FACE RECOGNITION", fg="#004080", width=45, height=3,
                        font=('times', 20, 'italic bold '))
        message.place(x=12, y=20)

        lbl = Label(root, text="USERNAME", width=20, height=2, fg="black", font=('times', 15, ' bold '))
        lbl.place(x=30, y=200)

        txt = Entry(root, validate="key", width=20, font=('times', 25, ' bold '))
        txt.place(x=300, y=200)

        compare_dataset = Button(root, text="TRAINING", width=15, height=1, fg="#FFF", bg="#004080", command=training,
                                 activebackground="orange", activeforeground="white", font=('times', 15, ' bold '))
        compare_dataset.place(x=250, y=350)

        resust_dataset = Button(root, text="TESTING", width=15, height=1, fg="#FFF", bg="#004080", command=testing,
                                activebackground="orange", activeforeground="white", font=('times', 15, ' bold '))
        resust_dataset.place(x=450, y=350)
        # components()
        root.mainloop()
