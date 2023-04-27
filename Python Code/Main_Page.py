import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter import messagebox
import Donor_Home_Page
import Lab_Technician_Home_Page
import Hospital_Home_Page
import userpage
import adminhome


# Please change the 'user' and 'pswd' fields below as per the username and password of your database (MySQL Workbench)
user="root"
pswd="password@123"



class LoginPage(tk.Frame):
    def __init__(self, parent, on_login,user,pswd):
        super().__init__(parent, bg="#B71C1C")
        self.on_login = on_login
        self.user=user
        self.pswd=pswd

        tk.Label(self, text="Login Page", font=("Arial", 20, "bold"), fg="white", bg="#B71C1C").pack(pady=20)

        tk.Label(self, text="Username:", font=("Arial", 14, "bold"), fg="white", bg="#B71C1C").pack(pady=10)
        self.username_entry = tk.Entry(self, font=("Arial", 14))
        self.username_entry.pack(pady=10)


        tk.Label(self, text="Password:", font=("Arial", 14,"bold"), fg="white", bg="#B71C1C").pack(pady=10)
        self.password_entry = tk.Entry(self, show="*", font=("Arial", 14))
        self.password_entry.pack(pady=10)
        self.password_entry.focus_set()
        
        
        self.username_entry.bind("<Return>", lambda event: self.login())


        login_button = tk.Button(self, text="Login", command=self.login, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        login_button.pack(pady=20)
        
        back_button = tk.Button(self, text="Back", command=self.back, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        back_button.pack(side=tk.BOTTOM, padx=20, pady=20)
        
        
        self.after(1, lambda: self.username_entry.focus_set())
        
    

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.on_login(username, password)=='donor':
            self.destroy()
            donor_home_page = Donor_Home_Page.DonorHomePage(self.master,username,self.user,self.pswd)
            donor_home_page.pack()
        elif self.on_login(username, password)=='lab_technician':
            self.destroy()
            lab_technician_home_page = Lab_Technician_Home_Page.LabTechnicianHomePage(self.master, username,self.user,self.pswd)
            lab_technician_home_page.pack()
        elif self.on_login(username, password)=='hospital':
            self.destroy()
            hospital_home_page = Hospital_Home_Page.HospitalHomePage(self.master, username,self.user,self.pswd)
            hospital_home_page.pack()
        elif self.on_login(username, password)=='admin':
            self.destroy()
            admin_home_page = adminhome.AdminHomePage(self.master,self.user,self.pswd)
            admin_home_page.pack()
        else:
            messagebox.showerror("showerror", "Please check if the username and password is correct")
            self.password_entry.delete(0, tk.END)

    def back(self):
       self.destroy()
       self.master.home_page = MainPage(self.master,self.user,self.pswd)
       self.master.home_page.pack()



class MainPage(tk.Frame):
    def __init__(self, parent,user,pswd):
        super().__init__(parent, bg="#B71C1C")
        self.user=user
        self.pswd=pswd

        tk.Label(self, text="Blood Bank Management System", font=("Arial", 20, "bold"), fg="white", bg="#B71C1C").pack(pady=20)

        new_user_button = tk.Button(self, text="New User", command=self.new_user_page, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        new_user_button.pack(pady=20)

        existing_user_button = tk.Button(self, text="Existing User", command=self.existing_user_page, font=("Arial", 14, "bold"), bg="#4CAF50", fg="black")
        existing_user_button.pack(pady=20)
        

    def new_user_page(self):
        self.destroy()
        newuser_page = userpage.newUserPage(self.master,self.user,self.pswd)
        newuser_page.pack()

    def existing_user_page(self):
        self.destroy()
        login_page = LoginPage(self.master, self.handle_login,self.user,self.pswd)
        login_page.pack()


    def handle_login(self, username, password):
        # Check username and password against MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user=self.user,
            password=self.pswd,
            database="bloodbankdb"
        )
        cursor = db.cursor()
        cursor.execute("select login(%s,%s)",(username,password))
        result = cursor.fetchone()
        return result[0]
        cursor.close()
        db.close()
        



class MyApp(tk.Tk):

    def __init__(self,user,pswd):
        super().__init__()
        
        self.user=user
        self.pswd=pswd
        self.title("Blood Bank Management System")
        self.configure(bg="#B71C1C")
        self.eval('tk::PlaceWindow . center')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = screen_width
        window_height = screen_height
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.resizable(False, False)
       
        #self.resizable(False, False)
        main_page = MainPage(self,user,pswd)
        main_page.pack()

if __name__ == "__main__":

    app = MyApp(user,pswd)
    app.mainloop()