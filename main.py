import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter
import os
import subprocess
import math
from tkinter import ttk


def merge_pdfs(pdf1_path, pdf2_path, output_path):
    # Open the two PDF files
    pdf1 = PdfReader(pdf1_path)
    pdf2 = PdfReader(pdf2_path)

    # Create a new PDF writer object
    pdf_writer = PdfWriter()

    if not radio_var:
        # Append all the pages from the first PDF and second PDF
        for page1, page2 in zip(pdf1.pages, pdf2.pages):
            pdf_writer.add_page(page1)
            pdf_writer.add_page(page2)
    else:
        # Append all the pages from the first PDF and second PDF in inverse order
        for page1, page2 in zip(pdf1.pages, reversed(pdf2.pages)):
            pdf_writer.add_page(page1)
            pdf_writer.add_page(page2)


    # # Append all the pages from the first PDF
    # for page in pdf1.pages:
    #     pdf_writer.add_page(page)
    #
    # # Append all the pages from the second PDF
    # for page in pdf2.pages:
    #     pdf_writer.add_page(page)

    # Write the merged PDF to the output file
    with open(output_path, "wb") as output_file:
        pdf_writer.write(output_file)

    show_success_message()
    # print("PDF files merged successfully!")


def select_pdf1():
    file_path = filedialog.askopenfilename(title="Select PDF 1", filetypes=(("PDF files", "*.pdf"),))
    label_pdf1.config(text=file_path)


def select_pdf2():
    file_path = filedialog.askopenfilename(title="Select PDF 2", filetypes=(("PDF files", "*.pdf"),))
    label_pdf2.config(text=file_path)


def select_output_location():
    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=(("PDF files", "*.pdf"),))
    label_output.config(text=output_path)


def merge_files():
    pdf1_path = label_pdf1.cget("text")
    pdf2_path = label_pdf2.cget("text")
    output_path = label_output.cget("text")
    merge_pdfs(pdf1_path, pdf2_path, output_path)


def open_output_folder():
    output_path = label_output.cget("text")
    if output_path:
        output_folder = os.path.dirname(output_path)
        output_folder = output_folder.replace("/", "\\")
        # print(output_folder)
        subprocess.Popen(f'explorer "{output_folder}"')


def show_success_message():
    success_label = tk.Label(window, text="Merge successful", fg="green")
    success_label.place(relx=0.5, rely=0.5, anchor="center")

    def fade_out():
        alpha = success_label.winfo_rgb(success_label["fg"]) + (0,)
        success_label.config(fg=f"#{alpha[0]:04x}{alpha[1]:04x}{alpha[2]:04x}")
        alpha = alpha[:-1] + (alpha[3] - 100,)
        if alpha[3] > 0:
            success_label.after(20, fade_out)
        else:
            success_label.destroy()

    success_label.after(2000, fade_out)


# Create the main window
window = tk.Tk()
window.title("PDF Merger")
# window.configure(bg="#090580")

# Calculate the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the window width and height
window_width = 600
window_height = 400

# Calculate the x and y coordinates for centering the window
x = math.floor((screen_width - window_width) / 2)
y = math.floor((screen_height - window_height) / 2)

# Set the window size and position
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Configure the style for themed widgets
style = ttk.Style(window)
style.theme_use('clam')


# Configure the style for the buttons
style.configure("TButton",
                background="#090580",
                foreground="white",
                font=("Arial", 12),
                padding=10,
                width=15)

# Configure the style for the labels
style.configure("TLabel",
                background="#23272A",
                foreground="white",
                font=("Arial", 12),
                padding=5)

radio_frame = ttk.Frame(window)
radio_frame.pack(pady=10)
radio_var = tk.IntVar()

radio_button1 = tk.Radiobutton(radio_frame, text="reverse order", variable=radio_var, value="0", bg="#dcdad5")
radio_button1.grid(row=0, column=0, padx=10, pady=4)

radio_button2 = tk.Radiobutton(radio_frame, text="normal", variable=radio_var, value="1", bg="#dcdad5")
radio_button2.grid(row=0, column=1, padx=10, pady=4)

# Configure the grid to span two columns
radio_frame.grid_columnconfigure(0, weight=1)
radio_frame.grid_columnconfigure(1, weight=1)


frame = ttk.Frame(window)
frame.pack(pady=20)

# Create a label and button for selecting PDF 1
label_pdf1 = tk.Label(frame, text="Select PDF 1:")
label_pdf1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

button_pdf1 = tk.Button(frame, text="Browse", command=select_pdf1)
button_pdf1.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Create a label and button for selecting PDF 2
label_pdf2 = tk.Label(frame, text="Select PDF 2:")
label_pdf2.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

button_pdf2 = tk.Button(frame, text="Browse", command=select_pdf2)
button_pdf2.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# Create a label and button for selecting output location
label_output = tk.Label(frame, text="Select Output Location:")
label_output.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

button_output = tk.Button(frame, text="Browse", command=select_output_location, width=10, height=2)
button_output.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

# Create a button to merge the PDF files
button_merge = tk.Button(frame, text="Merge PDFs", command=merge_files, width=15, height=3)
button_merge.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Create a button to open the output folder
button_open_folder = tk.Button(frame, text="Output Location", command=open_output_folder, width=15, height=3)
button_open_folder.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Start the main event loop
window.mainloop()
