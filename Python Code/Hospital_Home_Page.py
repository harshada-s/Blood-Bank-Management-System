import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter import ttk
import Main_Page
from tkinter import messagebox



class HospitalHomePage(tk.Frame):
    def __init__(self, parent, username,user,pswd):
        super().__init__(parent, bg="#B71C1C")
        self.username=username
        self.user=user
        self.pswd=pswd

        tk.Label(self, text="Welcome!", font=("Arial", 20, "bold"), fg="white", bg="#B71C1C").pack(pady=20)
        
        create_request_button = tk.Button(self, text="Create New Request", command=self.create_request_page, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        create_request_button.pack(pady=20)
        
        view_request_button = tk.Button(self, text="View Requests", command=self.view_request_page, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        view_request_button.pack(pady=20)
        
        back_button = tk.Button(self, text="Back", command=self.back, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        back_button.pack(side=tk.BOTTOM, padx=20, pady=20)
        
    def create_request_page(self):
         self.destroy()
         create_request_obj = CreateRequestPage(self.master,self.username,self.user,self.pswd)
         create_request_obj.pack()
         
    def view_request_page(self):
         self.destroy()
         view_request_obj = ViewRequestPage(self.master, self.username,self.user,self.pswd)
         view_request_obj.pack()
         
         
    def back(self):
       self.destroy()
       self.master.home_page = Main_Page.MainPage(self.master,self.user,self.pswd)
       self.master.home_page.pack()
         
         
class CreateRequestPage(tk.Frame):
    def __init__(self, parent, username,user,pswd):
        super().__init__(parent, bg="#B71C1C")
        self.username=username
        self.user=user
        self.pswd=pswd

        tk.Label(self, text="Enter Blood Group:", font=("Arial", 14, "bold"), fg="white", bg="#B71C1C").pack(pady=10)
        self.bloodgroup_entry = tk.Entry(self, font=("Arial", 14))
        self.bloodgroup_entry.pack(pady=10)
        
        tk.Label(self, text="Enter Amount:", font=("Arial", 14, "bold"), fg="white", bg="#B71C1C").pack(pady=10)
        self.amount_entry = tk.Entry(self, font=("Arial", 14))
        self.amount_entry.pack(pady=10)
        
        create_button = tk.Button(self, text="Create", command=self.create_request, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        create_button.pack(pady=20)
        
        home_button = tk.Button(self, text="Home", command=lambda:[self.destroy(),HospitalHomePage(self.master,username,self.user,self.pswd).pack()],font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        home_button.pack(pady=20)
        
        
    def create_request(self):
        bloodgroup=self.bloodgroup_entry.get()
        amount=self.amount_entry.get()
        
        db = mysql.connector.connect(
            host="localhost",
            user=self.user,
            password=self.pswd,
            database="bloodbankdb"
        )
        try:
            cursor = db.cursor()
            if(len(bloodgroup)>0 and len(amount)>0):
                cursor.execute("SELECT hospital_name from hospital where hpt_username=%s",(self.username,))
                hospital=cursor.fetchone()[0]
                cursor.execute("INSERT INTO request (requested_blood_group, requested_amount, hospital_name) VALUES (%s,%s,%s)", (bloodgroup,amount,hospital))
                messagebox.showinfo("success", "Request created successfully!")
                db.commit()
            elif len(bloodgroup)>0:
                messagebox.showerror("showerror", "Please enter an amount")
            elif len(amount)>0:
                messagebox.showerror("showerror", "Please enter a blood group type")
        except mysql.connector.Error as e:
            messagebox.showerror("showerror", "Please enter the correct blood group type")
        finally:
            cursor.close()
            db.close()
          
            
class ViewRequestPage(tk.Frame):
    def __init__(self, parent, username,user,pswd):
        super().__init__(parent, bg="#B71C1C")
        self.username=username
        self.user=user
        self.pswd=pswd
        
        self.center_frame = tk.Frame(self, background="#B71C1C",width=800,height=200)
        self.center_frame.pack(pady=10, side='bottom')
        tk.Label(self, text="Filter by Blood Group:", font=("Arial", 14, "bold"), fg="white", bg="#B71C1C").pack(pady=10)
        self.bloodgroup_entry = tk.Entry(self, font=("Arial", 14))
        self.bloodgroup_entry.pack(pady=10)
        
        tk.Label(self, text="Filter by Status: Enter 1 for open requests and 0 for closed", font=("Arial", 14, "bold"), fg="white", bg="#B71C1C").pack(pady=10)
        self.status_entry = tk.Entry(self, font=("Arial", 14))
        self.status_entry.pack(pady=10)
        
        search_button = tk.Button(self, text="Search", command=self.get_request, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        search_button.pack(pady=20)
        
        clear_filters_button = tk.Button(self, text="Clear", command=self.clearfilters, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        clear_filters_button.pack(pady=20)
        
        home_button = tk.Button(self, text="Home", command=lambda:[self.destroy(),HospitalHomePage(self.master,username,self.user,self.pswd).pack()],font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        home_button.pack(pady=20)

          

    def get_request(self):
        self.center_frame.destroy()
        bloodgroup=self.bloodgroup_entry.get()
        status=self.status_entry.get()
        
        default_headings=[]
        columns=[]
        
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password@123",
            database="bloodbankdb"
        )
        cursor = db.cursor()
        cursor.execute("SELECT hospital_name from hospital where hpt_username=%s",(self.username,))
        hospital=cursor.fetchone()[0]
        if len(status)>0:
            cursor.execute("call get_request(%s,%s,%s)",(hospital,bloodgroup,status))
            
        else:
            cursor.execute("call get_request(%s,%s,NULL)",(hospital,bloodgroup))
        result = cursor.fetchall()
        for i,col in enumerate(cursor.column_names):
            columns.append("col"+str(i))
            default_headings.append(col)
        self.center_frame = tk.Frame(self, background="#B71C1C",width=800,height=200)
        self.center_frame.pack(pady=10, side='bottom')
        tree = ttk.Treeview(self.center_frame, columns = columns, show = 'headings')
        for index, col in enumerate(columns):
            tree.column(col, width = 150, anchor = 'center')
            tree.heading(col, text=default_headings[index])
        scrollbar = ttk.Scrollbar(self.center_frame, orient = tk.VERTICAL, command = tree.yview)
        tree.configure(yscroll = scrollbar.set)
        tree.grid(row = 0, column = 0)
        scrollbar.grid(row = 0, column = 1)
        for index in range(len(result)):
            tree.insert('', tk.END, values=result[index])
            
            
        cursor.close()
        db.close()
            
          
    def clearfilters(self):
        self.bloodgroup_entry.delete(0, tk.END)
        self.status_entry.delete(0, tk.END)
        
        