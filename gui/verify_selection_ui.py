import tkinter as tk
from tkinter import messagebox
from gui.verify_file_ui import verify_file_ui
from gui.verify_collection_ui import verify_collection_ui

def verify_selection_ui(app):
    selection_window = tk.Toplevel()
    selection_window.title("VERIFICAR")
    selection_window.geometry("350x180")
    selection_window.resizable(False, False)

    # Estilo
    label_font = ("Helvetica", 14)
    button_font = ("Helvetica", 14)
    button_bg = "#2e3f4f"
    button_fg = "#ffffff"
    button_active_bg = "#1c262f"
    button_active_fg = "#e6e6e6"
    pady = 10
    padx = 20

    tk.Label(selection_window, text="¿QUÉ DESEA VERIFICAR?", font=label_font).pack(pady=pady, padx=padx)

    def verify_file():
        selection_window.destroy()
        verify_file_ui(app)

    def verify_collection():
        verify_collection_ui(app)

    tk.Button(selection_window, text="EXPEDIENTE", font=button_font, bg=button_bg, fg=button_fg,
              activebackground=button_active_bg, activeforeground=button_active_fg, command=verify_file).pack(pady=pady, padx=padx, fill="x")

    tk.Button(selection_window, text="COLECCIÓN", font=button_font, bg=button_bg, fg=button_fg,
              activebackground=button_active_bg, activeforeground=button_active_fg, command=verify_collection).pack(pady=pady, padx=padx, fill="x")

if __name__ == "__main__":
    root = tk.Tk()
    app = None
    verify_selection_ui(app)
    root.mainloop()
