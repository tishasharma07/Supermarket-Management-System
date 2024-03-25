import tkinter
import tkinter.messagebox
import tkinter.ttk
import csv
class demo:
    def product_exist(self,productcode):
        rd=open("products.csv","r")
        reader=csv.reader(rd)
        flag=False
        for p in reader:
            if p[0]==productcode:
                flag=True
                break
        return flag
    def reset(self):
        self.txt1.delete(0,tkinter.END)
        self.txt2.delete(0,tkinter.END)
        self.txt3.delete(0,tkinter.END)
        self.txt4.delete(0,tkinter.END)
        self.txt5.delete(0,tkinter.END)
        self.cb1.set('')
    def add_products(self):
        if self.txt1.get()=="":
            tkinter.messagebox.showerror("SUPERMARKET","Product Code Is Mandatory")
        elif self.txt2.get()=="":
            tkinter.messagebox.showerror("SUPERMARKET","Product name Is Mandatory")
        elif self.txt3.get()=="":
             tkinter.messagebox.showerror("SUPERMARKET","Product Price Is Mandatory")
        elif self.txt4.get() == "":
             tkinter.messagebox.showerror("SUPERMARKET", "Product Discount")

        elif not self.txt3.get().isdigit() or not self.txt4.get().isdigit():
            tkinter.messagebox.showerror("SUPERMARKET","Enter valid price or discount")
        elif self.product_exist(self.txt1.get()):
            tkinter.messagebox.showerror("SUPERMARKET","Product Already Exist")
        else:
            x=[self.txt1.get(),self.txt2.get(),self.cb1.get(),self.txt3.get(),self.txt4.get(),self.txt5.get()]
            wr=open("products.csv","a",newline="")
            writer=csv.writer(wr)
            writer.writerow(x)
            wr.close()
            tkinter.messagebox.showinfo("SUPERMARKET","Product Added Successfully")
            self.reset()

    def __init__(self):
        self.root=tkinter.Tk()
        self.root.configure(bg="light yellow")
        self.root.geometry("500x300")
        self.root.title("Product Details")
        self.lb1=tkinter.Label(self.root,text="Enter Product ID")
        self.txt1=tkinter.Entry(self.root)
        self.lb2=tkinter.Label(self.root,text="Enter Product Name")
        self.txt2=tkinter.Entry(self.root)
        self.lb3=tkinter.Label(self.root,text="Enter Product Category")
        self.cb1=tkinter.ttk.Combobox(self.root,state="readonly",values=("FMCG","COSMETICS","FRUITS","VEGETABLES","CLEANING SOLUTIONS"))
        self.lb4=tkinter.Label(self.root,text="Enter price")
        self.txt3=tkinter.Entry(self.root)
        self.lb5=tkinter.Label(self.root,text="Enter discount")
        self.txt4=tkinter.Entry(self.root)
        self.lb6=tkinter.Label(self.root,text="Enter offer")
        self.txt5=tkinter.Entry(self.root)
        self.bt1=tkinter.Button(self.root,text="Add Products",command=self.add_products)
        self.lb1.grid(row=0,column=0)
        self.lb2.grid(row=1,column=0)
        self.lb3.grid(row=2,column=0)
        self.lb4.grid(row=3,column=0)
        self.lb5.grid(row=4,column=0)
        self.lb6.grid(row=5,column=0)
        self.txt1.grid(row=0,column=1)
        self.txt2.grid(row=1,column=1)
        self.txt3.grid(row=3,column=1)
        self.txt4.grid(row=4,column=1)
        self.txt5.grid(row=5,column=1)
        self.cb1.grid(row=2,column=1)
        self.bt1.grid(row=6,column=1)
        self.root.mainloop()

#----------------------------------------------
#obj=demo()



