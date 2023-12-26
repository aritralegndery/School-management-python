#index.py
# School-management-python
Python_basic_school_managemnet system

 # Login System with CustomTkinter and Image Processing

This project demonstrates how to create a login system using CustomTkinter, a Python library for creating beautiful and customizable user interfaces. The system includes image processing to enhance the visual appeal of the login screen.

## Step-by-Step Explanation

### 1. Importing Necessary Libraries

```python
import customtkinter as tk
from PIL import Image
import json
from hashlib import sha256
import secrets
```

- **CustomTkinter**: This library provides a set of customizable widgets for creating user interfaces.
- **PIL**: Python Imaging Library is used for image processing tasks.
- **json**: This library is used to read and write JSON files.
- **hashlib**: This library provides functions for hashing data.
- **secrets**: This library provides functions for generating secure random numbers.

### 2. Creating the Main Application Window

```python
app = tk.CTk()
app.geometry('800x600')
```

- **CTk()**: This line creates the main application window.
- **geometry()**: This method sets the size of the application window to 800x600 pixels.

### 3. Loading and Displaying the Background Image

```python
bg_img = Image.open('data\images\login\\32271.jpg')
bg = tk.CTkImage(bg_img, size=(600, 700))
lab = tk.CTkLabel(master=app, image=bg, text='')
lab.place(relx=0.2, rely=1, anchor='s')
```

- **Image.open()**: This line loads the background image from the specified path.
- **CTkImage()**: This line creates a CustomTkinter image object from the loaded image.
- **CTkLabel()**: This line creates a label widget to display the background image.
- **place()**: This method positions the label widget at the bottom-right corner of the application window.

### 4. Creating the Login Text Label

```python
Login_text = tk.CTkLabel(master=app, text='Login', font=Font, bg_color='transparent')
Login_text.place(relx=0.7, rely=0.2)
```

- **CTkLabel


#home.py
 # Student Management System

This is a simple student management system with a graphical user interface (GUI) built using the `customtkinter` library. It allows users to search for students and add new students to the system.

## Prerequisites

To run this code, you will need to have the following libraries installed:

* `customtkinter`
* `PIL` (Python Imaging Library)

## Code Overview

The code is structured as follows:

* The `home_2()` function is the main function that creates the GUI and handles the user interactions.
* The `on_c1()` function is called when the "Search Students" button is clicked. It imports the `main()` function from the `data.modules.search` module and calls it.
* The `on_c2()` function is called when the "Add Students" button is clicked. It imports the `formm()` function from the `data.modules.form` module and calls it.
* The `info()` function is called when the "Info" button is clicked. It displays a message box with information about the software.

## Step-by-Step Explanation

Here is a step-by-step explanation of the code:

1. The `home_2()` function creates the main window of the application and sets its title, geometry, and resizable properties.
2. The `search_image` button is created and placed on the window. When this button is clicked, the `on_c1()` function is called.
3. The `on_c1()` function imports the `main()` function from the `data.modules.search` module and calls it. The `main()` function is responsible for searching for students.
4. The `search_image` button is created and placed on the window. When this button is clicked, the `on_c2()` function is called.
5. The `on_c2()` function imports the `formm()` function from the `data.modules.form` module and calls it. The `formm()` function is responsible for adding new students to the system.
6. The `info()` function is created and placed on the window. When this button is clicked, the `info()` function is called.
7. The `info()` function displays a message box with information about the software.

## Running the Code

To run the code, simply open a terminal window and navigate to the
#form.py
 # Student Data Management System

This project is a simple student data management system built using Python and the `customtkinter` library. It allows users to add new students to a database, and view and edit existing student records.

## Prerequisites

To run this project, you will need the following:

* Python 3.6 or later
* `customtkinter` library

## Installation

To install the `customtkinter` library, open a terminal window and run the following command:

```
pip install customtkinter
```

## Usage

To use the student data management system, simply run the `formm.py` file. This will open the main application window, which contains a form for adding new students.

To add a new student, simply enter the student's name, roll number, father's name, mother's name, phone number, date of birth, and birth certificate number into the corresponding fields. Then, click the "Submit" button to save the student's data to the database.

## Database

The student data management system uses a SQLite database to store student records. The database is created automatically when you run the application for the first time.

## Code Explanation

The code for the student data management system is relatively simple and straightforward. Here is a step-by-step explanation of the code:

1. **Import the necessary libraries.**

```python
import customtkinter as tk
from tkinter import messagebox
import sqlite3
```

2. **Define the main application window.**

```python
app = tk.CTk()
app.title("Add A Student")
app.geometry('600x600')
```

3. **Create a form for adding new students.**

```python
entry_frame = tk.CTkFrame(master=app,width=550,height=550)
entry_frame.place(relx=0.5,rely=0.5,anchor="center")

name_entry = tk.CTkEntry(master=entry_frame,text_color='white',placeholder_text='Enter Name',width=200,placeholder_text_color='white',corner_radius=34)
name_entry.place(relx=0.2,rely=0.1,anchor='s')

roll_entry = tk.CTkEntry(master=

```

#search.py
 # Student Database Search Application with SQLite and Tkinter

This is a student database search application built using SQLite and Tkinter. It allows users to search, edit, and delete student records from a local database.

### Step-by-Step Explanation

#### 1. Importing Necessary Modules

```python
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
```

We start by importing the necessary modules for building the GUI and interacting with the SQLite database.

#### 2. Creating the Database Table

```python
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
```

The `create_table()` function establishes a connection to the SQLite database and creates a table named `students` if it doesn't already exist. The table has several columns, including `id`, `name`, `roll`, `father`, `mother`, `phone`, `birth_date`, and `birth_certificate`.

#### 3. Inserting Data into the Database

```python
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
```

The `insert_data()` function takes various student details as arguments and inserts them into the `students` table.

#### 4. Searching for Data in the Database

```python
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

```



```project by aritra```
