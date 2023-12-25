#Color codes 
RED='#FF0000'
LIGHT_BLUE='#1F9791'
Font=("Times New Roman",20)


import customtkinter as tk 
from PIL import Image
from tkinter import messagebox
import time 


button_image=Image.open('play-button.png')
login_img= Image.open('images/login/login.png')

app=tk.CTk()
app.geometry('800x600')
tk.CTk._windows_set_titlebar_icon('images/icon.ico')

app.resizable(False,False)
app.title('Login Form')
tk.set_appearance_mode('dark')



        

class verify:
    def on_click():
        if Email.get() != "ar" and password.get() != 'Password':
         alert_text.configure(text='Please Enter Valid Information')
         messagebox.showerror('Error',"Enter a Valid password")
        else:
            alert_text.configure(text='Sucess!')
            
            from read import main
            
            main()
        
    
    
    






#ui part.......
Login_text = tk.CTkLabel(master=app,text='Welcome........',font=Font,text_color='white')
Login_text.pack(padx=10,pady=10)

my_image = tk.CTkImage(light_image=Image.open("images/login/login.png"),
                                  dark_image=Image.open("images/login/login.png"),
                                  size=(180, 180))

image_label = tk.CTkLabel(app, image=my_image, text="") 
image_label.pack(padx=30,pady=30) # display image with a CTkLabel


frame_login = tk.CTkFrame(master=app,height=400,width=500,bg_color='transparent')
frame_login.place(relx=0.2,rely=0.9,anchor='w')


Email = tk.CTkEntry(master=frame_login,placeholder_text="Enter Your Email",placeholder_text_color='white',corner_radius=34,width=300)
Email.place(relx=0.5,rely=0.2,anchor='center')

password = tk.CTkEntry(master=frame_login,placeholder_text="Enter Your password",placeholder_text_color='white',corner_radius=34,width=300)
password.place(relx=0.5,rely=0.3,anchor='center')


login_img=Image.open('images/login/enter.png')

login_button = tk.CTkButton(master=frame_login,text="Login",image=tk.CTkImage(login_img),corner_radius=32,fg_color=LIGHT_BLUE,hover_color='#29C790',font=Font,command=verify.on_click)
login_button.place(relx=0.5,rely=0.5,anchor='center')


alert_text=tk.CTkLabel(master=app,text='',text_color='red',font=Font)
alert_text.pack(padx=40,pady=40)



app.mainloop()
