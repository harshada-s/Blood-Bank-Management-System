import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector
import adminhome
import tkinter.messagebox as tkMessageBox


class CampsPage(tk.Frame):
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

        # Fetch camps from database
        cursor = db.cursor()
        cursor.execute("SELECT * FROM donationcamp")
        camps = cursor.fetchall()

        # Create a treeview to display camps
        tree_frame = ttk.Frame(self)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.tree = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add columns to the treeview
        self.tree.heading(1, text="Camp ID")
        self.tree.column(1, width=100)
        self.tree.heading(2, text="Street")
        self.tree.column(2, width=100)
        self.tree.heading(3, text="City")
        self.tree.column(3, width=100)
        self.tree.heading(4, text="State")
        self.tree.column(4, width=100)
        self.tree.heading(5, text="Zip Code")
        self.tree.column(5, width=100)
        self.tree.heading(6, text="Camp Date")
        self.tree.column(6, width=100)
        self.tree.heading(7, text="Camp Time")
        self.tree.column(7, width=100)
        self.tree.heading(8, text="Blood Bank Name")
        self.tree.column(8, width=100)

        # Add camps to the treeview
        for camp in camps:
            camp_id, street, city, state, zip_code, camp_date, camp_time, bloodbank_name = camp
            self.tree.insert("", tk.END, values=(camp_id, street, city, state, zip_code, camp_date, camp_time, bloodbank_name))

        # Add scrollbar to the treeview
        tree_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.configure(yscrollcommand=tree_scroll.set)

        # Bind a function to the treeview items
        self.tree.bind("<Double-1>", self.edit_camp)

        # Create a "Back" button at the bottom left
        back_button = tk.Button(self, text="Back", command=self.back, font=("Arial", 14, "bold"),  bg="#4CAF50", fg="black")
        back_button.pack(side=tk.BOTTOM, padx=20, pady=20)
        
        add_button = tk.Button(self, text="Add New Camp", command=self.add_camp, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        add_button.pack(side=tk.BOTTOM, padx=20, pady=20)

    def back(self):
        # Destroy the camps page and show the admin home page
        self.destroy()
        self.master.admin_home_page = adminhome.AdminHomePage(self.master,self.user,self.pswd)
        self.master.admin_home_page.pack()
        
    def add_camp(self):

        self.destroy()
        self.master.edit_camp_page = AddCampPage(self.master,self.user,self.pswd)
        self.master.edit_camp_page.pack()

    def edit_camp(self, event):
        # Get the selected camp ID
        selection = self.tree.selection()
        if not selection:
            print("No camp selected")
            return
        camp_id = self.tree.item(selection[0])["values"][0]
        print(f"Selected camp ID: {camp_id}")
    
        # Show the edit camp page
        self.destroy()
        self.master.edit_camp_page = EditCampPage(self.master, camp_id,self.user,self.pswd)
        self.master.edit_camp_page.pack()
                
        
        
        
        
class EditCampPage(tk.Frame):
    def __init__(self, parent, camp_id,user,pswd):
        super().__init__(parent, bg="#B71C1C")
        self.camp_id = camp_id
        self.user=user
        self.pswd=pswd

        # Connect to MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user=self.user,
            password=self.pswd,
            database="bloodbankdb"
        )

        # Fetch camp from database
        cursor =db.cursor()
        cursor.execute("SELECT * FROM donationcamp WHERE camp_id = %s", (str(camp_id),))
        camp = cursor.fetchone()
        # Create form frame
        form_frame = tk.Frame(self, bg="#B71C1C")
        form_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        # Add a "Cancel" button at the bottom left
        
        cancel_button = tk.Button(self, text="Cancel", command=self.cancel, font=("Arial", 14, "bold"), bg="#C62828", fg="black")
        cancel_button.pack(side=tk.BOTTOM, padx=20, pady=20)
        
        # Add a "Save Changes" button at the bottom right
        save_button = tk.Button(self, text="Save Changes", command=self.save_changes, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        save_button.pack(side=tk.BOTTOM, padx=20, pady=20)
    
        camp_id_label = tk.Label(form_frame, text="Camp ID:", font=("Arial", 14, 'bold'), fg="white", bg="#B71C1C")
        camp_id_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.camp_id_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.camp_id_entry.insert(tk.END, camp[0])
        #self.camp_id_entry.config(state='disabled')
        self.camp_id_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        
        # Call the update method to force the screen to redraw all widgets
        self.update()


        # Add a label and input field for the blood group
        street_label = tk.Label(form_frame, text="Street:", font=("Arial", 14, 'bold'), fg="white", bg="#B71C1C")
        street_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.street_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.street_entry.insert(tk.END, camp[1])
        #self.blood_group_entry.config(state='disabled')
        self.street_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        
        # Call the update method to force the screen to redraw all widgets
        self.update()


        # Add a label and input field for the camped amount
        city_label = tk.Label(form_frame, text="City:", font=("Arial", 14, 'bold'), fg="white", bg="#B71C1C")
        city_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.city_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.city_entry.insert(tk.END, camp[2])
        #self.amount_entry.config(state='disabled')
        self.city_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        
        # Call the update method to force the screen to redraw all widgets
        self.update()


        # Add a label and input field for the status
        state_label = tk.Label(form_frame, text="State:", font=("Arial", 14, 'bold'), fg="white",  bg="#B71C1C")
        state_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.state_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.state_entry.insert(tk.END, camp[3] )
        #self.status_entry.config(state='disabled')
        self.state_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        
        # Call the update method to force the screen to redraw all widgets
        self.update()

        
        
        # Add a label and input field for the hospital name
        zip_label = tk.Label(form_frame, text="Zip Code:", font=("Arial", 14, 'bold'), fg="white", bg="#B71C1C")
        zip_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.zip_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.zip_entry.insert(tk.END, camp[4])
        #self.hospital_name_entry.config(state='disabled')
        self.zip_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        # Call the update method to force the screen to redraw all widgets
        self.update()
        
    
        # Add a label and input field for the completed by bloodbank
        date_label = tk.Label(form_frame, text="Camp Date:", font=("Arial", 14,'bold'), fg="white", bg="#B71C1C")
        date_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.date_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.date_entry.insert(tk.END, camp[5])
        #self.completed_by_entry.config(state='disabled')
        self.date_entry.grid(row=5, column=1, padx=10, pady=10, sticky="w")
        
        # Call the update method to force the screen to redraw all widgets
        self.update()

        # Add a label and input field for the completed by bloodbank
        time_label = tk.Label(form_frame, text="Camp Time:", font=("Arial", 14,'bold'), fg="white", bg="#B71C1C")
        time_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.time_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.time_entry.insert(tk.END, camp[6])
        #self.completed_by_entry.config(state='disabled')
        self.time_entry.grid(row=6, column=1, padx=10, pady=10, sticky="w")
        
        # Call the update method to force the screen to redraw all widgets
        self.update()
        
        
        # Add a label and input field for the completed by bloodbank
        bbname_label = tk.Label(form_frame, text="Blood Bank Name:", font=("Arial", 14,'bold'), fg="white", bg="#B71C1C")
        bbname_label.grid(row=7, column=0, padx=10, pady=10, sticky="w")
        self.bbname_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.bbname_entry.insert(tk.END, camp[7])
        #self.completed_by_entry.config(state='disabled')
        self.bbname_entry.grid(row=7, column=1, padx=10, pady=10, sticky="w")

        # Call the update method to force the screen to redraw all widgets
        self.update()

    
    def save_changes(self):
        # Get the updated camp details from the input fields
        street = self.street_entry.get()
        city = self.city_entry.get()
        state = self.state_entry.get()
        zip_code = self.zip_entry.get()
        camp_date = self.date_entry.get()
        camp_time = self.time_entry.get()
        bloodbank_name = self.bbname_entry.get()
    
        # Connect to the database and update the camp
        db = mysql.connector.connect(
            host="localhost",
            user=self.user,
            password=self.pswd,
            database="bloodbankdb"
        )
        cursor = db.cursor()
        cursor.execute("UPDATE donationcamp SET street=%s, city=%s, state=%s, zip_code=%s, camp_date=%s, camp_time=%s, bloodbank_name=%s WHERE camp_id=%s",
                       (street, city, state, zip_code, camp_date, camp_time, bloodbank_name, self.camp_id))
        db.commit()
        db.close()
    
        # Show a success message and go back to the camps page
        tkMessageBox.showinfo("Success", "Camp updated successfully!")
        self.cancel()
    
    def cancel(self):
        # Destroy the edit camp page and show the camps page
        self.destroy()
        self.master.camp_page = CampsPage(self.master,self.user,self.pswd)
        self.master.camp_page.pack()
  
    
  
class AddCampPage(tk.Frame):
    def __init__(self, parent,user,pswd):
        super().__init__(parent, bg="#B71C1C")
        self.user=user
        self.pswd=pswd

        # Create form frame
        form_frame = tk.Frame(self, bg="#B71C1C")
        form_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        # Add a "Cancel" button at the bottom left
        
        cancel_button = tk.Button(self, text="Cancel", command=self.cancel, font=("Arial", 14, "bold"), bg="#C62828", fg="black")
        cancel_button.pack(side=tk.BOTTOM, padx=20, pady=20)
        
        # Add a "Save Changes" button at the bottom right
        save_button = tk.Button(self, text="Save Changes", command=self.save_changes, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        save_button.pack(side=tk.BOTTOM, padx=20, pady=20)
    

        # Add a label and input field for the blood group
        street_label = tk.Label(form_frame, text="Street:", font=("Arial", 14, 'bold'), fg="white", bg="#B71C1C")
        street_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.street_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.street_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        
        # Call the update method to force the screen to redraw all widgets
        self.update()


        # Add a label and input field for the camped amount
        city_label = tk.Label(form_frame, text="City:", font=("Arial", 14, 'bold'), fg="white", bg="#B71C1C")
        city_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.city_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.city_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        
        # Call the update method to force the screen to redraw all widgets
        self.update()


        # Add a label and input field for the status
        state_label = tk.Label(form_frame, text="State:", font=("Arial", 14, 'bold'), fg="white",  bg="#B71C1C")
        state_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.state_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.state_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        
        # Call the update method to force the screen to redraw all widgets
        self.update()

        
        
        # Add a label and input field for the hospital name
        zip_label = tk.Label(form_frame, text="Zip Code:", font=("Arial", 14, 'bold'), fg="white", bg="#B71C1C")
        zip_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.zip_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.zip_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        # Call the update method to force the screen to redraw all widgets
        self.update()
        
    
        # Add a label and input field for the completed by bloodbank
        date_label = tk.Label(form_frame, text="Camp Date:", font=("Arial", 14,'bold'), fg="white", bg="#B71C1C")
        date_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.date_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.date_entry.grid(row=5, column=1, padx=10, pady=10, sticky="w")
        self.date_entry.insert(0,"YYYY-MM-DD")
        self.date_entry.config(foreground='gray')
        self.date_entry.bind("<FocusIn>", self.clear_entry_date)
        self.date_entry.bind("<FocusOut>", self.set_entry_date)
        # Call the update method to force the screen to redraw all widgets
        self.update()

        # Add a label and input field for the completed by bloodbank
        time_label = tk.Label(form_frame, text="Camp Time:", font=("Arial", 14,'bold'), fg="white", bg="#B71C1C")
        time_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.time_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.time_entry.insert(0,"HH:MM:SS")
        self.time_entry.config(foreground='gray')
        self.time_entry.bind("<FocusIn>", self.clear_entry_time)
        self.time_entry.bind("<FocusOut>", self.set_entry_time)
        self.time_entry.grid(row=6, column=1, padx=10, pady=10, sticky="w")
        
        # Call the update method to force the screen to redraw all widgets
        self.update()
        
        
        # Add a label and input field for the completed by bloodbank
        bbname_label = tk.Label(form_frame, text="Blood Bank Name:", font=("Arial", 14,'bold'), fg="white", bg="#B71C1C")
        bbname_label.grid(row=7, column=0, padx=10, pady=10, sticky="w")
        self.bbname_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.bbname_entry.grid(row=7, column=1, padx=10, pady=10, sticky="w")

        # Call the update method to force the screen to redraw all widgets
        self.update()
        
    def clear_entry_date(self, event):
            if self.date_entry.get() == "YYYY-MM-DD":
                self.date_entry.delete(0, tk.END)
                self.date_entry.config(foreground='black')
                   
    def set_entry_date(self, event):
        if not self.date_entry.get():
            self.date_entry.insert(0, "YYYY-MM-DD")
            
        
    def clear_entry_time(self, event):
            if self.time_entry.get() == "HH:MM:SS":
                  self.time_entry.delete(0, tk.END)
                  self.time_entry.config(foreground='black')
                
    def set_entry_time(self, event):
            if not self.time_entry.get():
                self.time_entry.insert(0, "HH:MM:SS")
            
    def save_changes(self):
        # Get the updated camp details from the input fields
        street = self.street_entry.get()
        city = self.city_entry.get()
        state = self.state_entry.get()
        zip_code = self.zip_entry.get()
        camp_date = self.date_entry.get()
        camp_time = self.time_entry.get()
        bloodbank_name = self.bbname_entry.get()
    
        # Connect to the database and update the camp
        db = mysql.connector.connect(
            host="localhost",
            user=self.user,
            password=self.pswd,
            database="bloodbankdb"
        )
        cursor = db.cursor()
        sql = "INSERT INTO donationcamp (street, city, state, zip_code, camp_date, camp_time, bloodbank_name) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (street, city, state, zip_code, camp_date, camp_time, bloodbank_name))
        db.commit()

        db.commit()
        db.close()
    
        # Show a success message and go back to the camps page
        tkMessageBox.showinfo("Success", "Camp Inserted successfully!")
        self.cancel()
    
    def cancel(self):
        # Destroy the edit camp page and show the camps page
        self.destroy()
        self.master.camp_page = CampsPage(self.master,self.user,self.pswd)
        self.master.camp_page.pack()



#Main class

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Blood Bank Management System")
        window_width = 500
        window_height =600
        self.configure(bg="#B71C1C")
        self.eval('tk::PlaceWindow . center')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # Coordinates of the upper left corner of the window to make the window appear in the center
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        # Create admin home page and show it
        self.reqpage = CampsPage(self,self.user,self.pswd)
        self.reqpage.pack()


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
