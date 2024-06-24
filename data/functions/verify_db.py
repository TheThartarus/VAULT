from data.database import Database

def get_file_details(classification, year, file_number):
    db = Database()
    try:
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM files WHERE classification = ? AND year = ? AND file_number = ?",
                       (classification, year, file_number))
        return cursor.fetchone()
    finally:
        db.connection.close()

def update_file_details(classification, year, file_number, collection_number, relative_position, crimes):
    db = Database()
    try:
        db.connection.execute('''
            UPDATE files
            SET collection_number = ?, relative_position = ?, crimes = ?
            WHERE classification = ? AND year = ? AND file_number = ?
        ''', (collection_number, relative_position, crimes, classification, year, file_number))
        db.connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        db.connection.close()
