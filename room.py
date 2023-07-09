from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox
from tkcalendar import DateEntry
import datetime

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #variables to store data

        self.var_contact=StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noOfdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualcost = StringVar()
        self.var_total = StringVar()






        # title
        lbl_title = Label(self.root, text="Room Booking Details", font=("times new roman", 18, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # logo of hotel
        img2 = Image.open(r"C:\Users\HIMANSHU\Desktop\hmspycharm\images\logo.png")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

       #labels and entries
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Details",
                                    font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # customer reference
        lbl_cust_contact= Label(labelframeleft, text="Customer CONTACT:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        entry_contact = ttk.Entry(labelframeleft, textvariable=self.var_contact,width=20,font=("times new roman", 13, "bold"))
        entry_contact.grid(row=0, column=1,sticky=W)



        # button for fetching data
        btnFetchdata = Button(labelframeleft, text="Fetch Data", command=self.Fetch_contact,font=("arial", 8, "bold"), bg="black", fg="gold",
                        width=8)

        btnFetchdata.place(x=347,y=4)

        #check in date
        today = datetime.date.today()
        check_in_date=Label(labelframeleft,font=("arial",12,"bold"),text="Check-in Date:",padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=DateEntry(labelframeleft,textvariable=self.var_checkin,mindate=today,font=("arial",13,"bold"),width=22)
        txtcheck_in_date.grid(row=1,column=1)

        # check out date
        check_out_date = Label(labelframeleft, font=("arial", 12, "bold"), text="Check-out Date:", padx=2, pady=6)
        check_out_date.grid(row=2, column=0, sticky=W)
        txtcheck_out_date = DateEntry(labelframeleft, textvariable=self.var_checkout,mindate=today,font=("arial", 13, "bold"), width=22)
        txtcheck_out_date.grid(row=2, column=1)

        # room type
        lblRoomType = Label(labelframeleft, font=("arial", 12, "bold"), text="Room Type:", padx=2, pady=6)
        lblRoomType.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="kaushik@2918",
                                       database="python_connector")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide = my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        # room availability
        lblRoomAvailable = Label(labelframeleft, font=("arial", 12, "bold"), text="Available Rooms:", padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)
        #txtRoomAvailable = ttk.Entry(labelframeleft, textvariable=self.var_roomavailable,font=("arial", 13, "bold"), width=29)
        #txtRoomAvailable.grid(row=4, column=1)

        conn = mysql.connector.connect(host="localhost", username="root", password="kaushik@2918",
                                       database="python_connector")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows = my_cursor.fetchall()

        combo_RoomNo = ttk.Combobox(labelframeleft, textvariable=self.var_roomavailable, font=("arial", 12, "bold"),
                                      width=27, state="readonly")
        combo_RoomNo["value"] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)


        #meals
        lblMeal = Label(labelframeleft, font=("arial", 12, "bold"), text="Food:", padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)
        combo_Meal = ttk.Combobox(labelframeleft, textvariable=self.var_meal, font=("arial", 12, "bold"),
                                      width=27, state="readonly")
        combo_Meal["value"] = ("Select", "Breakfast & Lunch (Rs 300)", "Only Lunch (Rs 150)", "Lunch & Dinner (Rs 350)", "Breakfast & Dinner (Rs 300)", "3 Meals (Rs 450)", "No meals")
        combo_Meal.current(0)
        combo_Meal.grid(row=5, column=1)


        #number of days
        lblNoOfDays = Label(labelframeleft, font=("arial", 12, "bold"), text="No of Days:", padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(labelframeleft, textvariable=self.var_noOfdays,font=("arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=6, column=1)



        # tax paid
        lblNoOfDays = Label(labelframeleft, font=("arial", 12, "bold"), text="Tax Paid:", padx=2, pady=6)
        lblNoOfDays.grid(row=7, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(labelframeleft, textvariable=self.var_paidtax,font=("arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=7, column=1)


        # sub total
        lblNoOfDays = Label(labelframeleft, font=("arial", 12, "bold"), text="Room charge:", padx=2, pady=6)
        lblNoOfDays.grid(row=8, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(labelframeleft, textvariable=self.var_actualcost,font=("arial",13, "bold"), width=29)
        txtNoOfDays.grid(row=8, column=1)


        # total calculation
        lblIDNumber = Label(labelframeleft, font=("arial", 12, "bold"), text="Total Cost :", padx=2, pady=6)
        lblIDNumber.grid(row=9, column=0, sticky=W)
        txtIDNumber = ttk.Entry(labelframeleft,textvariable=self.var_total, font=("arial", 13, "bold"), width=29)
        txtIDNumber.grid(row=9, column=1)


        # bill button on room

        btnBill = Button(labelframeleft, text="BILL",command=self.total, font=("arial", 11, "bold"), bg="black", fg="gold",
                        width=10)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)



        # buttons from customer frame

        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="ADD",command = self.add_data, font=("arial", 11, "bold"), bg="black", fg="gold",
                        width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update",command=self.update,font=("arial", 11, "bold"), bg="black",
                           fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete"
                           ,command=self.mDelete, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset,font=("arial", 11, "bold"), bg="black",
                          fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)


        # right side image in room window

        img3 = Image.open(r"C:\Users\HIMANSHU\Desktop\hmspycharm\images\roombed.jpg")
        img3 = img3.resize((520, 300), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=760, y=55, width=520, height=200)



        #search system in room window

        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search",
                                 font=("times new roman", 12, "bold"), padx=2)
        Table_Frame.place(x=435, y=280, width=860, height=260)

        lblSearchBy = Label(Table_Frame, font=("arial", 12, "bold"), text="Search By:", bg="red", fg="white", padx=2,
                            pady=6)
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=24,
                                    state="readonly")
        combo_Search["value"] = ("Contact", "Room")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_search, width=24, font=("arial", 13, "bold"))
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search", command=self.search,font=("arial", 11, "bold"), bg="black",
                           fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowallTable_Frame = Button(Table_Frame, text="Show all", command=self.fetch_data,
                                       font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnShowallTable_Frame.grid(row=0, column=4, padx=1)



        # data tables from customer window

        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table,
                                               column=("contact", "checkin", "checkout", "roomtype","roomavailable", "meal", "noOfdays")
                                               , xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="contact")
        self.room_table.heading("checkin", text="check-in")
        self.room_table.heading("checkout", text="check-out")
        self.room_table.heading("roomtype", text="room type")
        self.room_table.heading("roomavailable", text="room available")
        self.room_table.heading("meal", text="meal")
        self.room_table.heading("noOfdays", text="noOfdays")


        self.room_table["show"] = "headings"

        self.room_table.column("contact", width=100)
        self.room_table.column("checkin", width=100)
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noOfdays", width=100)
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()


    # adding data in boxes
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("ERROR","Please fill all the details",parent=self.root)
        else :
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="kaushik@2918",database="python_connector")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_contact.get(),
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noOfdays.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","ROOM BOOKED",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Something went wrong:{str(es)}",parent=self.root)

    #fetching data from db
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="kaushik@2918",
                                       database="python_connector")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()

            conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noOfdays.set(row[6])

    # update button
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("ERROR","Please enter mobile number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="kaushik@2918",
                                           database="python_connector")
            my_cursor = conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where contact=%s",(
            self.var_checkin.get(),
            self.var_checkout.get(),
            self.var_roomtype.get(),
            self.var_roomavailable.get(),
            self.var_meal.get(),
            self.var_noOfdays.get(),
            self.var_contact.get()
            ))


            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Updated","Room details has been updated successfully",parent=self.root)


    # delete button work
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System", "Do you want to delete the selected data?",parent=self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="kaushik@2918",
                                           database="python_connector")
            my_cursor = conn.cursor()
            query="delete from room where contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    #reset button work
    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noOfdays.set("")
        self.var_paidtax.set("")
        self.var_actualcost.set("")
        self.var_total.set("")




    #data fetch by conatct

    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("error","please enter contact number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="kaushik@2918",
                                           database="python_connector")
            my_cursor = conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","number not found", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=180)

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=0)

                # data fetch by gender

                conn = mysql.connector.connect(host="localhost", username="root", password="kaushik@2918",
                                               database="python_connector")
                my_cursor = conn.cursor()
                query = ("select Gender from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGender = Label(showDataframe, text="Gender:", font=("arial", 12, "bold"))
                lblGender.place(x=0, y=30)

                lbl = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=30)

                # data fetch by email

                conn = mysql.connector.connect(host="localhost", username="root", password="kaushik@2918",
                                               database="python_connector")
                my_cursor = conn.cursor()
                query = ("select Email from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblEmail = Label(showDataframe, text="Email:", font=("arial", 12, "bold"))
                lblEmail.place(x=0, y=60)

                lbl = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=60)


                # data fetching from nationality

                conn = mysql.connector.connect(host="localhost", username="root", password="kaushik@2918",
                                               database="python_connector")
                my_cursor = conn.cursor()
                query = ("select Nationality from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblNationality = Label(showDataframe, text="Nationality:", font=("arial", 12, "bold"))
                lblNationality.place(x=0, y=90)

                lbl = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=90)


                # data fetching from address

                conn = mysql.connector.connect(host="localhost", username="root", password="kaushik@2918",
                                               database="python_connector")
                my_cursor = conn.cursor()
                query = ("select Address from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblAddress = Label(showDataframe, text="Address:", font=("arial", 12, "bold"))
                lblAddress.place(x=0, y=120)

                lbl = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=120)

    #search system in room window
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="kaushik@2918",
                                       database="python_connector")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # working on bill button to calculate no of days and amounts
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate = datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noOfdays.set(abs(outDate-inDate).days)

        if(self.var_meal.get()=="Breakfast & Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(800)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3 * q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualcost.set(ST)
            self.var_total.set(TT)

        if (self.var_meal.get() == "Only Lunch" and self.var_roomtype.get() == "Single"):
            q1 = float(100)
            q2 = float(800)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualcost.set(ST)
            self.var_total.set(TT)

        if (self.var_meal.get() == "Lunch & Dinner" and self.var_roomtype.get() == "Single"):
            q1 = float(100)
            q2 = float(800)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualcost.set(ST)
            self.var_total.set(TT)

        if (self.var_meal.get() == "Breakfast & Dinner" and self.var_roomtype.get() == "Single"):
            q1 = float(250)
            q2 = float(800)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualcost.set(ST)
            self.var_total.set(TT)

        if (self.var_meal.get() == "3 Meals" and self.var_roomtype.get() == "Single"):
            q1 = float(400)
            q2 = float(800)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualcost.set(ST)
            self.var_total.set(TT)

        if (self.var_meal.get() == "Breakfast & Lunch" and self.var_roomtype.get() == "Luxury"):
            q1 = float(300)
            q2 = float(1500)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualcost.set(ST)
            self.var_total.set(TT)

        if (self.var_meal.get() == "Only Lunch" and self.var_roomtype.get() == "Luxury"):
            q1 = float(100)
            q2 = float(1500)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualcost.set(ST)
            self.var_total.set(TT)

        if (self.var_meal.get() == "Lunch & Dinner" and self.var_roomtype.get() == "Luxury"):
            q1 = float(100)
            q2 = float(1500)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualcost.set(ST)
            self.var_total.set(TT)

        if (self.var_meal.get() == "Breakfast & Dinner" and self.var_roomtype.get() == "Luxury"):
            q1 = float(250)
            q2 = float(1500)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualcost.set(ST)
            self.var_total.set(TT)

        if (self.var_meal.get() == "3 Meals" and self.var_roomtype.get() == "Luxury"):
            q1 = float(400)
            q2 = float(1500)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualcost.set(ST)
            self.var_total.set(TT)


if __name__ == '__main__':
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()