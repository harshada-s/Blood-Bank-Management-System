import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Main_Page

class LabTechnicianHomePage(tk.Frame):
    def __init__(self, parent, username,user,pswd):
        super().__init__(parent, bg="#B71C1C")
        self.username=username
        self.user=user
        self.pswd=pswd

        tk.Label(self, text="Welcome!", font=("Arial", 20, "bold"), fg="white", bg="#B71C1C").pack(pady=20)
        
        donor_details_button = tk.Button(self, text="View donor", command=self.view_donor_details_page, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        donor_details_button.pack(pady=20)
        
        donor_update_button = tk.Button(self, text="Update donor", command=self.update_donor_details_page, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        donor_update_button.pack(pady=20)
        
        back_button = tk.Button(self, text="Back", command=self.back, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        back_button.pack(side=tk.BOTTOM, padx=20, pady=20)
        
    def view_donor_details_page(self):
         self.destroy()
         donor_details_page = DonorDetailsPage(self.master,self.username,self.user,self.pswd)
         donor_details_page.pack()
         
    def update_donor_details_page(self):
         self.destroy()
         donor_update_page = UpdateDonorPage(self.master, self.username,self.user,self.pswd)
         donor_update_page.pack()
         
    def back(self):
       self.destroy()
       self.master.home_page = Main_Page.MainPage(self.master,self.user,self.pswd)
       self.master.home_page.pack()
         
         
class DonorDetailsPage(tk.Frame):
    def __init__(self, parent, username,user,pswd):
        super().__init__(parent, bg="#B71C1C")
        self.username=username
        self.user=user
        self.pswd=pswd
        
        self.center_frame = tk.Frame(self, background="#B71C1C",width=800,height=200)
        self.center_frame.pack(pady=10, side='bottom')
        
        tk.Label(self, text="Donor email:", font=("Arial", 14, "bold"), fg="white", bg="#B71C1C").pack(pady=10)
        self.donoremail_entry = tk.Entry(self, font=("Arial", 14))
        self.donoremail_entry.pack(pady=10)
        
        search_button = tk.Button(self, text="Search", command=self.getdonor, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        search_button.pack(pady=20)
        
        clear_filters_button = tk.Button(self, text="Clear", command=self.clearfilters, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        clear_filters_button.pack(pady=20)
        
        updatedonor_button = tk.Button(self, text="Update Donor", command=lambda: [self.destroy(),
        UpdateDonorPage(self.master,username,self.user,self.pswd).pack()], font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        updatedonor_button.pack(pady=20)
        
        home_button = tk.Button(self, text="Home", command=lambda:[self.destroy(),LabTechnicianHomePage(self.master,username,self.user,self.pswd).pack()],font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        home_button.pack(pady=20)
        
        
    def getdonor(self):
        donoremail=self.donoremail_entry.get()
        
        db = mysql.connector.connect(
            host="localhost",
            user=self.user,
            password=self.pswd,
            database="bloodbankdb"
        )
        cursor = db.cursor()
        if len(donoremail)>0:
            cursor.execute("SELECT donor_fname, donor_lname, donor_email, donor_weight, donor_hemoglobin, donor_blood_group FROM donor WHERE donor_email = %s and lab_technician_id=(select lab_technician_id from lab_technician where lab_technician_username=%s)", (donoremail,self.username))
        else:
            cursor.execute("SELECT donor_fname, donor_lname, donor_email, donor_weight, donor_hemoglobin, donor_blood_group FROM donor WHERE lab_technician_id=(select lab_technician_id from lab_technician where lab_technician_username=%s)", (self.username,))
        result = cursor.fetchall()
        columns = ['col0','col1','col2','col4','col5','col6']
        default_headings = ['donor_fname', 'donor_lname', 'donor_email', 'donor_weight', 'donor_hemoglobin', 'donor_blood_group']
        tree = ttk.Treeview(self.center_frame, columns = columns, show = 'headings')
        # Defines the headings
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
        self.donoremail_entry.delete(0, tk.END)
        
        
class UpdateDonorPage(tk.Frame):
    def __init__(self, parent, username,user,pswd):
        super().__init__(parent, bg="#B71C1C")
        self.username=username
        self.user=user
        self.pswd=pswd
        
        tk.Label(self, text="Enter Donor email:", font=("Arial", 14, "bold"), fg="white", bg="#B71C1C").pack(pady=10)
        self.donoremail_entry = tk.Entry(self, font=("Arial", 14))
        self.donoremail_entry.pack(pady=10)
        
        tk.Label(self, text="Enter Blood Group", font=("Arial", 14, "bold"), fg="white", bg="#B71C1C").pack(pady=10)
        self.bloodgroup_entry = tk.Entry(self, font=("Arial", 14))
        self.bloodgroup_entry.pack(pady=10)
        
        
        tk.Label(self, text="Enter Hemoglobin:", font=("Arial", 14, "bold"), fg="white", bg="#B71C1C").pack(pady=10)
        self.hemoglobin_entry = tk.Entry(self, font=("Arial", 14))
        self.hemoglobin_entry.pack(pady=10)
        
        tk.Label(self, text="Enter Weight:", font=("Arial", 14, "bold"), fg="white", bg="#B71C1C").pack(pady=10)
        self.weight_entry = tk.Entry(self, font=("Arial", 14))
        self.weight_entry.pack(pady=10)
        
        
        updatedonor_button = tk.Button(self, text="Update", command=self.updatedonor,font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        updatedonor_button.pack(pady=20)
        
        home_button = tk.Button(self, text="Home", command=lambda:[self.destroy(),LabTechnicianHomePage(self.master,username,self.user,self.pswd).pack()],font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        home_button.pack(pady=20)
        
        
    def updatedonor(self):
        donoremail=self.donoremail_entry.get()
        bloodgroup=self.bloodgroup_entry.get()
        hemoglobin=self.hemoglobin_entry.get()
        weight=self.weight_entry.get()
        
        if weight=='':
            weight=0
        
        db = mysql.connector.connect(
            host="localhost",
            user=self.user,
            password=self.pswd,
            database="bloodbankdb"
        )
        cursor = db.cursor()
        cursor.execute("select * from donor where  donor_email = %s AND lab_technician_id=(select lab_technician_id from lab_technician where lab_technician_username=%s)",(donoremail,self.username))
        result=cursor.fetchone()
        try:
            if result:
                cursor.execute("call update_donor(%s,%s,%s,%s)",(donoremail,weight,hemoglobin,bloodgroup))
                messagebox.showinfo("success", "Updates made successfully!")
                db.commit()
            else:
                messagebox.showerror("showerror", "Please check the donor email. It should be of a donor assigned to you")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            db.close()