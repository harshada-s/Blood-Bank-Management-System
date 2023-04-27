import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector
import adminhome
import tkinter.messagebox as tkMessageBox


class AppointmentPage(tk.Frame):
    def __init__(self, parent,user,pswd):
        super().__init__(parent, bg="#B71C1C")
        self.user=user
        self.pswd=pswd
        
        # Connect to MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user=self.user,
            password=self.pswd,
            database="bloodbankdb"
        )

        # Fetch appointments from database
        cursor = db.cursor()
        cursor.execute("SELECT * FROM appointment")
        appointments = cursor.fetchall()

        # Create a treeview to display appointments
        tree_frame = ttk.Frame(self)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.tree = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5), show="headings")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add columns to the treeview
        self.tree.heading(1, text="Appointment ID")
        self.tree.column(1, width=100)
        self.tree.heading(2, text="Appointment Date")
        self.tree.column(2, width=100)
        self.tree.heading(3, text="Appointment Time")
        self.tree.column(3, width=100)
        self.tree.heading(4, text="Donor Assigned")
        self.tree.column(4, width=100)
        self.tree.heading(5, text="Camp ID:")
        self.tree.column(5, width=60)

        # Add appointments to the treeview
        for appointment in appointments:
            appointment_id, appointment_date, appointment_time, donor_id, camp_id = appointment
            self.tree.insert("", tk.END, values=(appointment_id, appointment_date, appointment_time, donor_id, camp_id))

        # Add scrollbar to the treeview
        tree_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.configure(yscrollcommand=tree_scroll.set)

        # Bind a function to the treeview items
        self.tree.bind("<Double-1>", self.edit_appointment)

        # Create a "Back" button at the bottom left
        back_button = tk.Button(self, text="Back", command=self.back, font=("Arial", 14, "bold"),  bg="#4CAF50", fg="black")
        back_button.pack(side=tk.BOTTOM, padx=20, pady=20)
        

    def back(self):
        # Destroy the appointments page and show the admin home page
        self.destroy()
        self.master.admin_home_page = adminhome.AdminHomePage(self.master,self.user,self.pswd)
        self.master.admin_home_page.pack()

    def edit_appointment(self, event):
        # Get the selected appointment ID
        selection = self.tree.selection()
        if not selection:
            print("No appointment selected")
            return
        appointment_id = self.tree.item(selection[0])["values"][0]
        print(f"Selected appointment ID: {appointment_id}")
    
        # Show the edit appointment page
        self.destroy()
        self.master.edit_appoint_page = EditAppointPage(self.master, appointment_id,self.user,self.pswd)
        self.master.edit_appoint_page.pack()
                
        
class EditAppointPage(tk.Frame):
    def __init__(self, parent, appointment_id,user,pswd):
        super().__init__(parent, bg="#B71C1C")
        self.appointment_id = appointment_id
        self.user=user
        self.pswd=pswd

        # Connect to MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user=self.user,
            password=self.pswd,
            database="bloodbankdb"
        )

        # Fetch appointment from database
        cursor = db.cursor()
        cursor.execute("SELECT * FROM appointment WHERE appointment_id = %s", (str(appointment_id),))
        appointment = cursor.fetchone()
        # Create form frame
        form_frame = tk.Frame(self, bg="#B71C1C")
        form_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        # Add a "Cancel" button at the bottom left
        
        cancel_button = tk.Button(self, text="Cancel", command=self.cancel, font=("Arial", 14, "bold"), bg="#C62828", fg="black")
        cancel_button.pack(side=tk.BOTTOM, padx=20, pady=20)
        
        # Add a "Save Changes" button at the bottom right
        save_button = tk.Button(self, text="Save Changes", command=self.save_changes, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        save_button.pack(side=tk.BOTTOM, padx=20, pady=20)
    
        appointment_id_label = tk.Label(form_frame, text="Appointment ID:", font=("Arial", 14, 'bold'), fg="white", bg="#B71C1C")
        appointment_id_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.appointment_id_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.appointment_id_entry.insert(tk.END, appointment[0])
        #self.appointment_entry.config(state='disabled')
        self.appointment_id_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")


        # Call the update method to force the screen to redraw all widgets
        self.update()

        # Add a label and input field for the appointment date
        appointment_date_label = tk.Label(form_frame, text="Appointment Date:", font=("Arial", 14, 'bold'), fg="white", bg="#B71C1C")
        appointment_date_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.appointment_date_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.appointment_date_entry.insert(tk.END, appointment[1])
        #self.blood_group_entry.config(state='disabled')
        self.appointment_date_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        
        # Call the update method to force the screen to redraw all widgets
        self.update()


        # Add a label and input field for appointment time
        appointment_time_label = tk.Label(form_frame, text="Appointment Time:", font=("Arial", 14, 'bold'), fg="white", bg="#B71C1C")
        appointment_time_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.appointment_time_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.appointment_time_entry.insert(tk.END, appointment[2])
        #self.amount_entry.config(state='disabled')
        self.appointment_time_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        
        # Call the update method to force the screen to redraw all widgets
        self.update()


        # Add a label and input field for the donor id
        donor_id_label = tk.Label(form_frame, text="Donor ID:", font=("Arial", 14, 'bold'), fg="white",  bg="#B71C1C")
        donor_id_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.donor_id_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.donor_id_entry.insert(tk.END, appointment[3])
        #self.status_entry.config(state='disabled')
        self.donor_id_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        # Call the update method to force the screen to redraw all widgets
        self.update()
        
        
        # Add a label and input field for the camp id
        camp_id_label = tk.Label(form_frame, text="Crime ID:", font=("Arial", 14, 'bold'), fg="white", bg="#B71C1C")
        camp_id_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.camp_id_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.camp_id_entry.insert(tk.END,appointment[4])
        #self.hospital_name_entry.config(state='disabled')
        self.camp_id_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        # Call the update method to force the screen to redraw all widgets
        self.update()
   

    
    def save_changes(self):
        # Get the updated appointment details from the input fields
        appointment_date = self.appointment_date_entry.get()
        appointment_time = self.appointment_time_entry.get()
        donor_id = self.donor_id_entry.get()
        camp_id = self.camp_id_entry.get()
        
    
        # Connect to the database and update the appointment
        db = mysql.connector.connect(
            host="localhost",
            user=self.user,
            password=self.pswd,
            database="bloodbankdb"
        )
        cursor = db.cursor()
        cursor.execute("UPDATE appointment SET  appointment_date=%s, appointment_time=%s, donor_id=%s, camp_id=%s WHERE appointment_id=%s",
                       (appointment_date, appointment_time, donor_id, camp_id, self.appointment_id))
        db.commit()
        #db.close()
    
        # Show a success message and go back to the appointments page
        tkMessageBox.showinfo("Success", "Appointment updated successfully!")
        self.cancel()
    
    def cancel(self):
        # Destroy the edit appointment page and show the appointments page
        self.destroy()
        self.master.appointment_page = AppointmentPage(self.master,self.user,self.pswd)
        self.master.appointment_page.pack()
    



#Main class

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Blood Bank Management System")
        window_width = 500
        window_height =490
        self.configure(bg="#B71C1C")
        self.eval('tk::PlaceWindow . center')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # Coordinates of the upper left corner of the window to make the window appear in the center
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        # Create admin home page and show it
        self.reqpage = AppointmentPage(self,self.user,self.pswd)
        self.reqpage.pack()


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
