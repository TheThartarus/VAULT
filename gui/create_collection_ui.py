# Importar Tkinter
import tkinter as tk
from tkinter import messagebox

# Importar módulo de base de datos correspondiente
from data.functions.create_collection_db import create_collection_db

# Definir el UI
def create_collection_ui(app):
    # Configurar las propiedades de la ventana
    new_window = tk.Toplevel()
    new_window.title("CREAR")
    new_window.geometry("500x125")
    new_window.resizable(False, False)
    new_window.grid_columnconfigure(0, weight=1)
    new_window.grid_columnconfigure(1, weight=1)

    # Definir variables de estilo
    label_font = ("Helvetica", 14)
    entry_font = ("Helvetica", 14)
    button_font = ("Helvetica", 14)
    button_bg = "#2e3f4f"
    button_fg = "#ffffff"
    button_active_bg = "#1c262f"
    button_active_fg = "#e6e6e6"
    padx = 20
    pady = 10

    # Desplegar el 'Label' y configurar el 'grid'
    tk.Label(new_window, text="N° DE COLECCIÓN", font=label_font).grid(row=0, column=0, pady=pady, padx=padx, sticky="e")

    # Desplegar el 'Input'
    collection_number_var = tk.Entry(new_window, font=entry_font)

    # Configurar el 'grid' del 'Input'
    collection_number_var.grid(row=0, column=1, pady=pady, padx=padx, sticky="ew")

    def submit():
        collection_number = collection_number_var.get()
        if create_collection_db(collection_number):
            messagebox.showinfo("ÉXITO", "COLECCIÓN CREADA EXITOSAMENTE")
            app.update_add_button_state()
            new_window.destroy()
        else:
            messagebox.showerror("ERROR", "LA COLECCIÓN YA EXISTE O HUBO UN ERROR")
    
    # Desplegar y configurar el estilo del botón submit "ENVIAR"
    submit_button = tk.Button(new_window, text="ENVIAR", font=button_font, bg=button_bg, fg=button_fg,
                              activebackground=button_active_bg, activeforeground=button_active_fg, command=submit)
    
    # Configurar el 'grid' del botón "ENVIAR"
    submit_button.grid(row=1, column=0, columnspan=2, pady=20, padx=padx, sticky="ew")

if __name__ == "__main__":
    root = tk.Tk()
    app = None
    create_collection_ui(app)
    root.mainloop()
