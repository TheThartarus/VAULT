import tkinter as tk
from tkinter import messagebox
from data.functions.verify_db import get_file_details, update_file_details

def verify_file_ui(app):
    def load_file_details():
        classification = classification_var.get()
        year = year_var.get()
        file_number = file_number_var.get()
        if not classification or not year or not file_number:
            messagebox.showerror("ERROR", "TODOS LOS CAMPOS SON OBLIGATORIOS")
            return
        
        file_details = get_file_details(classification, year, file_number)
        if file_details:
            collection_number_var.set(file_details[4])
            relative_position_var.set(file_details[5])
            crimes_var.set(file_details[6])
            toggle_inputs(True)
        else:
            messagebox.showerror("ERROR", "EXPEDIENTE NO ENCONTRADO")

    def toggle_inputs(state):
        # Alternar todos los campos excepto los tres iniciales y "N° DE COLECCIÓN"
        collection_number_entry.config(state=tk.DISABLED)
        relative_position_menu.config(state=tk.NORMAL if state else tk.DISABLED)
        crimes_entry.config(state=tk.NORMAL if state else tk.DISABLED)
        
        # Alternar los tres campos iniciales según el estado (solo deshabilitar si el estado es True).
        load_button.config(state=tk.DISABLED if state else tk.NORMAL)
        classification_menu.config(state=tk.DISABLED if state else tk.NORMAL)
        year_entry.config(state=tk.DISABLED if state else tk.NORMAL)
        file_number_entry.config(state=tk.DISABLED if state else tk.NORMAL)

    def save_file_details():
        classification = classification_var.get()
        year = year_var.get()
        file_number = file_number_var.get()
        collection_number = collection_number_var.get()
        relative_position = relative_position_var.get()
        crimes = crimes_var.get()
        
        if update_file_details(classification, year, file_number, collection_number, relative_position, crimes):
            messagebox.showinfo("ÉXITO", "EXPEDIENTE ACTUALIZADO CORRECTAMENTE")
        else:
            messagebox.showerror("ERROR", "HUBO UN ERROR AL ACTUALIZAR EL EXPEDIENTE")

    new_window = tk.Toplevel(app.root)
    new_window.title("VERIFICAR")
    new_window.geometry("500x500")
    new_window.resizable(False, False)
    new_window.grid_columnconfigure(0, weight=1)
    new_window.grid_columnconfigure(1, weight=1)

    # Estilo
    label_font = ("Helvetica", 14)
    entry_font = ("Helvetica", 14)
    button_font = ("Helvetica", 14)
    button_bg = "#2e3f4f"
    button_fg = "#ffffff"
    button_active_bg = "#1c262f"
    button_active_fg = "#e6e6e6"
    pady = 10
    padx = 20

    # Inputs
    tk.Label(new_window, text="CLASIFICACIÓN", font=label_font).grid(row=0, column=0, pady=pady, padx=padx, sticky="e")
    classification_var = tk.StringVar(new_window)
    classification_options = ["MP", "MJ", "MK", "C"]
    classification_menu = tk.OptionMenu(new_window, classification_var, *classification_options)
    classification_menu.config(font=entry_font)
    classification_menu.grid(row=0, column=1, pady=pady, padx=padx, sticky="ew")

    tk.Label(new_window, text="AÑO", font=label_font).grid(row=1, column=0, pady=pady, padx=padx, sticky="e")
    year_var = tk.StringVar(new_window)
    year_entry = tk.Entry(new_window, textvariable=year_var, font=entry_font)
    year_entry.grid(row=1, column=1, pady=pady, padx=padx, sticky="ew")

    tk.Label(new_window, text="N° DE EXPEDIENTE", font=label_font).grid(row=2, column=0, pady=pady, padx=padx, sticky="e")
    file_number_var = tk.StringVar(new_window)
    file_number_entry = tk.Entry(new_window, textvariable=file_number_var, font=entry_font)
    file_number_entry.grid(row=2, column=1, pady=pady, padx=padx, sticky="ew")

    load_button = tk.Button(new_window, text="CARGAR", font=button_font, bg=button_bg, fg=button_fg,
                            activebackground=button_active_bg, activeforeground=button_active_fg, command=load_file_details)
    load_button.grid(row=3, column=0, columnspan=2, pady=20, padx=padx, sticky="ew")

    tk.Label(new_window, text="N° DE COLECCIÓN", font=label_font).grid(row=4, column=0, pady=pady, padx=padx, sticky="e")
    collection_number_var = tk.StringVar(new_window)
    collection_number_entry = tk.Entry(new_window, textvariable=collection_number_var, font=entry_font, state=tk.DISABLED)
    collection_number_entry.grid(row=4, column=1, pady=pady, padx=padx, sticky="ew")

    tk.Label(new_window, text="POSICIÓN RELATIVA", font=label_font).grid(row=5, column=0, pady=pady, padx=padx, sticky="e")
    relative_position_var = tk.StringVar(new_window)
    relative_position_options = ["ARRIBA", "MITAD", "ABAJO"]
    relative_position_menu = tk.OptionMenu(new_window, relative_position_var, *relative_position_options)
    relative_position_menu.config(font=entry_font)
    relative_position_menu.grid(row=5, column=1, pady=pady, padx=padx, sticky="ew")

    tk.Label(new_window, text="DELITO(S)", font=label_font).grid(row=6, column=0, pady=pady, padx=padx, sticky="e")
    crimes_var = tk.StringVar(new_window)
    crimes_entry = tk.Entry(new_window, textvariable=crimes_var, font=entry_font)
    crimes_entry.grid(row=6, column=1, pady=pady, padx=padx, sticky="ew")

    save_button = tk.Button(new_window, text="GUARDAR", font=button_font, bg=button_bg, fg=button_fg,
                            activebackground=button_active_bg, activeforeground=button_active_fg, command=save_file_details)
    save_button.grid(row=7, column=0, columnspan=2, pady=20, padx=padx, sticky="ew")

    toggle_inputs(False)  # Deshabilitar campos no esenciales inicialmente

if __name__ == "__main__":
    root = tk.Tk()
    app = None
    verify_file_ui(app)
    root.mainloop()
