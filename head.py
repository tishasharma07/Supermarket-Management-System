import tkinter
from tkinter import *
from PIL import ImageTk,Image
import tkinter.messagebox
import addproducts
import viewproducts
import updateproducts
import billing
class myprogram:
    def open_addproducts(self):
        obj=addproducts.demo()
    def open_viewproducts(self):
        obj=viewproducts.demo()
    def open_updateproducts(self):
        obj=updateproducts.demo()
    def open_raisebill(self):
        obj=billing.billing()
    def __init__(self):#1355x675
        self.root=tkinter.Tk()
        self.root.geometry("1285x685")
        self.root.iconbitmap("iconp.ico")
        self.root.resizable(False,False)
        self.root.title("Login window")
        self.image0 = Image.open("ss.jpg")
        self.photo = ImageTk.PhotoImage(self.image0)
        self.lb1 = Label(self.root, image=self.photo)
        self.lb1.place(x=0, y=0,relwidth=1,relheight=1)
        self.frame_login=Frame(self.root,bg="white")
        self.frame_login.place(x=425,y=25,height=340,width=500)
        self.title=Label(self.frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white")
        self.title.place(x=140,y=25)
        self.title1=Label(self.frame_login,text="Employee Login Area",font=("Goudy old style",15,"bold"),fg="orange",bg="white")
        self.title1.place(x=140,y=90)
        self.lb_user=Label(self.frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white")
        self.lb_user.place(x=50,y=120)
        self.txt_user=Entry(self.frame_login,font=("times new roman",15),bg="lightgrey")
        self.txt_user.place(x=90,y=150,width=350,height=35)
        self.lb_pass=Label(self.frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white")
        self.lb_pass.place(x=50,y=190)
        self.txt_pass=Entry(self.frame_login,font=("times new roman",15),bg="lightgrey")
        self.txt_pass.place(x=90,y=220,width=350,height=35)
        self.login_bt=Button(self.root,text="Login",command=self.login,fg="white",bg="#d77337",font=("times new roman",20))
        self.login_bt.place(x=600,y=340,width=180,height=35)

        self.root.mainloop()

    def login(self):
        if self.txt_pass.get()==""or self.txt_user.get()=="":
            tkinter.messagebox.showerror("ERROR","All fields are required")
        elif self.txt_pass.get()!="a" or self.txt_user.get()!="a":
            tkinter.messagebox.showerror("ERROR","Invalid Username/Password")
        else:
            self.root.destroy()
            self.root2=tkinter.Tk()
            self.root2.geometry("1300x600")
            self.root2.title("WELCOME")
            self.root2.configure(bg="light yellow")
            #self.icon_title=PhotoImage(file="logo.pn'")
            self.welFrame= tkinter.LabelFrame(self.root2, text="Supermarket Management System", font=('arial', 36, 'bold'),bd=15,height=600,width=1300,bg='light yellow')
            self.welFrame.pack()
            self.welframe1 = tkinter.Frame(self.welFrame, bd=10, relief="groove")
            self.welframe1.grid(row=0, column=0, padx=10)
            self.lbfr1 = Label(self.welframe1, text="Product Manangemnet", font=("arial", 25, "bold"), fg="gray",   bg="white",height=3,width=20)
            self.lbfr1.grid(row=0,column=0)
            self.mm1 = Button(self.welframe1, text="Add Products", command=self.open_addproducts, fg="white", bg="#d77337",bd=5,width=20,height=2, font=("times new roman", 25))
            self.mm1.grid(row=1,column=0)
            self.mm2 = Button(self.welframe1, text="View Products", command=self.open_viewproducts, fg="white",
                              bg="#d77337", font=("times new roman", 25),width=20,height=2,bd=5)
            self.mm2.grid(row=2,column=0)
            self.mm3 = Button(self.welframe1, text="Update Products", command=self.open_updateproducts, fg="white",bg="#d77337",width=20,height=2, font=("times new roman", 25),bd=5)
            self.mm3.grid(row=3, column=0)
            self.welframe2 = tkinter.Frame(self.welFrame, bd=10, relief="groove")
            self.welframe2.grid(row=0, column=1, padx=10)
            self.lbfr2 = Label(self.welframe2, text="Billing  Manangemnet", font=("arial", 25, "bold"), fg="gray",
                               bg="white", height=3, width=20)
            self.lbfr2.grid(row=0, column=0)
            self.mm4 = Button(self.welframe2, text="Raise Bill", command=self.open_raisebill, fg="white", bg="#d77337",
                              font=("times new roman", 20),bd=5,width=20,height=3)
            self.mm4.grid(row=1,column=0)



           # self.li = Label(self.root2, text="SuperMarket Management System",  image=self.icon_title,compound=LEFT,font=("times new roman", 40, "bold"), fg="gray",bg="white",anchor="w",padx=20)
            #self.li.place(x=0,y=0,relwidth=1,height=70)
           # self.ll = Label(self.root2, text="Product Management", font=("times new roman", 15, "bold"), fg="gray",bg="white")
           # self.ll.place(x=0,y=0,width=180,height=130)
            ##self.ll.grid(row=0,column=0)
            self.mm1 = Button(self.root2, text="Add Products", command=self.open_addproducts, fg="white", bg="#d77337",font=("times new roman", 20))
           # self.mm1.place(x=0, y=80, width=180, height=150)
            ##self.mm1.grid(row=0, column=1)
            self.mm2 = Button(self.root2, text="View Products", command=self.open_viewproducts, fg="white", bg="#d77337",font=("times new roman", 20))
            #self.mm2.place(x=0, y=240, width=180, height=150)
            ##self.mm2.grid(row=0, column=2)
            self.mm3 = Button(self.root2, text="Update Products", command=self.open_updateproducts, fg="white",bg="#d77337", font=("times new roman", 18))
           # self.mm3.place(x=0, y=400, width=180, height=150)
            ##self.mm3.grid(row=0, column=3)
            self.ll1 = Label(self.root2, text="Billing Management", font=("times new roman", 15, "bold"), fg="gray",
                            bg="white")
           # self.ll1.place(x=190, y=0, width=180, height=130)
            ##self.ll1.grid(row=1, column=0)
            self.mm4 = Button(self.root2, text="Raise Bill", command=self.open_raisebill, fg="white", bg="#d77337",
                              font=("times new roman", 20))
            #self.mm4.place(x=190, y=80, width=180, height=150)
            ##self.mm4.grid(row=1, column=1)
           ## self.root2.resizable(False,False)
           ## self.lb_2=Label(self.root2,text="WELCOME !",font=('CAlibri(Body)',80,'bold'),bg="black",fg="blue")
            ##self.lb_2.place(x=300,y=200)
            self.mymenu = tkinter.Menu(self.root2)
            self.root2.config(menu=self.mymenu)
            self.submenu1 = tkinter.Menu(self.mymenu, tearoff=False)
            self.mymenu.add_cascade(label="Product Management", menu=self.submenu1)
            self.submenu1.add_command(label="Add product", command=self.open_addproducts)
            self.submenu1.add_command(label="View product", command=self.open_viewproducts)
            self.submenu1.add_command(label="Remove product", command=self.open_updateproducts)
            self.submenu2 = tkinter.Menu(self.mymenu, tearoff=False)
            self.mymenu.add_cascade(label="Billing Management", menu=self.submenu2)
            self.submenu2.add_command(label="Raise Bill", command=self.open_raisebill)

            self.root2.mainloop()

            #------------------------------------------
obj=myprogram()

