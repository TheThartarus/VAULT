from data.database import Database

def add_file_db(classification, year, file_number, collection_number, relative_position, crimes):
    db = Database()
    try:
        db.connection.execute('''
            INSERT INTO files (classification, year, file_number, collection_number, relative_position, crimes)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (classification, year, file_number, collection_number, relative_position, crimes))
        db.connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        db.connection.close()
