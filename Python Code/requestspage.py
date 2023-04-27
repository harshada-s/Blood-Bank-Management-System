
import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector
import adminhome
import tkinter.messagebox as tkMessageBox


class RequestsPage(tk.Frame):
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

        # Fetch requests from database
        cursor = db.cursor()
        cursor.execute("SELECT * FROM request")
        requests = cursor.fetchall()

        # Create a treeview to display requests
        tree_frame = ttk.Frame(self)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.tree = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6), show="headings")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add columns to the treeview
        self.tree.heading(1, text="Request ID")
        self.tree.column(1, width=100)
        self.tree.heading(2, text="Blood Group")
        self.tree.column(2, width=100)
        self.tree.heading(3, text="Amount")
        self.tree.column(3, width=100)
        self.tree.heading(4, text="Status")
        self.tree.column(4, width=100)
        self.tree.heading(5, text="Hospital Name")
        self.tree.column(5, width=200)
        self.tree.heading(6, text="Completed By")
        self.tree.column(6, width=200)

        # Add requests to the treeview
        for request in requests:
            request_id, requested_blood_group, requested_amount, is_open, hospital_name, completed_by_bloodbank = request
            self.tree.insert("", tk.END, values=(request_id, requested_blood_group, requested_amount, is_open, hospital_name, completed_by_bloodbank))

        # Add scrollbar to the treeview
        tree_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.configure(yscrollcommand=tree_scroll.set)

        # Bind a function to the treeview items
        self.tree.bind("<Double-1>", self.edit_request)

        # Create a "Back" button at the bottom left
        back_button = tk.Button(self, text="Back", command=self.back, font=("Arial", 14, "bold"),  bg="#4CAF50", fg="black")
        back_button.pack(side=tk.BOTTOM, padx=20, pady=20)

    def back(self):
        # Destroy the requests page and show the admin home page
        self.destroy()
        self.master.admin_home_page = adminhome.AdminHomePage(self.master,self.user,self.pswd)
        self.master.admin_home_page.pack()

    def edit_request(self, event):
        # Get the selected request ID
        selection = self.tree.selection()
        if not selection:
            print("No request selected")
            return
        request_id = self.tree.item(selection[0])["values"][0]
        print(f"Selected request ID: {request_id}")
    
        # Show the edit request page
        self.destroy()
        self.master.edit_requests_page = EditRequestPage(self.master, request_id,self.user,self.pswd)
        self.master.edit_requests_page.pack()
                
        
        
class EditRequestPage(tk.Frame):
    def __init__(self, parent, request_id,user,pswd):
        super().__init__(parent, bg="#B71C1C")
        self.request_id = request_id
        self.user=user
        self.pswd=pswd

        # Connect to MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user=self.user,
            password=self.pswd,
            database="bloodbankdb"
        )

        # Fetch request from database
        cursor = db.cursor()
        cursor.execute("SELECT * FROM request WHERE request_id = %s", (str(request_id),))
        request = cursor.fetchone()
        # Create form frame
        form_frame = tk.Frame(self, bg="#B71C1C")
        form_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        # Add a "Cancel" button at the bottom left
        
        cancel_button = tk.Button(self, text="Cancel", command=self.cancel, font=("Arial", 14, "bold"), bg="#C62828", fg="black")
        cancel_button.pack(side=tk.BOTTOM, padx=20, pady=20)
        
        # Add a "Save Changes" button at the bottom right
        save_button = tk.Button(self, text="Save Changes", command=self.save_changes, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        save_button.pack(side=tk.BOTTOM, padx=20, pady=20)
    
        request_id_label = tk.Label(form_frame, text="Request ID:", font=("Arial", 14, 'bold'), fg="white", bg="#B71C1C")
        request_id_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.request_id_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.request_id_entry.insert(tk.END, request[0])
        #self.request_id_entry.config(state='disabled')
        self.request_id_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Call the update method to force the screen to redraw all widgets
        self.update()

        # Add a label and input field for the blood group
        blood_group_label = tk.Label(form_frame, text="Blood Group:", font=("Arial", 14, 'bold'), fg="white", bg="#B71C1C")
        blood_group_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.blood_group_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.blood_group_entry.insert(tk.END, request[1])
        #self.blood_group_entry.config(state='disabled')
        self.blood_group_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        
        # Call the update method to force the screen to redraw all widgets
        self.update()


        # Add a label and input field for the requested amount
        amount_label = tk.Label(form_frame, text="Amount:", font=("Arial", 14, 'bold'), fg="white", bg="#B71C1C")
        amount_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.amount_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.amount_entry.insert(tk.END, request[2])
        #self.amount_entry.config(state='disabled')
        self.amount_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        
        # Call the update method to force the screen to redraw all widgets
        self.update()


        # Add a label and input field for the status
        status_label = tk.Label(form_frame, text="Status:", font=("Arial", 14, 'bold'), fg="white",  bg="#B71C1C")
        status_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.status_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.status_entry.insert(tk.END, "Open" if request[3] else "Closed")
        #self.status_entry.config(state='disabled')
        self.status_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        
        # Call the update method to force the screen to redraw all widgets
        self.update()

        
        
        # Add a label and input field for the hospital name
        hospital_name_label = tk.Label(form_frame, text="Hospital Name:", font=("Arial", 14, 'bold'), fg="white", bg="#B71C1C")
        hospital_name_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.hospital_name_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.hospital_name_entry.insert(tk.END, request[4])
        #self.hospital_name_entry.config(state='disabled')
        self.hospital_name_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")
        
        # Call the update method to force the screen to redraw all widgets
        self.update()

        
    
        # Add a label and input field for the completed by bloodbank
        completed_by_label = tk.Label(form_frame, text="Completed By:", font=("Arial", 14,'bold'), fg="white", bg="#B71C1C")
        completed_by_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.completed_by_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.completed_by_entry.insert(tk.END, request[5])
        #self.completed_by_entry.config(state='disabled')
        self.completed_by_entry.grid(row=5, column=1, padx=10, pady=10, sticky="w")

        # Call the update method to force the screen to redraw all widgets
        self.update()
   

    
    def save_changes(self):
        # Get the updated request details from the input fields
        requested_blood_group = self.blood_group_entry.get()
        requested_amount = self.amount_entry.get()
        is_open = True if self.status_entry.get().lower() == "open" else False
        hospital_name = self.hospital_name_entry.get()
        completed_by_bloodbank = self.completed_by_entry.get()
    
        # Connect to the database and update the request
        db = mysql.connector.connect(
            host="localhost",
            user=self.user,
            password=self.pswd,
            database="bloodbankdb"
        )
        cursor = db.cursor()
        cursor.execute("UPDATE request SET requested_blood_group=%s, requested_amount=%s, is_open=%s, hospital_name=%s, completed_by_bloodbank=%s WHERE request_id=%s",
                       (requested_blood_group, requested_amount, is_open, hospital_name, completed_by_bloodbank, self.request_id))
        db.commit()
        db.close()
    
        # Show a success message and go back to the requests page
        tkMessageBox.showinfo("Success", "Request updated successfully!")
        self.cancel()
    
    def cancel(self):
        # Destroy the edit request page and show the requests page
        self.destroy()
        self.master.requests_page = RequestsPage(self.master,self.user,self.pswd)
        self.master.requests_page.pack()
    



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
        self.reqpage = RequestsPage(self,self.user,self.pswd)
        self.reqpage.pack()


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
