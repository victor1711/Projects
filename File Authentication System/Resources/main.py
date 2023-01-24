from tkinter import *
from PIL import ImageTk, Image
from tkinter import TclError, ttk
from tkinter import messagebox

 
class Login:
    def __init__(self , root) :
        self.root = root
        self.root.title("USER AUTHENTICATION SYSTEM")
        self.root.geometry("1280x720")
        self.root.geometry("900x550+300+130")
        self.root.resizable(False, False)
        
        # Background IMAGE Options
        
        self.bg = ImageTk.PhotoImage(file="img2.png")
        self.bg_image =Label(self.root , image = self.bg).place(x=0 , y = 0, relwidth=1 , relheight=1)


        #Login Details Box
        
        Frame_login =Frame(self.root, bg ="white",highlightbackground="black", highlightthickness=1)
        Frame_login.place(x=220, y = 120 ,width =500 , height=400)
        
        
        #Title & Subtitles
        title = Label(Frame_login, text="Login Here" , font=("Impact" , 35 , "bold"), fg = "#6162FF" , bg = "white").place(x = 90, y = 30)
        subtitle = Label(Frame_login, text="User Login Here" , font=("Goudy old style" , 15 , "bold"), fg = "#1d1d1d" , bg = "white").place(x = 90, y = 100)
        
        #Username
        lbl_user = Label(Frame_login, text="Username" , font=("Goudy old style" , 15 , "bold"), fg = "grey" , bg = "white").place(x = 90, y = 140)
        
        self.username = Entry(Frame_login, font=("Goudy old style" , 15), bg = "#E7E6E6")
        self.username.place(x = 90, y = 170 ,width=320, height=35) 
      
      
        # Password
        lbl_password = Label(Frame_login, text="Password" , font=("Goudy old style" , 15 , "bold"), fg = "grey" , bg = "white").place(x = 90, y = 210)
        
        self.password = Entry(Frame_login, font=("Goudy old style" , 15), bg = "#E7E6E6")
        self.password.place(x = 90, y = 240 ,width=320, height=35) 

        #Forget Button
        
        forget  = Button(Frame_login, text="Forgot Password?" ,bd =0, cursor="hand2", font=("Goudy old style" , 12), fg = "#6162FF" , bg = "white").place(x = 90, y = 290)
        submit  = Button(Frame_login, command = self.check_fun,cursor="hand2", text="Login!" ,bd =0, font=("Goudy old style" , 15), bg = "#6162FF" , fg = "white").place(x = 90, y = 330 ,width=180, height=40) 
        
        
        
        
    def check_fun(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error" , "All  fields are required" , parent = self.root)
            
            
        elif self.username.get() != "Vikram1234" or self.password.get() != "Nda@1234":
            messagebox.showerror("Error" , "Invalid Username or Password" , parent = self.root)

        else:
            messagebox.showinfo("Welcome" , f"Welcome {self.username.get()}" )    


# USERNAME -> "Vikram1234"            
# PASSWORD -> Nda@1234
         

    
root = Tk()
obj = Login(root)
root.mainloop()


    