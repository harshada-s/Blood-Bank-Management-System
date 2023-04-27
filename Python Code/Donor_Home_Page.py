import tkinter as tk
from tkcalendar import DateEntry
import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Main_Page




class DonorHomePage(tk.Frame):
    def __init__(self, parent, username,user,pswd):
        super().__init__(parent, bg="#B71C1C")
        self.username=username
        self.user=user
        self.pswd=pswd

        tk.Label(self, text="Welcome!", font=("Arial", 20, "bold"), fg="white", bg="#B71C1C").pack(pady=20)
        
        book_appointment_button = tk.Button(self, text="Book an appointment", command=self.donor_book_appointment_page, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        book_appointment_button.pack(pady=20)
        
        view_camps_button = tk.Button(self, text="View Blood Donation Camps", command=self.donor_view_camps_page, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        view_camps_button.pack(pady=20)
        
        view_appointements_button = tk.Button(self, text="View Appointment History", command=self.donor_view_appointments_page, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        view_appointements_button.pack(pady=20)
        
        cancel_appointements_button = tk.Button(self, text="Cancel an appointment", command=self.donor_cancel_appointments_page, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        cancel_appointements_button.pack(pady=20)
        
        
        back_button = tk.Button(self, text="Back", command=self.back, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        back_button.pack(side=tk.BOTTOM, padx=20, pady=20)
        
    def donor_book_appointment_page(self):
        self.destroy()
        book_appointment_page = BookAppointmentPage(self.master, self.username,self.user,self.pswd)
        book_appointment_page.pack()
        
    def donor_view_camps_page(self):
        self.destroy()
        view_camps_page = ViewCampsPage(self.master,self.username,self.user,self.pswd)
        view_camps_page.pack()
        
    def donor_view_appointments_page(self):
        self.destroy()
        view_appointments_page = ViewAppointmentsPage(self.master, self.username,self.user,self.pswd)
        view_appointments_page.pack()
        
    def donor_cancel_appointments_page(self):
        self.destroy()
        cancel_appointments_page = CancelAppointmentsPage(self.master, self.username,self.user,self.pswd)
        cancel_appointments_page.pack()
        
        
    def back(self):
       self.destroy()
       self.master.home_page = Main_Page.MainPage(self.master,self.user,self.pswd)
       self.master.home_page.pack()
    
    
    
class BookAppointmentPage(tk.Frame):
    def __init__(self, parent, username,user,pswd):
        super().__init__(parent, bg="#B71C1C")
        self.username=username
        self.user=user
        self.pswd=pswd

        tk.Label(self, text="Book Appointment", font=("Arial", 20, "bold"), fg="white", bg="#B71C1C").pack(pady=20)
        tk.Label(self, text="Date:", font=("Arial", 14, "bold"), fg="white", bg="#B71C1C").pack(pady=10)
        self.date_entry = DateEntry(self, font=("Arial", 14),date_pattern="yyyy-mm-dd")
        self.date_entry.pack(pady=10)

        self.time_value = tk.StringVar(self)
  
        self.time_value.set("Select Time")
        self.time_list=[]
        self.time_list.append("Select Time")
        
        for t in range(9,20):
            string_time = str(t)+":00:00"
            self.time_list.append(string_time)
        tk.Label(self, text="Time:", font=("Arial", 14,"bold"), fg="white", bg="#B71C1C").pack(pady=10)
        self.time_entry=OptionMenu(self,self.time_value,*(self.time_list))
        self.time_entry.pack(pady=10)
        
        tk.Label(self, text="Donation Camp Name:", font=("Arial", 14,"bold"), fg="white", bg="#B71C1C").pack(pady=10)
        
        self.value_inside = tk.StringVar(self)
  
        self.value_inside.set("Select an Option")
        self.options_list=[]
        self.options_list.append("Select an Option")
        
        self.db = mysql.connector.connect(
            host="localhost",
            user=self.user,
            password=self.pswd,
            database="bloodbankdb"
        )
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT camp_id, street, bloodbank_name FROM donationcamp")
        self.result = self.cursor.fetchall()
        self.db.close()

        for self.r in self.result:
            string_data = [str(data) for data in self.r]
            self.options_list.append(".  ".join(string_data))
            
        self.blood_bank_name_entry=OptionMenu(self,self.value_inside,*(self.options_list))
        self.blood_bank_name_entry.pack(pady=10)
        
        
        book_button = tk.Button(self, text="Book", command=self.bookAppointment, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        book_button.pack(pady=20)
        
        home_button = tk.Button(self, text="Home", command=lambda:[self.destroy(),DonorHomePage(self.master,username,self.user,self.pswd).pack()],font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        home_button.pack(pady=20)
        
        
    def bookAppointment(self):
        date=self.date_entry.get()
        time=self.time_value.get()
        camp_id=self.value_inside.get()
        db = mysql.connector.connect(
            host="localhost",
            user=self.user,
            password=self.pswd,
            database="bloodbankdb"
        )
        try:
            cursor = db.cursor()
            cursor.execute("SELECT donor_id FROM donor WHERE donor_username = %s", (self.username,))
            donor_id = cursor.fetchone()
            cursor.execute("Insert into appointment values(NULL,%s,%s,%s,%s)", (date, time, donor_id[0], camp_id[0]))
            db.commit()
            messagebox.showinfo("success","Appointment Booked successfully")
            self.destroy()
            donor_home_page = DonorHomePage(self.master,self.username,self.user,self.pswd)
            donor_home_page.pack()
        except mysql.connector.Error as e:
            messagebox.showerror("showerror", e.msg)
        finally:
            db.close()
        
        
        
        
class ViewCampsPage(tk.Frame):
    def __init__(self, parent,username,user,pswd):
        super().__init__(parent, bg="#B71C1C")
        self.username=username
        self.user=user
        self.pswd=pswd
       
        self.center_frame = tk.Frame(self, background="#B71C1C",width=800,height=200)
        self.center_frame.pack(pady=10, side='bottom')
        
        tk.Label(self, text="View Blood Donation Camps", font=("Arial", 20, "bold"), fg="white", bg="#B71C1C").pack(pady=20)
        
        tk.Label(self, text="Filter by Date:", font=("Arial", 14, "bold"), fg="white", bg="#B71C1C").pack(pady=10)
        self.date_entry = DateEntry(self, font=("Arial", 14),date_pattern="yyyy-mm-dd")
        self.date_entry.pack(pady=10)
        
        
        tk.Label(self, text="Filter by Blood bank name:", font=("Arial", 14,"bold"), fg="white", bg="#B71C1C").pack(pady=10)
        
        self.value_inside = tk.StringVar(self)
  
        self.value_inside.set("Select an Option")
        self.options_list=[]
        self.options_list.append("Select an Option")
        
        self.db = mysql.connector.connect(
            host="localhost",
            user=self.user,
            password=self.pswd,
            database="bloodbankdb"
        )
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT bloodbank_name FROM bloodbank")
        self.result = self.cursor.fetchall()
        self.db.close()
        
        for self.r in self.result:
            self.options_list.append(self.r[0])
            
        self.blood_bank_name_entry=OptionMenu(self,self.value_inside,*(self.options_list))
        self.blood_bank_name_entry.pack(pady=10)
        
        
        search_button = tk.Button(self, text="Search", command=self.getcamps, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        search_button.pack(pady=20)
        
        clear_filters_button = tk.Button(self, text="Clear", command=self.clearfilters, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        clear_filters_button.pack(pady=20)
        
        book_appointment_button = tk.Button(self, text="Book Appointment", command=lambda:[self.destroy(),BookAppointmentPage(self.master,username,self.user,self.pswd).pack()], font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        book_appointment_button.pack(pady=20)
        
        home_button = tk.Button(self, text="Home", command=lambda:[self.destroy(),DonorHomePage(self.master,username,self.user,self.pswd).pack()],font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        home_button.pack(pady=20)
        

    def getcamps(self):
        
        date=self.date_entry.get()
        bloodbankname=self.value_inside.get()
        
        db = mysql.connector.connect(
            host="localhost",
            user=self.user,
            password=self.pswd,
            database="bloodbankdb"
        )
        cursor = db.cursor()
        if len(date)>0:
            cursor.execute("call get_camps(%s,%s,%s)",(self.username,date,bloodbankname))
            
        else:
            cursor.execute("call get_camps(%s,NULL,%s)",(self.username,bloodbankname))
        result = cursor.fetchall()
        db.close()
        
        
        columns = ['col0','col1','col2','col4','col5','col6','col7','col8']
        default_headings = ['camp_id', 'street', 'city','state','zip_code','camp_date','camp_time','bloodbank_name']
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
        
        
        
    def clearfilters(self):
        self.date_entry.delete(0, END)
        self.value_inside.set("Select an Option")
        
        
        
        
class ViewAppointmentsPage(tk.Frame):
    def __init__(self, parent, username,user,pswd):
        super().__init__(parent, bg="#B71C1C")
        self.username=username
        self.user=user
        self.pswd=pswd
       
        self.center_frame = tk.Frame(self, background="#B71C1C",width=800,height=200)
        self.center_frame.pack(pady=10, side='bottom')
        
        tk.Label(self, text="View Appointment History", font=("Arial", 20, "bold"), fg="white", bg="#B71C1C").pack(pady=20)
        
        tk.Label(self, text="Filter by Date:", font=("Arial", 14, "bold"), fg="white", bg="#B71C1C").pack(pady=10)
        self.date_entry = DateEntry(self, font=("Arial", 14),date_pattern="yyyy-mm-dd")
        self.date_entry.pack(pady=10)
        
        
        tk.Label(self, text="Filter by Blood bank name:", font=("Arial", 14,"bold"), fg="white", bg="#B71C1C").pack(pady=10)
        
        self.value_inside = tk.StringVar(self)
  
        self.value_inside.set("Select an Option")
        self.options_list=[]
        self.options_list.append("Select an Option")
        
        self.db = mysql.connector.connect(
            host="localhost",
            user=self.user,
            password=self.pswd,
            database="bloodbankdb"
        )
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT bloodbank_name FROM bloodbank")
        self.result = self.cursor.fetchall()
        self.db.close()

        for self.r in self.result:
            self.options_list.append(self.r[0])
            
        self.blood_bank_name_entry=OptionMenu(self,self.value_inside,*(self.options_list))
        self.blood_bank_name_entry.pack(pady=10)
        
        
        search_button = tk.Button(self, text="Search", command=self.getappointments, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        search_button.pack(pady=20)
        
        clear_filters_button = tk.Button(self, text="Clear", command=self.clearfilters, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        clear_filters_button.pack(pady=20)
        
        home_button = tk.Button(self, text="Home", command=lambda:[self.destroy(),DonorHomePage(self.master,username,self.user,self.pswd).pack()],font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        home_button.pack(pady=20)

    def getappointments(self):
        
        date=self.date_entry.get()
        bloodbankname=self.value_inside.get()
        
        db = mysql.connector.connect(
            host="localhost",
            user=self.user,
            password=self.pswd,
            database="bloodbankdb"
        )
        cursor =db.cursor()
        if len(date)>0:
            cursor.execute("call get_appointments(%s,%s,%s)",(self.username,date,bloodbankname))
            
        else:
            cursor.execute("call get_appointments(%s,NULL,%s)",(self.username,bloodbankname))
        result = cursor.fetchall()
        db.close()
        
        
        columns = ['col0','col1','col2','col4','col5','col6','col7']
        default_headings = ['appointment_id', 'appointment_date', 'appointment_time','donor_id','donation_camp_id','donation_camp_street','bloodbank_name']
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
        
        
    def clearfilters(self):
        self.date_entry.delete(0, tk.END)
        self.value_inside.set("Select an Option")
        
        
        
class CancelAppointmentsPage(tk.Frame):
    def __init__(self, parent, username,user,pswd):
        super().__init__(parent, bg="#B71C1C")
        self.username=username
        self.user=user
        self.pswd=pswd
        
        tk.Label(self, text="Cancel Appointment", font=("Arial", 20, "bold"), fg="white", bg="#B71C1C").pack(pady=20)
        tk.Label(self, text="Select Date:", font=("Arial", 14, "bold"), fg="white", bg="#B71C1C").pack(pady=10)
        self.date_entry = DateEntry(self, font=("Arial", 14),date_pattern="yyyy-mm-dd")
        self.date_entry.pack(pady=10)

        self.time_value = tk.StringVar(self)
  
        self.time_value.set("Select Time")
        self.time_list=[]
        self.time_list.append("Select Time")
        
        for t in range(9,20):
            string_time = str(t)+":00:00"
            self.time_list.append(string_time)
        tk.Label(self, text="Select Time:", font=("Arial", 14,"bold"), fg="white", bg="#B71C1C").pack(pady=10)
        self.time_entry=OptionMenu(self,self.time_value,*(self.time_list))
        self.time_entry.pack(pady=10)
        
        tk.Label(self, text="Select Donation Camp Name:", font=("Arial", 14,"bold"), fg="white", bg="#B71C1C").pack(pady=10)
        
        self.value_inside = tk.StringVar(self)
  
        self.value_inside.set("Select an Option")
        self.options_list=[]
        self.options_list.append("Select an Option")
        
        self.db = mysql.connector.connect(
            host="localhost",
            user=self.user,
            password=self.pswd,
            database="bloodbankdb"
        )
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT camp_id, street, bloodbank_name FROM donationcamp")
        self.result = self.cursor.fetchall()
        self.db.close()

        for self.r in self.result:
            string_data = [str(data) for data in self.r]
            self.options_list.append(".  ".join(string_data))
            
        self.blood_bank_name_entry=OptionMenu(self,self.value_inside,*(self.options_list))
        self.blood_bank_name_entry.pack(pady=10)
        
        
        book_button = tk.Button(self, text="Cancel Appointment", command=self.deleteAppointment, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        book_button.pack(pady=20)
        
        home_button = tk.Button(self, text="Home", command=lambda:[self.destroy(),DonorHomePage(self.master,username,self.user,self.pswd).pack()],font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        home_button.pack(pady=20)
       
        
    def deleteAppointment(self):
        date=self.date_entry.get()
        time=self.time_value.get()
        camp_id=self.value_inside.get()
        db = mysql.connector.connect(
            host="localhost",
            user=self.user,
            password=self.pswd,
            database="bloodbankdb"
        )
        cursor = db.cursor()
        cursor.execute("SELECT donor_id FROM donor WHERE donor_username = %s", (self.username,))
        donor_id = cursor.fetchone()
        try:
            cursor.execute("SELECT * from appointment where donor_id=%s and appointment_date=%s and appointment_time=%s and camp_id=%s", (donor_id[0], date, time, camp_id[0]))
            result=cursor.fetchall()
            if result:
                cursor.execute("DELETE from appointment where donor_id=%s and appointment_date=%s and appointment_time=%s and camp_id=%s", (donor_id[0], date, time, camp_id[0]))
                db.commit()
                messagebox.showinfo("success","Appointment canceled successfully")
                self.destroy()
                donor_home_page = DonorHomePage(self.master,self.username,self.user,self.pswd)
                donor_home_page.pack()
            else:
                messagebox.showerror("showerror", "Could not cancel the appointment. Please check all the details")
        except mysql.connector.Error as e:
            messagebox.showerror("showerror", "Could not cancel the appointment")
        finally:
            db.close()
            
        
        