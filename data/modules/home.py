def home_2():
    import customtkinter as tk
    from PIL import Image



    app = tk.CTk()
    app.title("Student Management System")
    app.geometry("800x600")
    app.resizable(False,False)


    def on_c1():
        from data.modules.search import main
        main()

    def on_c2():
        from data.modules.form import formm
        formm()



        




    search_image= tk.CTkButton(master=app,text='Search Students',border_color='#242242',command=on_c1)
    search_image.place(relx=0.19,rely=0.3,anchor='center')

    #him = Image.open('E:\\PYTHON\data\images\add-user.png')

    #prep_im = tk.CTkImage(him,size=(60,60))

    search_image= tk.CTkButton(master=app,text='Add Students',border_color='#242242',command=on_c2)
    search_image.place(relx=0.5,rely=0.3,anchor='center')


    def info():
        from tkinter import messagebox
        messagebox.showinfo("Software Info:","Software Version-Beta_2.0,Author:Aritraroy")


  

    search_image= tk.CTkButton(master=app,text='   Info  ',border_color='#242242',command=info)
    search_image.place(relx=0.8,rely=0.3,anchor='center')


    app.mainloop()

   
    