# Importar SQLite
import sqlite3

# Definir clase principal de la base de datos
class Database:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.create_tables()

    def create_tables(self):
        '''
        Crea las tablas de la base de datos.
        '''
        with self.connection:
            '''
            La tabla de las colecciones tendrá las siguientes columnas:

            id (int)
            collection_number (str) -   NÚMERO DE COLECCIÓN
            status (str) -              ESTATUS
            num_files (int) -           NÚMERO DE EXPEDIENTES ALOJADOS
            position_reference (str) -  REFERENCIA DE POSICIÓN FÍSICA-REAL
            '''
            self.connection.execute('''CREATE TABLE IF NOT EXISTS collections (
                                       id INTEGER PRIMARY KEY,
                                       collection_number TEXT NOT NULL UNIQUE,
                                       status TEXT NOT NULL,
                                       num_files INTEGER,
                                       position_reference TEXT)''')
            
            '''
            La tabla de los expedientes tendrá las siguientes columnas:

            id (int)
            classification (str) -                  CLASIFICACIÓN
            year (int) -                            AÑO
            file_number (int) -                     NÚMERO DE EXPEDIENTE
            collection_number (int - FOREIGN KEY) - NÚMERO DE COLECCIÓN EN EL QUE ALOJA
            relative_position (str) -               POSICIÓN RELATIVA EN EL INTERIOR DE LA COLECCIÓN
            crimes (str) -                          DELITO(S)
            '''
            self.connection.execute('''CREATE TABLE IF NOT EXISTS files (
                                       id INTEGER PRIMARY KEY,
                                       classification TEXT NOT NULL,
                                       year INTEGER NOT NULL,
                                       file_number INTEGER NOT NULL,
                                       collection_number TEXT,
                                       relative_position TEXT,
                                       crimes TEXT,
                                       FOREIGN KEY (collection_number) REFERENCES collections (collection_number))''')

    def get_all_collections(self):
        '''
        Retorna todas las colecciones que hayan en la base de datos.
        '''
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM collections")
            return cursor.fetchall()

    def get_all_files(self):
        '''
        Retorna todos los expedientes que hayan en la base de datos.
        '''
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM files")
            return cursor.fetchall()
