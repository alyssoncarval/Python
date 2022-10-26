import sqlite3

conn = sqlite3.connect('Users.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF IT DOES'NT EXISTS Users (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    User TEXT NOT NULL,
    Password TEXT NOT NULL
);
""")

print("Conectando ao Banco de Dados")