import sqlite3


connection = sqlite3.connect('ppab6.db')
cursor = connection.cursor()


print("Dropping table...")
cursor.execute("DROP TABLE users;")
print("Table dropped.")


connection.commit()
connection.close()