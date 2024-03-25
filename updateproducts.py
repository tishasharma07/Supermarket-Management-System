import tkinter
import tkinter.messagebox
import tkinter.ttk
import csv
import os
class demo:
    def remove_record(self):
        rd = open("products.csv","r")
        wr=open("temp.csv", "w", newline="")
        reader=csv.reader(rd)
        writer=csv.writer(wr)
        for row in reader:
            if row[0]==self.txt1.get():
                tkinter.messagebox.showinfo("supermarket","record removed")
            else:
                writer.writerow(row)
        wr.close()
        rd.close()
        os.remove("products.csv")
        os.rename("temp.csv", "products.csv")

    def search(self):
        rd=open("products.csv","r")
        reader=csv.reader(rd)
        for row in reader:
            if row[0]==self.txt1.get():
                self.txt2.insert(0,row[1])
                self.cb1.set(row[3])
                self.txt3.insert(0,row[2])
                self.txt4.insert(0,row[4])
                self.txt5.insert(0,row[5])
                break
        rd.close()
    def reset(self):
        self.txt1.delete(0,tkinter.END)
        self.txt2.delete(0,tkinter.END)
        self.txt3.delete(0,tkinter.END)
        self.txt4.delete(0,tkinter.END)
        self.txt5.delete(0,tkinter.END)
        self.cb1.set('')

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("500x300")
        self.root.configure(bg="light yellow")
        self.root.title(" Update Product Details")
        self.lb1 = tkinter.Label(self.root, text="Enter Product ID")
        self.txt1 = tkinter.Entry(self.root)
        self.bt2=tkinter.Button(self.root,text="search",command=self.search)
        self.lb2 = tkinter.Label(self.root, text="Enter Product Name")
        self.txt2 = tkinter.Entry(self.root)
        self.lb3 = tkinter.Label(self.root, text="Enter Product Category")
        self.cb1 = tkinter.ttk.Combobox(self.root, state="readonly", values=("FMCG", "COSMATICS", "FRUITS", "VEGETABLES"))
        self.lb4 = tkinter.Label(self.root, text="Enter price")
        self.txt3 = tkinter.Entry(self.root)
        self.lb5 = tkinter.Label(self.root, text="Enter discount")
        self.txt4 = tkinter.Entry(self.root)
        self.lb6 = tkinter.Label(self.root, text="Enter offer")
        self.txt5 = tkinter.Entry(self.root)
        self.bt1 = tkinter.Button(self.root, text="remove Products", command=self.remove_record)
        self.bt3=tkinter.Button(self.root,text="reset",command=self.reset)
        self.lb1.grid(row=0, column=0)
        self.lb2.grid(row=1, column=0)
        self.lb3.grid(row=2, column=0)
        self.lb4.grid(row=3, column=0)
        self.lb5.grid(row=4, column=0)
        self.lb6.grid(row=5, column=0)
        self.txt1.grid(row=0, column=1)
        self.txt2.grid(row=1, column=1)
        self.txt3.grid(row=3, column=1)
        self.txt4.grid(row=4, column=1)
        self.txt5.grid(row=5, column=1)
        self.cb1.grid(row=2, column=1)
        self.bt1.grid(row=6, column=1)
        self.bt2.grid(row=0,column=2)
        self.bt3.grid(row=6,column=2)
        self.root.mainloop()
    # ----------------------------------------------


#obj = demo()


