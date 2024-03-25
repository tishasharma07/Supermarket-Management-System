import tkinter
import tkinter.ttk
import csv
class demo:
    def __init__(self):
        self.root=tkinter.Tk()
        self.root.configure(bg="light yellow")
        self.t1=tkinter.ttk.Treeview(self.root,columns=("product code","product name","category","price","discount","offer"))
        self.t1.heading("product code",text="PRODUCT ID")
        self.t1.heading("product name",text="PRODUCT NAME")
        self.t1.heading("category",text="PRODUCT CATEGORY")
        self.t1.heading("price",text="PRODUCT PRICE")
        self.t1.heading("discount",text="PRODUCT DISCOUNT ")
        self.t1.heading("offer",text="PRODUCT OFFER")
        self.t1.pack()
        self.t1["show"]="headings"
        rd=open("products.csv","r")
        reader=csv.reader(rd)
        i=0
        for row in reader:
            self.t1.insert("",index=i,values=row)
            i=i+1
        rd.close()
        self.root.mainloop()


#------------------------------------------------
#obj=demo()





