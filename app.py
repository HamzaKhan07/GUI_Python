import tkinter as tk
from PIL import Image, ImageTk

root=tk.Tk()

canvas=tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# logo
logo = Image.open('images/logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# instructions
instructions=tk.Label(root, text="Upload the Image of Infected Skin Disease", font=("Arial", 14))
instructions.grid(column=1, row=1)

# button
upload_text=tk.StringVar()
upload_button=tk.Button(root, textvariable=upload_text, width=15, height=2, bg="#20bebe",
                        foreground="white", font=("Arial", 14))
upload_text.set("Upload")
upload_button.grid(column=1, row=2)

canvas=tk.Canvas(root, width=600, height=450)
canvas.grid(columnspan=3, rowspan=7)

# image
image = Image.open('images/act1.jpg')
image = ImageTk.PhotoImage(image)
image_label=tk.Label(image=image, width=300, height=190)
image_label.image=image
image_label.grid(column=1, row=3, pady=40)

# Detected Disease label
detected_label=tk.Label(root, text='Detected Skin Disease', font=('Arial', 12))
detected_label.grid(column=1, row=4)

# Disease Name
detected_disease=tk.Label(root, text='Pigmented Benign Kertosis', font=('Arial', 22))
detected_disease.grid(column=1, row=5)

# Confidence label
detected_label=tk.Label(root, text='Confidence', font=('Arial', 12))
detected_label.grid(column=1, row=6, pady=(25, 0))

# Confidence
detected_disease=tk.Label(root, text='98.69', font=('Arial', 22))
detected_disease.grid(column=1, row=7)

# Description label
description_label=tk.Label(root, text='Description', font=('Arial', 12))
description_label.grid(column=1, row=8, pady=(25, 0))

# Description label
desc='This is some description about the disease.\nThis is some description about the disease.\n'\
     'This is some description about the disease.'

description_text=tk.Label(root, text=desc, font=('Arial', 12))
description_text.grid(column=1, row=9, pady=(0, 35))

# render window
root.mainloop()

