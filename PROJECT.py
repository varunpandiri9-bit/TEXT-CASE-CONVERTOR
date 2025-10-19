import tkinter as tk
from tkinter import ttk

def convert_text():
    text = input_text.get("1.0", tk.END).strip()
    choice = case_var.get()

    if choice == "Uppercase":
        result = text.upper()
    elif choice == "Lowercase":
        result = text.lower()
    elif choice == "Little Case":
        result = text.title()
    else:
        result = "Please select a case option."

    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)
    output_text.config(state=tk.DISABLED)


# Create main window
root = tk.Tk()
root.title("Text Case Converter")
root.geometry("500x400")
root.resizable(False, False)

# Title label
title_label = ttk.Label(root, text="📝 Text Case Converter", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Input label and text box
ttk.Label(root, text="Enter your text:").pack(anchor="w", padx=20)
input_text = tk.Text(root, height=5, width=50, wrap="word")
input_text.pack(padx=20, pady=5)

# Case selection
case_var = tk.StringVar(value="Uppercase")
frame = ttk.Frame(root)
frame.pack(pady=10)

ttk.Radiobutton(frame, text="Uppercase", variable=case_var, value="Uppercase").grid(row=0, column=0, padx=10)
ttk.Radiobutton(frame, text="Lowercase", variable=case_var, value="Lowercase").grid(row=0, column=1, padx=10)
ttk.Radiobutton(frame, text="Little Case", variable=case_var, value="Little Case").grid(row=0, column=2, padx=10)

# Convert button
convert_button = ttk.Button(root, text="Convert", command=convert_text)
convert_button.pack(pady=10)

# Output label and text box
ttk.Label(root, text="Converted text:").pack(anchor="w", padx=20)
output_text = tk.Text(root, height=5, width=50, wrap="word", state=tk.DISABLED)
output_text.pack(padx=20, pady=5)

# Run the main loop
root.mainloop()