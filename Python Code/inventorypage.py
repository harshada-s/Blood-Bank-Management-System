
import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector
import adminhome
import tkinter.messagebox as tkMessageBox


class InventoryPage(tk.Frame):
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
        cursor.execute("SELECT * FROM inventory")
        availability = cursor.fetchall()

        # Create a treeview to display requests
        tree_frame = ttk.Frame(self)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.tree = ttk.Treeview(tree_frame, columns=(1, 2, 3), show="headings")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add columns to the treeview
        self.tree.heading(1, text="Blood Bank Name")
        self.tree.column(1, width=200)
        self.tree.heading(2, text="Blood Group")
        self.tree.column(2, width=100)
        self.tree.heading(3, text="Amount in Liters")
        self.tree.column(3, width=100)


        # Add requests to the treeview
        for available in availability:
            bloodbank_name, bloodgroup_name, amount_litres = available
            self.tree.insert("", tk.END, values=(bloodbank_name, bloodgroup_name, amount_litres))

        # Add scrollbar to the treeview
        tree_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.configure(yscrollcommand=tree_scroll.set)

        # Bind a function to the treeview items
        self.tree.bind("<Double-1>", self.edit_inventory)

        # Create a "Back" button at the bottom left
        back_button = tk.Button(self, text="Back", command=self.back, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        back_button.pack(side=tk.BOTTOM, padx=20, pady=20)

    def back(self):
        # Destroy the requests page and show the admin home page
        self.destroy()
        self.master.admin_home_page = adminhome.AdminHomePage(self.master,self.user,self.pswd)
        self.master.admin_home_page.pack()

    def edit_inventory(self, event):
        # Get the selected request ID
        selection = self.tree.selection()
        if not selection:
            print("No inventory selected")
            return
        bloodbank_name = self.tree.item(selection[0])["values"][0]
        print(f"Selected Blood Bank Name: {bloodbank_name}")
    
        # Show the edit request page
        self.destroy()
        self.master.edit_inventory_page = EditInventoryPage(self.master, bloodbank_name,self.user,self.pswd)
        self.master.edit_inventory_page.pack()
                
        
        
        
class EditInventoryPage(tk.Frame):
    def __init__(self, parent, bloodbank_name,user,pswd):
        super().__init__(parent, bg="#B71C1C")
        self.bloodbank_name = bloodbank_name
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
        cursor.execute("SELECT * FROM inventory WHERE bloodbank_name = %s", (str(bloodbank_name),))
        inventory = cursor.fetchone()
        # Create form frame
        form_frame = tk.Frame(self, bg="#B71C1C")
        form_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        # Add a "Cancel" button at the bottom left
        
        cancel_button = tk.Button(self, text="Cancel", command=self.cancel, font=("Arial", 14, "bold"), bg="#C62828", fg="black")
        cancel_button.pack(side=tk.BOTTOM, padx=20, pady=20)
        
        # Add a "Save Changes" button at the bottom right
        save_button = tk.Button(self, text="Save Changes", command=self.save_changes, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        save_button.pack(side=tk.BOTTOM, padx=20, pady=20)
    
        name_label = tk.Label(form_frame, text="Blood Bank Name:", font=("Arial", 14, 'bold'), fg="white", bg="#B71C1C")
        name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.name_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.name_entry.insert(tk.END, inventory[0])
        #self.request_id_entry.config(state='disabled')
        self.name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Call the update method to force the screen to redraw all widgets
        self.update()

        # Add a label and input field for the blood group
        blood_group_label = tk.Label(form_frame, text="Blood Group:", font=("Arial", 14, 'bold'), fg="white", bg="#B71C1C")
        blood_group_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.blood_group_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.blood_group_entry.insert(tk.END, inventory[1])
        #self.blood_group_entry.config(state='disabled')
        self.blood_group_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        
        # Call the update method to force the screen to redraw all widgets
        self.update()


        # Add a label and input field for the requested amount
        amount_label = tk.Label(form_frame, text="Amount:", font=("Arial", 14, 'bold'), fg="white", bg="#B71C1C")
        amount_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.amount_entry = tk.Entry(form_frame, font=("Arial", 14), fg="black", bg="#FFCDD2")
        self.amount_entry.insert(tk.END, inventory[2])
        #self.amount_entry.config(state='disabled')
        self.amount_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        
        # Call the update method to force the screen to redraw all widgets
        self.update()


    
    def save_changes(self):
        # Get the updated amount in liters from the input field
        amount_litres = self.amount_entry.get()
            
        # Connect to the database and update the amount in liters for the selected blood bank
        db = mysql.connector.connect(
            host="localhost",
            user=self.user,
            password=self.pswd,
            database="bloodbankdb"
        )
        cursor = db.cursor()
        cursor.execute("UPDATE inventory SET amount_litres=%s WHERE bloodbank_name=%s",
                       (amount_litres, self.bloodbank_name))
        db.commit()
        db.close()
    
        # Show a success message and go back to the requests page
        tkMessageBox.showinfo("Success", "Inventory updated successfully!")
        self.cancel()
    
    def cancel(self):
        # Destroy the edit request page and show the requests page
        self.destroy()
        self.master.inventory_page = InventoryPage(self.master,self.user,self.pswd)
        self.master.inventory_page.pack()
    



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
        self.reqpage = InventoryPage(self)
        self.reqpage.pack()


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
