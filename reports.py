from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox

class ReportsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Reports Room")
        self.root.geometry("1295x550+230+220")

        # title
        lbl_title = Label(self.root, text="ALL RECORDS", font=("times new roman", 18, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # logo of hotel
        img2 = Image.open(r"C:\Users\HIMANSHU\Desktop\hmspycharm\images\logo.png")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)



        # search system in room window
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search",
                                 font=("times new roman", 12, "bold"), padx=2)
        Table_Frame.place(x=0, y=0, width=1295, height=350)

        # Treeview widget to display records
        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.room_table = ttk.Treeview(Table_Frame, columns=("name", "mobile", "checkin", "checkout", "roomtype",
                                                             "roomno", "noOfdays"), xscrollcommand=scroll_x.set,
                                      yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        self.room_table.heading("name", text="contact")
        self.room_table.heading("mobile", text="Check_in")
        self.room_table.heading("checkin", text="Check-Out")
        self.room_table.heading("checkout", text="Room type")
        self.room_table.heading("roomtype", text="Room No")
        self.room_table.heading("roomno", text="Meal")
        self.room_table.heading("noOfdays", text="no of days")
        self.room_table["show"] = "headings"
        self.room_table.pack(fill=BOTH, expand=1)

        # Call function to fetch and display records
        self.display_records()

    def display_records(self):
        # Connect to MySQL database and fetch records
        conn = mysql.connector.connect(host="localhost", user="root", password="kaushik@2918", database="python_connector")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM room")
        records = cursor.fetchall()


        # Clear existing records
        self.room_table.delete(*self.room_table.get_children())

        # Insert fetched records into Treeview
        for record in records:
            self.room_table.insert("", END, values=record)

        # Close cursor and connection
        cursor.close()
        conn.close()

if __name__ == '__main__':
    root = Tk()
    obj = ReportsRoom(root)
    root.mainloop()
