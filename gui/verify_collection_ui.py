import tkinter as tk
from tkinter import messagebox

def verify_collection_ui(app):
    new_window = tk.Toplevel()
    new_window.title("VERIFICAR")
    new_window.geometry("500x125")
    new_window.resizable(False, False)
    new_window.grid_columnconfigure(0, weight=1)
    new_window.grid_columnconfigure(1, weight=1)

    # Estilo
    pady = 10
    padx = 20
    label_font = ("Helvetica", 14)
    entry_font = ("Helvetica", 14)
    button_font = ("Helvetica", 14)
    button_bg = "#2e3f4f"
    button_fg = "#ffffff"
    button_active_bg = "#1c262f"
    button_active_fg = "#e6e6e6"

    # Inputs
    tk.Label(new_window, text="N° DE COLECCIÓN", font=label_font).grid(row=0, column=0, pady=pady, padx=padx, sticky="e")
    collection_number_var = tk.Entry(new_window, font=entry_font)
    collection_number_var.grid(row=0, column=1, pady=pady, padx=padx, sticky="ew")

    submit_button = tk.Button(new_window, text="ENVIAR", font=button_font, bg=button_bg, fg=button_fg,
                              activebackground=button_active_bg, activeforeground=button_active_fg)
    submit_button.grid(row=1, column=0, columnspan=2, pady=20, padx=padx, sticky="ew")

if __name__ == "__main__":
    root = tk.Tk()
    app = None
    verify_collection_ui(app)
    root.mainloop()
