import tkinter as tk
from tkinter import scrolledtext
import tkinter.font as tkFont

def generate_email():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    net_id = entry_net_id.get()
    reason = entry_reason.get()
    date_range = entry_date_range.get()
    courses = [entry_course1.get(), entry_course2.get(), entry_course3.get(), entry_course4.get(), 
               entry_course5.get(), entry_course6.get(), entry_course7.get(), entry_course8.get()]

    # Filter out any empty course entries
    valid_courses = [course for course in courses if course]

    email_text = f"""
Dear Faculty,

You are receiving this message because {first_name} {last_name} ({net_id}) is listed as a student in a class you teach.
The College of Nursing and Health Sciences has received notification that the student is experiencing a {reason} concern.
The CNHS Dean’s Office is in support of the following academic adjustments:

• Class Attendance
• Assignments
• Test Dates

From: {date_range}

{first_name}, we wish you the best while you navigate this situation; please note that it is your responsibility to follow up with each of your professors in a timely manner to discuss any missed assignments/exams and getting back on track.
Your professors are expecting to hear from you regarding this request for flexibility as soon as you are able, and your professors may not be able to provide the flexibility if you delay in reaching out to them. If you need help navigating those conversations, please connect with your advisor or with CNHS Student Services.   


Student is enrolled in the following courses:
""" 

    # Add bullet points for each course
    for course in valid_courses:
        email_text += f"• {course}\n"

    email_text += """
Thank you,
Office of Student Services
College of Nursing and Health Sciences
"""

    # Clear the text box and insert the generated email
    email_display.delete(1.0, tk.END)
    email_display.insert(tk.END, email_text)

# Create the main window
root = tk.Tk()
root.title("CNHS Dean's Note Generator")

# Create a font object for Aptos, size 12
aptos_font = tkFont.Font(family="Aptos", size=12)

# Add a title and author credits
tk.Label(root, text="CNHS Dean's Note Generator", font=('Arial', 16, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
tk.Label(root, text="Created by Dylan Rhymaun 9.19.2024", font=('Arial', 10)).grid(row=1, column=0, columnspan=2, pady=5)

# Add input fields
tk.Label(root, text="Student First Name:").grid(row=2)
tk.Label(root, text="Student Last Name:").grid(row=3)
tk.Label(root, text="Student Net ID:").grid(row=4)
tk.Label(root, text="Health or Personal?:").grid(row=5)
tk.Label(root, text="Date Range:").grid(row=6)
tk.Label(root, text="Course 1:").grid(row=7)
tk.Label(root, text="Course 2:").grid(row=8)
tk.Label(root, text="Course 3:").grid(row=9)
tk.Label(root, text="Course 4:").grid(row=10)
tk.Label(root, text="Course 5:").grid(row=11)
tk.Label(root, text="Course 6:").grid(row=12)
tk.Label(root, text="Course 7:").grid(row=13)
tk.Label(root, text="Course 8:").grid(row=14)

entry_first_name = tk.Entry(root)
entry_last_name = tk.Entry(root)
entry_net_id = tk.Entry(root)
entry_reason = tk.Entry(root)
entry_date_range = tk.Entry(root)
entry_course1 = tk.Entry(root)
entry_course2 = tk.Entry(root)
entry_course3 = tk.Entry(root)
entry_course4 = tk.Entry(root)
entry_course5 = tk.Entry(root)
entry_course6 = tk.Entry(root)
entry_course7 = tk.Entry(root)
entry_course8 = tk.Entry(root)

entry_first_name.grid(row=2, column=1)
entry_last_name.grid(row=3, column=1)
entry_net_id.grid(row=4, column=1)
entry_reason.grid(row=5, column=1)
entry_date_range.grid(row=6, column=1)
entry_course1.grid(row=7, column=1)
entry_course2.grid(row=8, column=1)
entry_course3.grid(row=9, column=1)
entry_course4.grid(row=10, column=1)
entry_course5.grid(row=11, column=1)
entry_course6.grid(row=12, column=1)
entry_course7.grid(row=13, column=1)
entry_course8.grid(row=14, column=1)

# Add a button to generate the email
tk.Button(root, text="Generate Email", command=generate_email).grid(row=15, column=1)

# Add a scrollable text box to display the generated email, with custom font
email_display = scrolledtext.ScrolledText(root, width=80, height=20, wrap=tk.WORD, font=aptos_font)
email_display.grid(row=16, column=0, columnspan=2)

root.mainloop()
