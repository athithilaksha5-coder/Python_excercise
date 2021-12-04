import sqlite3
connection = sqlite3.connect("library.db")
cursor = connection.cursor()
print("Dastabase created successfully")
cursor.execute("drop table librarybooks")
cursor.execute("create table librarybooks(ID INTEGER PRIMARY KEY AUTOINCREMENT, BOOK_NAME TEXT,BOOK_AUTHOR TEXT,BOOK_PUBLISHER TEXT,NO_OF_BOOKS INTEGER)")
print("Table created successfully")
connection.close()

