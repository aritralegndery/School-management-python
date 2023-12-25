def main():


    import tkinter as tk
    from tkinter import ttk
    from tkinter import messagebox
    import sqlite3
    
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

    def search_data(search_text):
        conn = sqlite3.connect('student_data.db')
        cursor = conn.cursor()

        # Search for data based on the search text
        cursor.execute('''
            SELECT * FROM students
            WHERE name LIKE ? OR roll LIKE ? OR father LIKE ? OR mother LIKE ? OR phone LIKE ? OR birth_date LIKE ? OR birth_certificate LIKE ?
        ''', ('%' + search_text + '%', '%' + search_text + '%', '%' + search_text + '%', '%' + search_text + '%', '%' + search_text + '%', '%' + search_text + '%', '%' + search_text + '%'))

        rows = cursor.fetchall()
        conn.close()

        return rows

    def update_display(search_text=""):
        result_tree.delete(*result_tree.get_children())

        rows = search_data(search_text)
        
        for row in rows:
            result_tree.insert('', 'end', values=row)

    def on_search():
        search_text = search_entry.get()
        update_display(search_text)

    def on_edit():
        selected_item = result_tree.selection()

        if not selected_item:
            messagebox.showinfo("Error", "Please select a row to edit.")
            return

        data = result_tree.item(selected_item, 'values')

        # Open a new window for editing
        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Student Data")

        # Entry fields for editing
        name_entry = ttk.Entry(edit_window, width=30)
        name_entry.pack(pady=3)
        roll_entry = ttk.Entry(edit_window, width=30)
        roll_entry.pack(pady=3)
        father_entry = ttk.Entry(edit_window, width=30)
        father_entry.pack(pady=3)
        mothers_entry = ttk.Entry(edit_window, width=30)
        mothers_entry.pack(pady=3)
        phone_entry = ttk.Entry(edit_window, width=30)
        phone_entry.pack(pady=3)
        Birth_entry = ttk.Entry(edit_window, width=30)
        Birth_entry.pack(pady=3)
        bc_entry = ttk.Entry(edit_window, width=30)
        bc_entry.pack(pady=3)

        # Set data from the selected row to entry fields for editing
        name_entry.insert(0, data[1])
        roll_entry.insert(0, data[2])
        father_entry.insert(0, data[3])
        mothers_entry.insert(0, data[4])
        phone_entry.insert(0, data[5])
        Birth_entry.insert(0, data[6])
        bc_entry.insert(0, data[7])

        def save_changes():
            # Get the edited data
            edited_name = name_entry.get()
            edited_roll = roll_entry.get()
            edited_father = father_entry.get()
            edited_mother = mothers_entry.get()
            edited_phone = phone_entry.get()
            edited_birth_date = Birth_entry.get()
            edited_birth_certificate = bc_entry.get()

            conn = sqlite3.connect('student_data.db')
            cursor = conn.cursor()

            # Update the selected row with edited data
            cursor.execute('''
                UPDATE students
                SET name=?, roll=?, father=?, mother=?, phone=?, birth_date=?, birth_certificate=?
                WHERE id=?
            ''', (edited_name, edited_roll, edited_father, edited_mother, edited_phone, edited_birth_date, edited_birth_certificate, data[0]))

            conn.commit()
            conn.close()

            # Update the display after editing
            on_search()

            # Close the edit window
            edit_window.destroy()

        save_button = ttk.Button(edit_window, text="Save Changes", command=save_changes)
        save_button.pack(pady=10)

    def on_delete():
        selected_item = result_tree.selection()

        if not selected_item:
            messagebox.showinfo("Error", "Please select a row to delete.")
            return

        confirmation = messagebox.askokcancel("Confirmation", "Are you sure you want to delete this record?")
        
        if confirmation:
            conn = sqlite3.connect('student_data.db')
            cursor = conn.cursor()

            # Delete the selected row
            cursor.execute('DELETE FROM students WHERE id = ?', (result_tree.item(selected_item, 'values')[0],))

            conn.commit()
            conn.close()

            # Update the display after deletion
            on_search()

    # Create the table on application startup
    create_table()

    root = tk.Tk()
    root.title("Student Database Search")

    # Adding search bar
    search_frame = ttk.Frame(root)
    search_frame.pack(padx=10, pady=10, fill=tk.X)
    style = ttk.Style()
    search_entry = ttk.Entry(search_frame, width=30)
    search_entry.pack(side=tk.LEFT)

    search_button = ttk.Button(search_frame, text="Search", command=on_search)
    search_button.pack(side=tk.LEFT)

    # Adding result tree
    result_tree = ttk.Treeview(root, columns=('ID', 'Name', 'Roll', 'Father', 'Mother', 'Phone', 'Birth Date', 'Birth Certificate'), show='headings')
    result_tree.heading('ID', text='ID')
    result_tree.heading('Name', text='Name')
    result_tree.heading('Roll', text='Roll')
    result_tree.heading('Father', text='Father')
    result_tree.heading('Mother', text='Mother')
    result_tree.heading('Phone', text='Phone')
    result_tree.heading('Birth Date', text='Birth Date')
    result_tree.heading('Birth Certificate', text='Birth Certificate')

    result_tree.pack(padx=8, pady=8, fill=tk.BOTH, expand=True)

    # Update the display with all data initially
    update_display()

    # Adding edit and delete buttons
    edit_button = ttk.Button(root, text="Edit", command=on_edit)
    edit_button.pack(side=tk.LEFT, padx=5)

    delete_button = ttk.Button(root, text="Delete", command=on_delete)
    delete_button.pack(side=tk.LEFT)

    # Run the Tkinter main loop
    root.mainloop()



