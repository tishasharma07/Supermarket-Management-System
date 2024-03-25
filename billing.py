import tkinter
import tkinter.messagebox
import csv
import tkinter.ttk
import datetime
import os,tempfile,smtplib
class billing:
    def raise_bill(self):
        wr=open("bill.csv","a",newline="")
        writer=csv.writer(wr)
        for line in self.t1.get_children():
            row=[]
            for r in self.t1.item(line)["values"]:
                row.append(r)
            row.append(self.txt_date.get())
            row.append(self.txt_billid.get())
            row.append(self.txt_customer_name.get())
            writer.writerow(row)
            print(row)
        print("total payable amount")
        print(self.txt_total_payable.get())

        wr.close()
        self.reset()
    def print_bill(self):
        self.root3=tkinter.Tk()
        self.root3.geometry("600x600")
        """self.lb1= tkinter.Label(self.root3, text="*****************************************************************************************************************************************")
        self.lb1.grid(row=0, column=0)
        self.lb22 = tkinter.Label(self.root3,text="SUPERMARKET STORE")
        self.lb22.grid(row=1, column=0)
        self.lb33 = tkinter.Label(self.root3, text="INVOICE")
        self.lb33.grid(row=1, column=1)"""
        self.billframe=tkinter.Frame(self.root3,bd =10,relief="groove")
        self.billframe.grid(row=0,column=0,padx=10)
        self.billareaLabel=tkinter.Label(self.billframe,text="Bill area",font=('times new roman',15,'bold'),bd=7,relief="groove")
        self.billareaLabel.pack()
        self.scrollbar=tkinter.Scrollbar(self.billframe,orient='vertical')
        self.scrollbar.pack(side="right",fill="y")
        self.textarea=tkinter.Text(self.billframe,height=20,width=55,yscrollcommand=self.scrollbar.set)
        self.textarea.pack()
        self.scrollbar.config(command=self.textarea.yview)
        self.textarea.insert('end','\t\t**Welcome Customer**\n')
        self.textarea.insert('end',f'\nBill Number:{self.txt_billid.get()}\n')
        self.textarea.insert('end', f'\nCustomer Name :{self.txt_customer_name.get()}\n')
        self.textarea.insert('end','\n=======================================================')
        self.textarea.insert('end',' Product code \tProduct Name\t\t\tQuantity\t\t Price\n')
        self.textarea.insert('end', '\n=======================================================')


        wr = open("bill.csv", "a", newline="")
        writer = csv.writer(wr)
        for line in self.t1.get_children():
            row=[]

            for r in self.t1.item(line)["values"]:
                row.append(str(r))
            writer.writerow(row)
              #  display_values =row[1:5]
            displaystr = ",".join(row)
            #print(displaystr)
            values=displaystr.split(",")[1:5]
           # print(values)
            formatted="\t\t".join(values)+'\n'


            self.textarea.insert('end',formatted,'\n')

        self.textarea.insert('end', '\n=======================================================')
       # print("total payable amount")
        self.textarea.insert('end', f'\nTotal Payable amount :{self.txt_total_payable.get()}\n')
        self.textarea.insert('end','\n=======================================================')

        wr.close()
        self.bt_download = tkinter.Button(self.root3, text="download Bill", command=self.download_bill)
        self.bt_download.grid(row=1,column=1)
        self.bt_gmail=tkinter.Button(self.root3,text='Email Bill',command=self.send_email)
        self.bt_gmail.grid(row=2,column=1)
    def send_email(self):
        if(self.textarea.get(1.0,'end')=='\n'):
            tkinter.messagebox.showerror("Error","Bill is Empty")
        else:
            self.root4=tkinter.Tk()
            self.root4.title("send Gmail")
            self.root4.config(bg="light yellow")
            self.root4.resizable(0,0)
            self.senderFrame=tkinter.LabelFrame(self.root4,text="Sender",font=('arial',16,'bold'))
            self.senderFrame.grid(row=0,column=0,padx=40,pady=20)
            self.senderlabel=tkinter.Label(self.senderFrame,text="Sender's Email",font=('arial',14,'bold'))
            self.senderlabel.grid(row=0,column=0,padx=10,pady=8)
            self.senderEntry = tkinter.Entry(self.senderFrame,font=('arial', 14, 'bold'),bd=2,width=23,relief='ridge')
            self.senderEntry.grid(row=0, column=1,padx=10,pady=8)
            self.passwordlabel = tkinter.Label(self.senderFrame, text="Sender's Password", font=('arial', 14, 'bold'))
            self.passwordlabel.grid(row=1, column=0, padx=10, pady=8)
            self.passwordEntry = tkinter.Entry(self.senderFrame, font=('arial', 14, 'bold'), bd=2, width=23,relief='ridge',show="*")
            self.passwordEntry.grid(row=1, column=1, padx=10, pady=8)
            self.recipientFrame = tkinter.LabelFrame(self.root4, text="Recipient", font=('arial', 16, 'bold'))
            self.recipientFrame.grid(row=1, column=0,padx=40,pady=20)
            self.recieverlabel = tkinter.Label(self.recipientFrame, text="Email Address", font=('arial', 14, 'bold'))
            self.recieverlabel.grid(row=0, column=0, padx=10, pady=8)
            self.recieverEntry = tkinter.Entry(self.recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23,
                                             relief='ridge')
            self.recieverEntry.grid(row=0, column=1, padx=10, pady=8)
            self.messagelabel = tkinter.Label(self.recipientFrame, text="Message", font=('arial', 14, 'bold'))
            self.messagelabel.grid(row=1, column=0, padx=10, pady=8)
            self.email_textarea=tkinter.Text(self.recipientFrame,font=('arial',14,'bold'),bd=2,relief='sunken',width=42,height=11)
            self.email_textarea.grid(row=2,column=0,columnspan=2)
            self.email_textarea.delete(1.0,'end')# delete before inserting
            self.email_textarea.insert('end',self.textarea.get(1.0,'end').replace('=','').replace('\t\t\t','\t').replace('\t\t','\t'))

            self.sendButton=tkinter.Button(self.root4,text='SEND',font=('arial',16,'bold'),width=15,command=self.send_gmail)
            self.sendButton.grid(row=2,column=0,pady=20)




            self.root4.mainloop()# to see window continuously

    def send_gmail(self):
        try:
            ob = smtplib.SMTP("smtp.gmail.com", 587)
            ob.starttls()  # establishing secure connection
            ob.login(self.senderEntry.get(), self.passwordEntry.get())
            message = self.email_textarea.get(1.0, 'end')
            # reciever_address=self.recieverEntry.get() # directly pass
            ob.sendmail(self.senderEntry.get(), self.recieverEntry.get(), message)  # from ,to,mrssage
            ob.quit()
            tkinter.messagebox.showinfo("Success", "Bill is Successfully sent")
        except:
            tkinter.messagebox.showerror("ERROR","Something went wrong")



    def download_bill(self):
        if(self.textarea.get(1.0,'end')=='\n'):
            tkinter.messagebox.showerror("Error","bill is empty")
        else:
            file=tempfile.mktemp('.txt')
            open(file,'w').write(self.textarea.get(1.0,'end'))
            os.startfile(file,'print')











    def reset(self):
        self.txt_total_price.delete(0,tkinter.END)
        self.txt_total_discount.delete(0,tkinter.END)
        self.txt_total_payable.delete(0,tkinter.END)
        self.txt_billid.delete(0,tkinter.END)
        self.txt_customer_name.delete(0,tkinter.END)
        self.txt_pid.delete(0,tkinter.END)
        self.txt2_qty.delete(0,tkinter.END)
        for item in self.t1.get_children():
            self.t1.delete(item)

    def add_to_cart(self):
        if self.txt_customer_name.get()=="":
            tkinter.messagebox.showerror("SUPERMARKET","Invalid Customer name")
        elif not self.txt_billid.get().isdigit():
            tkinter.messagebox.showerror("SUPERMARKET","enter valid id")
        elif self.txt_customer_name.get().isdigit():
            tkinter.messagebox.showerror("SUPERMARKET","enter valid customer name")
        elif not self.txt_pid.get().isdigit():
            tkinter.messagebox.showerror("SUPERMARKET","Invalid product code")
        elif not self.txt2_qty.get().isdigit():
            tkinter.messagebox.showerror("SUPERMARKET","Invalid quantity")
        else:
            rd=open("products.csv","r")
            reader=csv.reader(rd)
            flag=False
            for row in reader:
                if str(row[0])==str(self.txt_pid.get()):
                    flag=True
                    pname=row[1]
                    price=row[3]
                    discount=row[4]
                    netprice=int(price)-int(price)*float(discount)/100
                    self.tp=self.tp+int(price)*int(self.txt2_qty.get())
                    self.total_discount=self.total_discount+float(discount)*int(self.txt2_qty.get())
                    total=netprice*int(self.txt2_qty.get())
                    self.total_payable=self.total_payable+total
                    break
            if flag==True:
                self.srno = self.srno + 1
                item = self.srno, self.txt_pid.get(), pname, self.txt2_qty.get(), price, discount, netprice, total
                self.t1.insert("", index=self.srno, values=item)
                self.txt_total_price.delete(0, tkinter.END)
                self.txt_total_price.insert(0, str(self.tp))
                self.txt_total_payable.delete(0, tkinter.END)
                self.txt_total_payable.insert(0, str(self.total_payable))
                self.txt_total_discount.delete(0, tkinter.END)
                self.txt_total_discount.insert(0, str(self.total_discount))
            else:
                tkinter.messagebox.showerror("SUPER STORE", "Invalid Product")

    def __init__(self):
        self.root=tkinter.Tk()
        self.root.configure(bg="light yellow")
        self.srno=0
        self.tp=0
        self.total_discount=0
        self.total_payable=0
        self.root.geometry("1000x800")
        self.p1=tkinter.PanedWindow(self.root)
        self.p2=tkinter.PanedWindow(self.root)
        self.p3=tkinter.PanedWindow(self.root)
        self.p1.pack()
        self.p2.pack()
        self.p3.pack()
        self.bt_bill=tkinter.Button(self.p3,text="Raise Bill",command=self.raise_bill)
        self.bt_print=tkinter.Button(self.p3,text="Print Bill",command=self.print_bill )

        self.lb_total_price=tkinter.Label(self.p3,text="Total Price")
        self.txt_total_price=tkinter.Entry(self.p3)
        self.lb_total_discount=tkinter.Label(self.p3,text="Total Discount")
        self.txt_total_discount=tkinter.Entry(self.p3)
        self.lb_total_payable=tkinter.Label(self.p3,text="Total Payable amount")
        self.txt_total_payable=tkinter.Entry(self.p3)
        self.bt1=tkinter.Button(self.p1,text="Add to Cart",command=self.add_to_cart)
        self.lb_date=tkinter.Label(self.p1,text="Date")
        self.txt_date=tkinter.Entry(self.p1)
        self.lb_billid=tkinter.Label(self.p1,text="Enter bill no. ")
        self.txt_billid=tkinter.Entry(self.p1)
        self.lb_customer_name=tkinter.Label(self.p1,text="Enter Customer Name")
        self.txt_customer_name=tkinter.Entry(self.p1)
        self.lb_pid=tkinter.Label(self.p1,text="Enter Product Code")
        self.txt_pid=tkinter.Entry(self.p1)
        self.lb2_qty=tkinter.Label(self.p1,text="Quantity")
        self.txt2_qty=tkinter.Entry(self.p1)
        self.t1=tkinter.ttk.Treeview(self.p2,columns=("srno","pid","pname","qty","price","discount","netprice","totalprice"))
        self.t1.column("srno",width=15)
        self.t1.heading("srno",text="S NO.")
        self.t1.heading("pid",text="PRODUCT CODE")
        self.t1.heading("pname",text="PRODUCT NAME")
        self.t1.heading("qty",text="QUANTITY")
        self.t1.heading("price",text="PRICE")
        self.t1.heading("discount",text="DISCOUNT")
        self.t1.heading("netprice",text="NET PRICE")
        self.t1.heading("totalprice",text="TOTAL PRICE")
        self.t1["show"]="headings"
        self.lb_date.grid(row=0,column=0)
        self.txt_date.grid(row=0,column=1)
        self.lb_billid.grid(row=0,column=10)
        self.txt_billid.grid(row=0,column=11)
        self.lb_customer_name.grid(row=2,column=2)
        self.txt_customer_name.grid(row=2,column=3)
        self.lb_pid.grid(row=4,column=0)
        self.txt_pid.grid(row=4,column=1)
        self.lb2_qty.grid(row=4,column=2)
        self.txt2_qty.grid(row=4,column=3)
        self.bt1.grid(row=4,column=4)
        self.lb_total_price.grid(row=0,column=0)
        self.txt_total_price.grid(row=0,column=1)
        self.lb_total_payable.grid(row=2,column=0)
        self.txt_total_payable.grid(row=2,column=1)
        self.lb_total_discount.grid(row=1,column=0)
        self.txt_total_discount.grid(row=1,column=1)
        self.bt_bill.grid(row=3,column=1)
        self.bt_print.grid(row=3,column=3)

        self.t1.pack()
        self.txt2_qty.insert(0,"1")
        self.txt_date.insert(0,datetime.date.today())
        self.txt_pid.bind('<Return>',self.add_to_cart)
        self.root.mainloop()
#--------------------------------------------------------------------------------------------------
#obj=billing()