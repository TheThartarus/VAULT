# Importar Tkinter
import tkinter as tk
from tkinter import messagebox

# Importar los módulos
from gui.create_collection_ui import create_collection_ui
from gui.add_file_ui import add_file_ui
from gui.verify_selection_ui import verify_selection_ui
from data.database import Database

# Crear la clase principal
class VaultApp:
    def __init__(self, root):
        # Configurar las propiedades de la ventana
        self.root = root
        self.root.title("Vault")
        self.root.geometry("200x360")
        self.root.resizable(False, False)
        root.grid_columnconfigure(0, weight=1)

        # Definir variables de estilo
        self.button_font = ("Helvetica", 14)
        self.button_bg = "#2e3f4f"
        self.button_fg = "#ffffff"
        self.button_active_bg = "#1c262f"
        self.button_active_fg = "#e6e6e6"
        self.padx = 20
        self.pady = 10

        # Desplegar los botones
        self.create_button = self.create_ui_button("CREAR", self.open_create_collection, 0)
        self.add_button = self.create_ui_button("AÑADIR", self.open_add_file, 1)
        self.verify_button = self.create_ui_button("VERIFICAR", self.open_verify_selection, 2)
        self.delete_button = self.create_ui_button("ELIMINAR", None, 3)
        self.export_button = self.create_ui_button("EXPORTAR", None, 4)
        self.credits_button = self.create_ui_button("CRÉDITOS", None, 5)

        # Verificar estado del botón "AÑADIR"
        self.update_add_button_state()

    # Definir función para crear los botones
    def create_ui_button(self, text, command, row):
        '''
        Crea los botones.

        --- PARÁMETROS ---

        text (str) -         TEXTO INTERNO DEL BOTÓN.
        command (funct) -    ACCIÓN QUE HARÁ AL HACER CLICK EN EL BOTÓN.
        row (int) -          FILA QUE OCUPARÁ EL BOTÓN.
        '''
    
        # Crea y configura el estilo del botón
        button = tk.Button(self.root, text=text, font=self.button_font, bg=self.button_bg, fg=self.button_fg,
                           activebackground=self.button_active_bg, activeforeground=self.button_active_fg, command=command)
    
        # Configura el 'grid' del botón.
        button.grid(row=row, column=0, padx=self.padx, pady=self.pady, sticky="ew")

        # Retorna el botón
        return button

    # Definir función para verificar estado del botón "AÑADIR"
    def update_add_button_state(self):
        '''
        Verifica el estado del botón AÑADIR. \n
        Si no hay ninguna colección en la base de datos, el botón estará deshabilitado.
        '''
        db = Database()
        collections = db.get_all_collections()
        self.add_button.config(state=tk.NORMAL if collections else tk.DISABLED)

    def open_create_collection(self):
        create_collection_ui(self)

    def open_add_file(self):
        add_file_ui(self)

    def open_verify_selection(self):
        verify_selection_ui(self)

if __name__ == "__main__":
    root = tk.Tk()
    app = VaultApp(root)
    root.mainloop()
