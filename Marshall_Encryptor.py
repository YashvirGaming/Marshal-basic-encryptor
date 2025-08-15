import marshal, tkinter as tk, customtkinter as ctk
from tkinter import filedialog
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Marshall Basic Encryptor")
app.geometry("500x300")

def encrypt_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if not file_path:
        return
    with open(file_path, "r", encoding="utf-8") as f:
        source_code = f.read()
    code_obj = compile(source_code, "<string>", "exec")
    encrypted_code = marshal.dumps(code_obj)
    new_name = os.path.splitext(file_path)[0] + "_Encrypted.py"
    with open(new_name, "w", encoding="utf-8") as f:
        f.write("import marshal\n")
        f.write(f"exec(marshal.loads({repr(encrypted_code)}))")
    status_label.configure(text=f"Encrypted saved:\n{new_name}", text_color="green")

title_label = ctk.CTkLabel(app, text="Marshall Basic Encryptor", font=("Consolas", 20, "bold"))
title_label.pack(pady=20)

encrypt_btn = ctk.CTkButton(app, text="Load & Encrypt .py", command=encrypt_file, font=("Consolas", 15))
encrypt_btn.pack(pady=15)

status_label = ctk.CTkLabel(app, text="", font=("Consolas", 13))
status_label.pack(pady=10)

app.mainloop()
