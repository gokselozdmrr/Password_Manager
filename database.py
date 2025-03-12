import sqlite3

def insert_password(service, username, password):
    """It inserts passwords into the database"""
    connection = sqlite3.connect("identifier.sqlite")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO passwords(service,username,password) VALUES (?,?,?)", (service, username, password))

    connection.commit()
    connection.close()


def get_password(service):
    """It gets password that belongs to related service"""
    connection = sqlite3.connect("identifier.sqlite")
    cursor = connection.cursor()

    cursor.execute("SELECT username,password FROM passwords WHERE service=?", (service,))
    result = cursor.fetchone()
    connection.close()

    return result