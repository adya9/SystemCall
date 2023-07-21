# import tkinter as tk
# from tkinter import filedialog
# import shutil
# import os

# selected_file = ""

# def create_file():
#     file_path = filedialog.asksaveasfilename()
#     if file_path:
#         try:
#             with open(file_path, 'w'):
#                 pass
#             status_label.config(text="File created successfully!")
#         except Exception as e:
#             status_label.config(text=f"Error: {e}")

# def move_file():
#     global selected_file
#     source_path = filedialog.askopenfilename()
#     if source_path:
#         selected_file = source_path
#         status_label.config(text="Select destination to move the file.")

# def copy_file():
#     global selected_file
#     source_path = filedialog.askopenfilename()
#     if source_path:
#         selected_file = source_path
#         status_label.config(text="Select destination to copy the file.")

# def paste_file():
#     global selected_file
#     destination_path = filedialog.askdirectory()
#     if selected_file and destination_path:
#         try:
#             shutil.copy2(selected_file, os.path.join(destination_path, os.path.basename(selected_file)))
#             status_label.config(text="File pasted successfully!")
#         except Exception as e:
#             status_label.config(text=f"Error: {e}")

# def delete_file():
#     file_path = filedialog.askopenfilename()
#     if file_path:
#         try:
#             os.remove(file_path)
#             status_label.config(text="File deleted successfully!")
#         except Exception as e:
#             status_label.config(text=f"Error: {e}")

# def rename_file():
#     global selected_file
#     new_name = filedialog.asksaveasfilename()
#     if selected_file and new_name:
#         try:
#             shutil.move(selected_file, new_name)
#             status_label.config(text="File renamed successfully!")
#         except Exception as e:
#             status_label.config(text=f"Error: {e}")

# def cut_file():
#     global selected_file
#     source_path = filedialog.askopenfilename()
#     if source_path:
#         selected_file = source_path
#         status_label.config(text="Select destination to cut the file.")

# # GUI setup
# root = tk.Tk()
# root.title("File Operations")

# # Welcome label with green color
# welcome_label = tk.Label(root, text="Welcome", font=("Arial", 18, "bold"), fg="green")
# welcome_label.grid(row=0, column=0, columnspan=3, padx=30, pady=30)

# # Increase button size
# button_width = 20
# button_height = 2

# create_button = tk.Button(root, text="CREATE", width=button_width, height=button_height, command=create_file)
# create_button.grid(row=1, column=0, padx=30, pady=10)

# move_button = tk.Button(root, text="MOVE", width=button_width, height=button_height, command=move_file)
# move_button.grid(row=1, column=1, padx=10, pady=10)

# copy_button = tk.Button(root, text="COPY", width=button_width, height=button_height, command=copy_file)
# copy_button.grid(row=1, column=2, padx=10, pady=10)

# paste_button = tk.Button(root, text="PASTE", width=button_width, height=button_height, command=paste_file)
# paste_button.grid(row=2, column=0, padx=30, pady=10)

# delete_button = tk.Button(root, text="DELETE", width=button_width, height=button_height, command=delete_file)
# delete_button.grid(row=2, column=1, padx=10, pady=10)

# rename_button = tk.Button(root, text="RENAME", width=button_width, height=button_height, command=rename_file)
# rename_button.grid(row=2, column=2, padx=10, pady=10)

# cut_button = tk.Button(root, text="CUT", width=button_width, height=button_height, command=cut_file)
# cut_button.grid(row=3, column=0, padx=30, pady=10)

# status_label = tk.Label(root, text="", width=button_width*3, height=3, font=("Arial", 14, "bold"), fg="green")
# status_label.grid(row=4, column=0, columnspan=3, padx=30, pady=30)

# root.mainloop()

# import tkinter as tk
# from tkinter import filedialog
# import shutil
# import os
# import subprocess

# selected_file = ""

# def create_file():
#     file_path = filedialog.asksaveasfilename()
#     if file_path:
#         try:
#             with open(file_path, 'w'):
#                 pass
#             status_label.config(text="File created successfully!")
#         except Exception as e:
#             status_label.config(text=f"Error: {e}")

# def open_file():
#     global selected_file
#     file_path = filedialog.askopenfilename()
#     if file_path:
#         selected_file = file_path
#         if os.name == 'nt':  # Windows
#             os.startfile(selected_file)
#         elif os.name == 'posix':  # macOS and Linux
#             subprocess.run(['xdg-open', selected_file])
#         else:
#             status_label.config(text="Error: Opening file is not supported on this platform.")

# def copy_file():
#     global selected_file
#     file_path = filedialog.askopenfilename()
#     if file_path:
#         selected_file = file_path
#         status_label.config(text="File copied successfully!")

# def paste_file():
#     global selected_file
#     destination_path = filedialog.askdirectory()
#     if selected_file and destination_path:
#         try:
#             shutil.copy2(selected_file, os.path.join(destination_path, os.path.basename(selected_file)))
#             status_label.config(text="File pasted successfully!")
#         except Exception as e:
#             status_label.config(text=f"Error: {e}")

# def delete_file():
#     file_path = filedialog.askopenfilename()
#     if file_path:
#         try:
#             os.remove(file_path)
#             status_label.config(text="File deleted successfully!")
#         except Exception as e:
#             status_label.config(text=f"Error: {e}")

# def rename_file():
#     global selected_file
#     new_name = filedialog.asksaveasfilename()
#     if selected_file and new_name:
#         try:
#             shutil.move(selected_file, new_name)
#             status_label.config(text="File renamed successfully!")
#         except Exception as e:
#             status_label.config(text=f"Error: {e}")

# def cut_file():
#     global selected_file
#     file_path = filedialog.askopenfilename()
#     if file_path:
#         selected_file = file_path
#         status_label.config(text="File cut successfully!")

# # GUI setup
# root = tk.Tk()
# root.title("File Operations")

# # Welcome label with green color
# welcome_label = tk.Label(root, text="Welcome", font=("Arial", 18, "bold"), fg="green")
# welcome_label.grid(row=0, column=0, columnspan=2, padx=30, pady=30)

# # Increase button size
# button_width = 20
# button_height = 2

# create_button = tk.Button(root, text="CREATE", width=button_width, height=button_height, command=create_file)
# create_button.grid(row=1, column=0, padx=30, pady=10)

# open_button = tk.Button(root, text="OPEN", width=button_width, height=button_height, command=open_file)
# open_button.grid(row=1, column=1, padx=10, pady=10)

# copy_button = tk.Button(root, text="COPY", width=button_width, height=button_height, command=copy_file)
# copy_button.grid(row=2, column=0, padx=30, pady=10)

# paste_button = tk.Button(root, text="PASTE", width=button_width, height=button_height, command=paste_file)
# paste_button.grid(row=2, column=1, padx=10, pady=10)

# delete_button = tk.Button(root, text="DELETE", width=button_width, height=button_height, command=delete_file)
# delete_button.grid(row=3, column=0, padx=30, pady=10)

# rename_button = tk.Button(root, text="RENAME", width=button_width, height=button_height, command=rename_file)
# rename_button.grid(row=3, column=1, padx=10, pady=10)

# cut_button = tk.Button(root, text="CUT", width=button_width, height=button_height, command=cut_file)
# cut_button.grid(row=4, column=0, padx=30, pady=10)

# status_label = tk.Label(root, text="", width=button_width*2, height=3, font=("Arial", 14, "bold"), fg="green")
# status_label.grid(row=5, column=0, columnspan=2, padx=30, pady=30)

# root.mainloop()

import tkinter as tk
from tkinter import filedialog
import os
import subprocess

selected_file = ""

def create_file():
    file_path = filedialog.asksaveasfilename()
    if file_path:
        try:
            with open(file_path, 'w'):
                pass
            status_label.config(text="File created successfully!")
        except Exception as e:
            status_label.config(text=f"Error: {e}")

def open_file():
    global selected_file
    file_path = filedialog.askopenfilename()
    if file_path:
        selected_file = file_path
        if os.name == 'nt':  # Windows
            os.startfile(selected_file)
        elif os.name == 'posix':  # macOS and Linux
            subprocess.run(['xdg-open', selected_file])
        else:
            status_label.config(text="Error: Opening file is not supported on this platform.")

def copy_file():
    global selected_file
    file_path = filedialog.askopenfilename()
    if file_path:
        selected_file = file_path
        status_label.config(text="File copied successfully!")

def paste_file():
    global selected_file
    destination_path = filedialog.askdirectory()
    if selected_file and destination_path:
        try:
            shutil.copy2(selected_file, os.path.join(destination_path, os.path.basename(selected_file)))
            status_label.config(text="File pasted successfully!")
        except Exception as e:
            status_label.config(text=f"Error: {e}")

def delete_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            os.remove(file_path)
            status_label.config(text="File deleted successfully!")
        except Exception as e:
            status_label.config(text=f"Error: {e}")

def rename_file():
    global selected_file
    new_name = filedialog.asksaveasfilename()
    if selected_file and new_name:
        try:
            os.rename(selected_file, new_name)
            selected_file = new_name
            status_label.config(text="File renamed successfully!")
        except Exception as e:
            status_label.config(text=f"Error: {e}")

def cut_file():
    global selected_file
    file_path = filedialog.askopenfilename()
    if file_path:
        selected_file = file_path
        status_label.config(text="File cut successfully!")

# GUI setup
root = tk.Tk()
root.title("File Operations")

# Welcome label with green color
welcome_label = tk.Label(root, text="Welcome", font=("Arial", 18, "bold"), fg="green")
welcome_label.grid(row=0, column=0, columnspan=2, padx=30, pady=30)

# Increase button size
button_width = 20
button_height = 2

create_button = tk.Button(root, text="CREATE", width=button_width, height=button_height, command=create_file)
create_button.grid(row=1, column=0, padx=30, pady=10)

open_button = tk.Button(root, text="OPEN", width=button_width, height=button_height, command=open_file)
open_button.grid(row=1, column=1, padx=10, pady=10)

copy_button = tk.Button(root, text="COPY", width=button_width, height=button_height, command=copy_file)
copy_button.grid(row=2, column=0, padx=30, pady=10)

paste_button = tk.Button(root, text="PASTE", width=button_width, height=button_height, command=paste_file)
paste_button.grid(row=2, column=1, padx=10, pady=10)

delete_button = tk.Button(root, text="DELETE", width=button_width, height=button_height, command=delete_file)
delete_button.grid(row=3, column=0, padx=30, pady=10)

rename_button = tk.Button(root, text="RENAME", width=button_width, height=button_height, command=rename_file)
rename_button.grid(row=3, column=1, padx=10, pady=10)

cut_button = tk.Button(root, text="CUT", width=button_width, height=button_height, command=cut_file)
cut_button.grid(row=4, column=0, padx=30, pady=10)

status_label = tk.Label(root, text="", width=button_width*2, height=3, font=("Arial", 14, "bold"), fg="green")
status_label.grid(row=5, column=0, columnspan=2, padx=30, pady=30)

root.mainloop()
