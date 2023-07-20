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

# Create the main app window
app = tk.Tk()
app.title("Contact Tracing App")
app.geometry("600x600")

# Background Image

# Variables for user information

# User Information Input

# Save Button

# Search Entry

# Search Result

# Run the main loop