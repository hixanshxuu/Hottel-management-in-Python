from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
import re

class Customer_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")


        #variables of sql and random no generate
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_pincode = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()

        def validate_contact(event=None):
            contact = txtMobile.get()
            if contact and not re.match(r'^\d{10}$', contact):
                messagebox.showerror("Invalid Input", "Contact should be a 10-digit number")
                txtMobile.focus_set()

        def validate_email(event):
            email = txtEmail.get()
            if email and not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                messagebox.showerror("Invalid Input", "Invalid email format")
                txtEmail.focus_set()

        def validate_pincode(event=None):
            pincode = txtPinCode.get()
            if pincode and not re.match(r'^\d{6}$', pincode):
                messagebox.showerror("Invalid Input", "Pincode should be a 6-digit number")
                txtPinCode.focus_set()

        def validate_name(event=None):
            name = txtcname.get()
            if name and len(name) < 3:
                messagebox.showerror("Invalid Input", "Name should have at least 3 characters")
                txtcname.focus_set()


        def validate_id(event=None):
            id = txtIdNumber.get()
            if id and not re.match(r'^\d{12}$', id):
                messagebox.showerror("Invalid Input", "Input should be a 12-digit number")
                txtIdNumber.focus_set()

        # title
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS",font=("times new roman", 18, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)
        # logo of hotel
        img2 = Image.open(r"C:\Users\HIMANSHU\Desktop\hmspycharm\images\logo.png")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        # label frames
        labelframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("times new roman", 12, "bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #labels and entries
        #customer reference
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref:",font=("arial", 12, "bold"),padx=2, pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,state="readonly",font=("times new roman", 13, "bold"))
        entry_ref.grid(row=0,column=1)

        #customer name
        cname = Label(labelframeleft,font=("arial",12,"bold"),text="Customer Name:",padx=2,pady=6)
        cname.grid(row=1, column=0, sticky=W)
        txtcname = ttk.Entry(labelframeleft, textvariable=self.var_cust_name,width=29, font=("times new roman", 13, "bold"))
        txtcname.grid(row=1, column=1)
        txtcname.bind("<FocusOut>", validate_name)

        #mothers name
        lblmname = Label(labelframeleft,font=("arial", 12, "bold"),text="Mother's Name:", padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky=W)
        txtmname = ttk.Entry(labelframeleft,  textvariable=self.var_mother,width=29, font=("times new roman", 13, "bold"))
        txtmname.grid(row=2, column=1)

        #gender selection
        label_gender = Label(labelframeleft,  font=("arial", 12, "bold"),text="Gender:", padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)

        combo_gender = ttk.Combobox(labelframeleft, textvariable=self.var_gender,font=("arial", 12, "bold"), width=27, state="readonly")
        combo_gender["value"] = ("Select","Male", "Female", "Others")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        #pincode
        lblPinCode = Label(labelframeleft,  font=("arial", 12, "bold"), text="Pincode:",padx=2, pady=6)
        lblPinCode.grid(row=4, column=0, sticky=W)
        txtPinCode = ttk.Entry(labelframeleft,textvariable=self.var_pincode,width=29, font=("times new roman", 13, "bold"))
        txtPinCode.grid(row=4, column=1)
        txtPinCode.bind("<FocusOut>", validate_pincode)

        # contact number
        lblMobile = Label(labelframeleft, font=("arial", 12, "bold"),text="Mobile:", padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)
        txtMobile = ttk.Entry(labelframeleft,textvariable=self.var_mobile, width=29, font=("arial", 13, "bold"))
        txtMobile.grid(row=5, column=1)
        txtMobile.bind("<FocusOut>", validate_contact)

        # mail address
        lblEmail = Label(labelframeleft, font=("arial", 12, "bold"), text="Email:", padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)
        txtEmail = ttk.Entry(labelframeleft,textvariable=self.var_email, width=29, font=("arial", 13, "bold"))
        txtEmail.grid(row=6, column=1)
        txtEmail.bind("<FocusOut>", validate_email)

        # nationailty
        lblNationality = Label(labelframeleft, font=("arial", 12, "bold"), text="Nationality:", padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)

        combo_Nationality = ttk.Combobox(labelframeleft, textvariable=self.var_nationality,font=("arial", 12, "bold"), width=27, state="readonly")
        combo_Nationality["value"] = ("Indian", "British", "Amrerican","Others")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7, column=1)

        # idtype
        lblIdProof = Label(labelframeleft, font=("arial", 12, "bold"), text="Id Proof Type:", padx=2, pady=6)
        lblIdProof.grid(row=8, column=0, sticky=W)

        combo_id = ttk.Combobox(labelframeleft,textvariable=self.var_id_proof, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_id["value"] = ("Adhaar Card","Others")
        combo_id.current(0)
        combo_id.grid(row=8, column=1)

        # id number
        lblIdNumber = Label(labelframeleft, font=("arial", 12, "bold"), text="ID Number:", padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)
        txtIdNumber = ttk.Entry(labelframeleft, textvariable=self.var_id_number,width=29, font=("arial", 13, "bold"))
        txtIdNumber.grid(row=9, column=1)
        txtIdNumber.bind("<FocusOut>", validate_id())

        # address
        lblAddress = Label(labelframeleft, font=("arial", 12, "bold"), text="Address:", padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)
        txtAddress = ttk.Entry(labelframeleft, textvariable=self.var_address,width=29, font=("arial", 13, "bold"))
        txtAddress.grid(row=10, column=1)


        #buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial", 11, "bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate = Button(btn_frame, text="Update",command=self.update, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.mDelete
                           , font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        #label frame and search options
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search",
                                    font=("times new roman", 12, "bold"), padx=2)
        Table_Frame.place(x=435, y=50, width=860, height=490)

        lblSearchBy = Label(Table_Frame, font=("arial", 12, "bold"), text="Search By:",bg="red",fg="white", padx=2, pady=6)
        lblSearchBy.grid(row=0, column=0, sticky=W,padx=2)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame,textvariable=self.search_var, font=("arial", 12, "bold"), width=24, state="readonly")
        combo_Search["value"] = ("Mobile", "Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch = ttk.Entry(Table_Frame,textvariable=self.txt_search, width=24, font=("arial", 13, "bold"))
        txtSearch.grid(row=0, column=2,padx=2)

        btnSearch = Button(Table_Frame, text="Search", command=self.search,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowallTable_Frame = Button(Table_Frame, text="Show all", command=self.fetch_data,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnShowallTable_Frame.grid(row=0, column=4, padx=1)

        # data tables
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table, column=("ref", "name", "mother name", "gender", "pincode" ,"mobile",
                                                                    "email", "nationality", "idproof", "id number", "address")
                                             , xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother name",text="Mother's Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("pincode",text="Pincode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="IDProof")
        self.Cust_Details_Table.heading("id number",text="ID Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother name",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("pincode",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("id number",width=100)
        self.Cust_Details_Table.column("address",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("ERROR","Please fill all the details",parent=self.root)
        else :
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="kaushik@2918",database="python_connector")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_pincode.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer data added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="kaushik@2918",
                                       database="python_connector")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()

            conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_pincode.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("ERROR","Please enter mobile number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="kaushik@2918",
                                           database="python_connector")
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set Name=%s,`Mother Name`=%s,Gender=%s,Pincode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
                self.var_cust_name.get(),
                self.var_mother.get(),
                self.var_gender.get(),
                self.var_pincode.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_address.get(),
                self.var_ref.get()
            ))


            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Updated","Customer details has been updated successfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System", "Do you want to delete the selected data?",parent=self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="kaushik@2918",
                                           database="python_connector")
            my_cursor = conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_pincode.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")

        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="kaushik@2918",
                                       database="python_connector")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()



if __name__ == '__main__':
    root=Tk()
    obj=Customer_window(root)
    root.mainloop()



