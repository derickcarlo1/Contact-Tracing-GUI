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
name_label = tk.Label(app, text="Name:")
name_label.pack()
name_entry = tk.Entry(app, textvariable=name_var)
name_entry.pack()

name_label = tk.Label(app, text="Name:")
name_label.pack()
name_entry = tk.Entry(app, textvariable=name_var)
name_entry.pack()

gender_label = tk.Label(app, text="Gender:")
gender_label.pack()
gender_choices = ["Male", "Female", "Other"]
gender_var.set(gender_choices[0])  # Default choice
gender_menu = tk.OptionMenu(app, gender_var, *gender_choices)
gender_menu.pack()

contact_label = tk.Label(app, text="Contact:")
contact_label.pack()
contact_entry = tk.Entry(app, textvariable=contact_var)
contact_entry.pack()
address_label = tk.Label(app, text="Address:")
address_label.pack()
address_entry = tk.Entry(app, textvariable=address_var)
address_entry.pack()

travel_history_label = tk.Label(app, text="Travel History:")
travel_history_label.pack()
travel_history_choices = ["Yes", "No"]
travel_history_var.set(travel_history_choices[1])  # Default choice
travel_history_menu = tk.OptionMenu(app, travel_history_var, *travel_history_choices)
travel_history_menu.pack()

symptoms_label = tk.Label(app, text="Symptoms:")
symptoms_label.pack()
symptoms_entry = tk.Entry(app, textvariable=symptoms_var)
symptoms_entry.pack()

# Save Button
save_button = tk.Button(app, text="Save Data", command=save_data)
save_button.pack()

# Search Entry
search_label = tk.Label(app, text="Search by Name:")
search_label.pack()
search_entry = tk.Entry(app, textvariable=name_var)
search_entry.pack()

search_button = tk.Button(app, text="Search", command=search_data)
search_button.pack()

# Search Result
search_result_text = tk.Text(app, width=60, height=10)
search_result_text.pack()

# Run the main loop
app.mainloop()