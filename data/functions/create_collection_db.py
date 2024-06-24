# Importar SQLite
import sqlite3

# Importar la clase principal de la base de datos
from data.database import Database

def create_collection_db(collection_number):
    '''
    Crea una colección en la base de datos.

    --- PARÁMETROS ---

    colecction_number (int) - NÚMERO DE COLECCIÓN A CREAR

    --- RETORNA ---

    True - (COLECCIÓN CREADA EXITOSAMENTE) \n
    False - (LA COLECCIÓN YA EXISTE O HUBO UN ERROR)
    '''
    db = Database()
    try:
        db.connection.execute("INSERT INTO collections (collection_number, status, num_files, position_reference) VALUES (?, ?, ?, ?)",
                              (collection_number, 'ABIERTO', 0, ''))
        db.connection.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        db.connection.close()
