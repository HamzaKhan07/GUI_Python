import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root=tk.Tk()

canvas=tk.Canvas(root, width=600, height=340)
canvas.grid(columnspan=3, rowspan=3)

# logo
logo = Image.open('images/logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# instructions
instructions=tk.Label(root, text="Select the pdf you want to extract", font=("Arial", 14))
instructions.grid(column=1, row=1)


# open file
def open_file():
    browse_text.set('loading...')
    file=askopenfile(parent=root, mode='rb', title='Select a file')
    if file:
        print(file.name)
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        text=tk.Text(root, width=50, height=10, padx=15, pady=15)
        text.insert(1.0, page_content)
        text.grid(column=1, row=3)

    browse_text.set('Browse')


# browse button
browse_text=tk.StringVar()
browse=tk.Button(root, command=lambda: open_file(), textvariable=browse_text, font=("Arial", 14), foreground="white", bg="#20bebe",
                 height=2, width=15)
browse_text.set('Browse')
browse.grid(column=1, row=2)

canvas=tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)


# render window
root.mainloop()