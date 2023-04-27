import tkinter as tk
import mysql.connector
import Main_Page
import donorregi
import hospitalregi
import adminregi
import labtecregi


class newUserPage(tk.Frame):
     def __init__(self, parent,user,pswd):
         super().__init__(parent, bg="#B71C1C")
         self.user=user
         self.pswd=pswd
         # Create main label
         tk.Label(self, text="Blood Bank Management System", font=("Arial", 20, "bold"), fg="white", bg="#B71C1C").pack(pady=20)

         # Create buttons
         new_donor_button = tk.Button(self, text="New Donor", command=self.new_donor_page, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
         new_donor_button.pack(pady=20)
         

         new_hospital_button = tk.Button(self, text="New Hospital", command=self.new_hospital_page, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
         new_hospital_button.pack(pady=20)
         
         new_admin_button = tk.Button(self, text="New Admin", command=self.new_admin_page, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
         new_admin_button.pack(pady=20)
         
         new_lab_technician_button = tk.Button(self, text="New Lab Technician", command=self.new_lab_technician_page, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
         new_lab_technician_button.pack(pady=20)       
         
         # Create a "Back" button at the bottom left
         back_button = tk.Button(self, text="Back", command=self.back, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
         back_button.pack(side=tk.BOTTOM, padx=20, pady=20)
     
    
     def back(self):
        self.destroy()
        self.master.home_page = Main_Page.MainPage(self.master,self.user,self.pswd)
        self.master.home_page.pack()
        

     def new_donor_page(self):          
         self.destroy()
         donor_regi_page = donorregi.DonorRegistration(self.master,self.user,self.pswd)
         donor_regi_page.pack()
         
     def new_hospital_page(self):
         self.destroy()
         hospital_regi_page = hospitalregi.HospitalRegistration(self.master,self.user,self.pswd)
         hospital_regi_page.pack()
         
         
     def new_admin_page(self):
         self.destroy()
         hospital_regi_page = adminregi.AdminRegistration(self.master,self.user,self.pswd)
         hospital_regi_page.pack()
         
     def new_lab_technician_page(self):
         self.destroy()
         labtech_regi_page = labtecregi.LTRegistration(self.master,self.user,self.pswd)
         labtech_regi_page.pack()
    
    
class MyApp(tk.Tk):
    
    def __init__(self,user,pswd):
        super().__init__()
        self.user=user
        self.pswd=pswd
        self.title("Blood Bank Management System")
        window_width = 500
        window_height = 600
        self.configure(bg="#B71C1C")
        self.eval('tk::PlaceWindow . center')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = screen_width 
        window_height = screen_height
        # Coordinates of the upper left corner of the window to make the window appear in the center
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        
        # Create admin home page and show it
        newuser_page = newUserPage(self,self.user,self.pswd)
        newuser_page.pack()
        
if __name__ == "__main__":
    app = MyApp()
    app.mainloop()