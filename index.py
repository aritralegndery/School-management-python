import customtkinter as tk 
from PIL import Image





app=tk.CTk()
app.geometry('800x600')
#image_path = Image.open('E:/PYTHON/bg.jpg')

#app.iconbitmap(image_path)


RED='#FF0000'
LIGHT_BLUE='#1F9791'
Font=("Times New Roman",30,'bold')
app.resizable(False,False)
app.title("Login")

from tkinter import messagebox
#logic of login
class verify:

    def login():
        if Email.get() == "admin" and password.get() == 'aritraroy08':
            from data.modules.home import home_2
            home_2()
            app.destroy()
            
            
        else:

            messagebox.showerror('Error',"Enter Valid Info")
            Email.delete(0,'end')
            password.delete(0,'end')





#Part of illustration Fitting
bg_img =Image.open('data\images\login\\32271.jpg')
bg=tk.CTkImage(bg_img,size=(600,700))
lab= tk.CTkLabel(master=app,image=bg,text='')
lab.place(relx=0.2,rely=1,anchor='s')
#login Part--
Login_text = tk.CTkLabel(master=app,text='     Welcome Back!!',font=Font,bg_color='transparent',text_color='#e024b1')
Login_text.place(relx=0.6,rely=0.2)

Email = tk.CTkEntry(master=app,placeholder_text="Enter Your Username:",
                    placeholder_text_color='white',
                    corner_radius=34,width=300,
                    border_color='#242422',
                    height=48,
                    font=('roboto',19))
Email.place(relx=0.8,rely=0.5,anchor='center')
password = tk.CTkEntry(master=app,placeholder_text="Enter Your password",
                       placeholder_text_color='white',
                       corner_radius=34,
                       width=300,
                       border_color='#242422',
                       height=48,show='*',
                       font=('roboto',19))
password.place(relx=0.8,
               rely=0.6,
               anchor='center')
login_img=Image.open('data/images/login/enter.png')
login_button = tk.CTkButton(master=app,text="Login",image=tk.CTkImage(login_img),corner_radius=92,fg_color=LIGHT_BLUE,hover_color='#29C790',font=('roboto',19),border_color='#242422',command=verify.login)
login_button.place(relx=0.78,rely=0.7,anchor='center')



def stop_bypass():
    x='data2020'
    print('x')

app.mainloop()