# Importar Tkinter
import tkinter as tk
from tkinter import messagebox

# Importar la clase principal de la base de datos
from data.database import Database

# Importar módulo de base de datos correspondiente
from data.functions.add_file_db import add_file_db

def get_all_collection_numbers():
    db = Database()
    try:
        collections = db.get_all_collections()
        return [str(row[1]) for row in collections]  # Extrayendo números de colección
    finally:
        db.connection.close()

def add_file_ui(app):
    # Configurar las propiedades de la ventana
    new_window = tk.Toplevel()
    new_window.title("AÑADIR")
    new_window.geometry("500x400")
    new_window.resizable(False, False)
    new_window.grid_columnconfigure(0, weight=1)
    new_window.grid_columnconfigure(1, weight=1)

    # Definir variables de estilo
    style_config = {
        "label_font": ("Helvetica", 14),
        "entry_font": ("Helvetica", 14),
        "button_font": ("Helvetica", 14),
        "button_bg": "#2e3f4f",
        "button_fg": "#ffffff",
        "button_active_bg": "#1c262f",
        "button_active_fg": "#e6e6e6",
        "pady": 10,
        "padx": 20
    }

    # Inputs
    def create_label(text, row):
        tk.Label(new_window, text=text, font=style_config["label_font"]).grid(row=row, column=0, pady=style_config["pady"], padx=style_config["padx"], sticky="e")

    def create_entry(row):
        entry = tk.Entry(new_window, font=style_config["entry_font"])
        entry.grid(row=row, column=1, pady=style_config["pady"], padx=style_config["padx"], sticky="ew")
        return entry

    def create_option_menu(variable, options, row):
        tk.OptionMenu(new_window, variable, *options).grid(row=row, column=1, pady=style_config["pady"], padx=style_config["padx"], sticky="ew")

    create_label("CLASIFICACIÓN", 0)
    classification_var = tk.StringVar(new_window)
    classification_options = ["MP", "MJ", "MK", "C"]
    create_option_menu(classification_var, classification_options, 0)

    create_label("AÑO", 1)
    year_var = create_entry(1)

    create_label("N° DE EXPEDIENTE", 2)
    file_number_var = create_entry(2)

    create_label("N° DE COLECCIÓN", 3)
    collection_number_var = tk.StringVar(new_window)
    collections = get_all_collection_numbers()
    create_option_menu(collection_number_var, collections, 3)

    create_label("POSICIÓN RELATIVA", 4)
    relative_position_var = tk.StringVar(new_window)
    relative_position_options = ["ARRIBA", "MITAD", "ABAJO"]
    create_option_menu(relative_position_var, relative_position_options, 4)

    create_label("DELITO(S)", 5)
    crimes_var = create_entry(5)

    def submit():
        classification = classification_var.get()
        year = year_var.get()
        file_number = file_number_var.get()
        collection_number = collection_number_var.get()
        relative_position = relative_position_var.get()
        crimes = crimes_var.get()

        if add_file_db(classification, year, file_number, collection_number, relative_position, crimes):
            messagebox.showinfo("ÉXITO", "EXPEDIENTE AÑADIDO EXITOSAMENTE")
            new_window.destroy()
        else:
            messagebox.showerror("ERROR", "HUBO UN ERROR AL AÑADIR EL EXPEDIENTE")

    tk.Button(new_window, text="ENVIAR", font=style_config["button_font"], bg=style_config["button_bg"], fg=style_config["button_fg"],
              activebackground=style_config["button_active_bg"], activeforeground=style_config["button_active_fg"], command=submit).grid(row=6, column=0, columnspan=2, pady=20, padx=style_config["padx"], sticky="ew")

if __name__ == "__main__":
    root = tk.Tk()
    app = None
    add_file_ui(app)
    root.mainloop()
