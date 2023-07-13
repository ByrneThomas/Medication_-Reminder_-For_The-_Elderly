import tkinter as tk
from tkinter import ttk
import datetime
import csv
from tkinter import messagebox
import pyttsx3
import dateutil.parser

def speak_text(command):
    text = pyttsx3.init()
    text.say(command)
    text.runAndWait()

# Constants
MEDICATION_FILE = 'medication.csv'

# Function to load medication data from CSV
def load_medication_data():
    medication_data = []
    with open(MEDICATION_FILE, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            medication_data.append(row)
    return medication_data

# Function to display medication information
def display_medication_info():
    medication_data = load_medication_data()
    for row in medication_data:
        label_medication_name = tk.Label(top, text=row, font=("Arial", 12), fg="#FFFFFF", bg="#333333")
        label_medication_name.pack(pady=10)

# Function to set reminders for medication
def set_medication_reminders():
    medication_data = load_medication_data()
    current_time = datetime.datetime.now().strftime("%H:%M")

    for row in medication_data:
        medication_name = row[0]
        frequency = row[2]
        schedule_time_str = row[3]

        # Parse the schedule time string to a datetime object
        schedule_time = dateutil.parser.parse(schedule_time_str).strftime("%H:%M")

        if current_time == schedule_time:
            messagebox.showinfo("Medication Reminder", f"It's time to take {medication_name}.")
            print(f"Reminder: Take {medication_name}!")

# Function to add medication to the schedule
def add_medication_schedule():
    medication_name = entry_medication_name.get()
    dosage = entry_dosage.get()
    frequency = entry_frequency.get()
    schedule_time = entry_schedule_time.get()

    # Append the medication schedule to the CSV file
    with open(MEDICATION_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([medication_name, dosage, frequency, schedule_time])
    messagebox.showinfo("Success", "Medication schedule added successfully.")

def add_medication():
    top1 = tk.Toplevel()
    top1.title("Add Medication")
    top1.geometry("400x300")
    top1.config(bg='#333333')
    global entry_medication_name
    global entry_dosage
    global entry_frequency
    global entry_schedule_time

    # Medication Schedule Form
    label_medication_name = tk.Label(top1, text="Medication Name:", font=("Arial", 12), fg="#FFFFFF", bg="#333333")
    label_medication_name.pack(pady=5)
    entry_medication_name = tk.Entry(top1, font=("Arial", 12))
    entry_medication_name.pack(pady=5)

    label_dosage = tk.Label(top1, text="Dosage:", font=("Arial", 12), fg="#FFFFFF", bg="#333333")
    label_dosage.pack(pady=5)
    entry_dosage = tk.Entry(top1, font=("Arial", 12))
    entry_dosage.pack(pady=5)

    label_frequency = tk.Label(top1, text="Frequency:", font=("Arial", 12), fg="#FFFFFF", bg="#333333")
    label_frequency.pack(pady=5)
    entry_frequency = tk.Entry(top1, font=("Arial", 12))
    entry_frequency.pack(pady=5)

    label_schedule_time = tk.Label(top1, text="Schedule Time:", font=("Arial", 12), fg="#FFFFFF", bg="#333333")
    label_schedule_time.pack(pady=5)
    entry_schedule_time = tk.Entry(top1, font=("Arial", 12))
    entry_schedule_time.pack(pady=5)

    button_add_medication = tk.Button(top1, text="Add Medication", command=add_medication_schedule, font=("Arial", 12), fg="#000000", bg="#117A65")
    button_add_medication.pack(pady=5)
    top1.after(500, speak_text, "You have clicked on Add Medication App. Kindly enter your Medication, Dosage, Frequency, and schedule time")
    top1.mainloop()

def display_medication():
    top = tk.Toplevel()
    top.title("Display Medication Reminder")
    top.geometry("400x300")
    top.config(bg='#333333')

    # Medication Schedule Form
    label_medication_name = tk.Label(top, text='Display Medication', font=("Arial", 16), fg="#FFFFFF", bg="#333333")
    label_medication_name.pack(pady=10)

    label_medication_info_btn = tk.Button(top, text='Click to view Medication', command=display_medication_info, font=("Arial", 12), fg="#000000", bg="#117A65")
    label_medication_info_btn.pack(pady=10)

    top.after(500, speak_text, "You have clicked on Display Medication App successfully")
    top.mainloop()

def close():
    window.destroy()

# Create the main window
window = tk.Tk()
window.title("Medication App")
window.geometry("400x300")
window.config(bg='#333333')

# Create a label with custom styling
label = tk.Label(window, text="Medication Reminder App", font=("Arial", 20), pady=20, bg='#333333', fg='#FFFFFF')
label.pack()

# Create a styled frame for buttons
button_frame = ttk.Frame(window, padding=20)
button_frame.pack()

# Create three styled buttons vertically aligned
button1 = ttk.Button(button_frame, text="Add Medication", command=add_medication, style="Custom.TButton")
button1.pack(pady=10)

button2 = ttk.Button(button_frame, text="Display Medication", command=display_medication, style="Custom.TButton")
button2.pack(pady=10)

button3 = ttk.Button(button_frame, text="Set Reminder", command=set_medication_reminders, style="Custom.TButton")
button3.pack(pady=10)

button4 = ttk.Button(button_frame, text="Exit/Close", command=close, style="Custom.TButton")
button4.pack(pady=10)

# Define custom styling for the buttons
style = ttk.Style()
style.configure("Custom.TButton", font=("Arial", 12), foreground="#000000", background="#117A65", relief="raised")
style.map("Custom.TButton", foreground=[('active', 'red'), ('disabled', 'gray')], background=[('active', '#0E4C3C'), ('disabled', 'gray')])

window.after(500, speak_text, "Welcome to our advanced Medication Reminder App. It offers features to add, display, set reminders, and exit with ease.")

# Start the main event loop
window.mainloop()
