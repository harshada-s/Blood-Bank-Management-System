import tkinter as tk
import requestspage
import appointpage
import campspage
import inventorypage
import Main_Page

class AdminHomePage(tk.Frame):
    def __init__(self, parent,user,pswd):
        super().__init__(parent, bg="#B71C1C")
        self.user=user
        self.pswd=pswd
        # Create welcome label
        tk.Label(self, text="Welcome!", font=("Arial", 20, "bold"), fg="white", bg="#B71C1C").pack(pady=20)

        # Create buttons to view requests, appointments, donation camps, and inventory
        requests_button = tk.Button(self, text="View Requests", font=("Arial", 14, "bold"),bg="#4CAF50", fg="black")
        requests_button.pack(pady=10)
        requests_button.config(command=self.view_requests)

        appointments_button = tk.Button(self, text="View Appointments",font=("Arial", 14, "bold"),bg="#4CAF50", fg="black")
        appointments_button.pack(pady=10)
        appointments_button.config(command=self.view_appointments)

        donation_camps_button = tk.Button(self, text="View Donation Camps",font=("Arial", 14, "bold"),bg="#4CAF50", fg="black")
        donation_camps_button.pack(pady=10)
        donation_camps_button.config(command=self.view_donation_camps)

        inventory_button = tk.Button(self, text="View Inventory",font=("Arial", 14, "bold"),bg="#4CAF50", fg="black")
        inventory_button.pack(pady=10)
        inventory_button.config(command=self.view_inventory)
        
        back_button = tk.Button(self, text="Back", command=self.back, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        back_button.pack(side=tk.BOTTOM, padx=20, pady=20)
        
    def view_requests(self,):
        # Destroy the admin home page and show the requests page
        self.destroy()
        self.master.admin_home_page = requestspage.RequestsPage(self.master,self.user,self.pswd)
        self.master.admin_home_page.pack()

    
    def view_appointments(self):
        
        self.destroy()
        self.master.admin_home_page = appointpage.AppointmentPage(self.master,self.user,self.pswd)
        self.master.admin_home_page.pack()
    
    
    def view_donation_camps(self):
        self.destroy()
        self.master.admin_home_page = campspage.CampsPage(self.master,self.user,self.pswd)
        self.master.admin_home_page.pack()
    
    def view_inventory(self):
        self.destroy()
        self.master.admin_home_page = inventorypage.InventoryPage(self.master,self.user,self.pswd)
        self.master.admin_home_page.pack()
        
    def back(self):
       # Destroy the requests page and show the admin home page
       self.destroy()
       self.master.home_page = Main_Page.MainPage(self.master,self.user,self.pswd)
       self.master.home_page.pack()


class MyApp(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Blood Bank Management System")
        window_width = 500
        window_height = 600
        self.configure(bg="#B71C1C")
        self.eval('tk::PlaceWindow . center')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # Coordinates of the upper left corner of the window to make the window appear in the center
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        
        # Create admin home page and show it
        admin_home_page = AdminHomePage(self,self.user,self.pswd)
        admin_home_page.pack()
        
if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
