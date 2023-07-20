import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Function to save the collected information to a file
def save_data():
    name = name_var.get()
    age = age_var.get()
    gender = gender_var.get()
    contact = contact_var.get()
    address = address_var.get()
    travel_history = travel_history_var.get()
    symptoms = symptoms_var.get()

    with open("contact_tracing.txt", "a") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Gender: {gender}\n")
        file.write(f"Contact: {contact}\n")
        file.write(f"Address: {address}\n")
        file.write(f"Travel History: {travel_history}\n")
        file.write(f"Symptoms: {symptoms}\n")
        file.write("\n")
    messagebox.showinfo("Success", "Data saved successfully!")

# Function to search for an entry by name and display the information
def search_data():
    name_to_search = name_var.get()
    found = False
    with open("contact_tracing.txt", "r") as file:
        lines = file.readlines()
        data = ""
        for i in range(len(lines)):
            if lines[i].strip() == f"Name: {name_to_search}":
                found = True
                for j in range(i, i + 7):
                    data += lines[j]
                break

    if found:
        search_result_text.delete("1.0", tk.END)
        search_result_text.insert(tk.END, data)
    else:
        messagebox.showinfo("Not Found", "Entry not found!")

# Create the main app window
app = tk.Tk()
app.title("Contact Tracing App")
app.geometry("600x600")

# Background Image
bg_image = Image.open("backgroundct.png")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(app, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Variables for user information
name_var = tk.StringVar()
age_var = tk.StringVar()
gender_var = tk.StringVar()
contact_var = tk.StringVar()
address_var = tk.StringVar()
travel_history_var = tk.StringVar()
symptoms_var = tk.StringVar()

# User Information Input

# Save Button

# Search Entry

# Search Result

# Run the main loop