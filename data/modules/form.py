def formm():

    import customtkinter as tk
    from tkinter import messagebox
    import sqlite3

    Font = ('Times New Roman',20)
    father = ''' Father's name'''
    mother = ''' Mothers's name'''

    app = tk.CTk()
    app.title("Add A Student")
    app.geometry('600x600')

    txt_label=tk.CTkLabel(master=app,text='',text_color='white',font=('Times New Roman',20))
    txt_label.pack()
    scroll = tk.CTkScrollableFrame(master=app,width=550,height=550)
    scroll.place(relx=0.5,rely=0.5,anchor="center")

    entry_frame = tk.CTkFrame(master=app,width=550,height=550)
    entry_frame.place(relx=0.5,rely=0.5,anchor="center")

    name_entry = tk.CTkEntry(master=entry_frame,text_color='white',placeholder_text='Enter Name',width=200,placeholder_text_color='white',corner_radius=34)
    name_entry.place(relx=0.2,rely=0.1,anchor='s')


    roll_entry = tk.CTkEntry(master=entry_frame,text_color='white',placeholder_text='Roll',width=200,placeholder_text_color='white',corner_radius=34)
    roll_entry.place(relx=0.6,rely=0.1,anchor='s')


    father_entry = tk.CTkEntry(master=entry_frame,text_color='white',placeholder_text=father,width=200,placeholder_text_color='white',corner_radius=34)
    father_entry.place(relx=0.2,rely=0.2,anchor='s')

    mothers_entry = tk.CTkEntry(master=entry_frame,text_color='white',placeholder_text=mother,width=200,placeholder_text_color='white',corner_radius=34)
    mothers_entry.place(relx=0.6,rely=0.2,anchor='s')


    phone_entry = tk.CTkEntry(master=entry_frame,text_color='white',placeholder_text='Phone No.',width=200,placeholder_text_color='white',corner_radius=34)
    phone_entry.place(relx=0.2,rely=0.3,anchor='s')

    Birth_entry = tk.CTkEntry(master=entry_frame,text_color='white',placeholder_text="Date Of Birth",width=200,placeholder_text_color='white',corner_radius=34)
    Birth_entry.place(relx=0.6,rely=0.3,anchor='s')


    bc_entry = tk.CTkEntry(master=entry_frame,text_color='white',placeholder_text='Birth Certificate Number',width=200,placeholder_text_color='white',corner_radius=34)
    bc_entry.place(relx=0.2,rely=0.4,anchor='s')



    def create_table():
        conn = sqlite3.connect('student_data.db')
        cursor = conn.cursor()
        
        # Create a table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                roll TEXT NOT NULL,
                father TEXT,
                mother TEXT,
                phone TEXT,
                birth_date TEXT,
                birth_certificate TEXT
            )
        ''')
        
        conn.commit()
        conn.close()

    def insert_data(name, roll, father, mother, phone, birth_date, birth_certificate):
        conn = sqlite3.connect('student_data.db')
        cursor = conn.cursor()

        # Insert data into the table
        cursor.execute('''
            INSERT INTO students (name, roll, father, mother, phone, birth_date, birth_certificate)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, roll, father, mother, phone, birth_date, birth_certificate))

        conn.commit()
        conn.close()



    def on_submit():
        # Get data from entry fields
        name = name_entry.get()
        roll = roll_entry.get()
        father = father_entry.get()
        mother = mothers_entry.get()
        phone = phone_entry.get()
        birth_date = Birth_entry.get()
        birth_certificate = bc_entry.get()

        # Insert data into the database
        insert_data(name, roll, father, mother, phone, birth_date, birth_certificate)
        messagebox.showinfo("Sucees",f'{name} Has been Added')
        name_entry.delete(0,'end')
        roll_entry.delete(0,'end')
        father_entry.delete(0,'end')
        mothers_entry.delete(0,'end')
        phone_entry.delete(0,'end')
        Birth_entry.delete(0,'end')
        bc_entry.delete(0,'end')



        

    # Create the table on application startup
    create_table()





    submit_btn=tk.CTkButton(master=entry_frame,text='submit',fg_color='green',command=on_submit)
    submit_btn.place(relx=0.5,rely=0.5,anchor='center')
    app.mainloop()