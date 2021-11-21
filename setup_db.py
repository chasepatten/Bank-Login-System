import sqlite3


# Sets up a database named 'ppab6.db' and inserts initial VALUES into it
def setup_db():
    # Creates a connection to the database specified in ''
    connection = sqlite3.connect('ppab6.db')
    # Creates a cursor object to manipulate the database with
    cursor = connection.cursor()

    # Checks the table master list of the database to see if the table 'users' already exists
    # get the count of tables with the name 'users'
    cursor.execute('''SELECT count(name) FROM sqlite_master WHERE type= 'table'AND name = 'users' ''')
    if cursor.fetchone()[0] == 1:
        print("Table exists.")
        print("Dropping table...")
        cursor.execute("DROP TABLE users;")
        print("Table dropped.")

        
    # Creates table named users with two columns: username and password_hash
    cursor.execute('''CREATE TABLE users (username text, hash_password text)''')
    print("Table created with two columns: username, hash_password")                
    # inserts test username and password_hash into table
    cursor.execute("INSERT INTO users VALUES ('test','b8fd23c8ad9f90270d6ab278db7aae63318cb9b1d58922bf711a38d29251263f')")
    cursor.execute("INSERT INTO users VALUES ('robert','ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f')")
    cursor.execute("INSERT INTO users VALUES ('jake','f36d80e0148ef00e96eb77bd04090592bcee96e62fb878dd8b924aab07fbfaa6')")
    cursor.execute("INSERT INTO users VALUES ('nadia','20bab27736be2c8648914db45a1e49712b1c622fd1860af87d70846e0a19550b')")
    cursor.execute("INSERT INTO users VALUES ('maria','7022d1412263eb6885da804d5b95e12ee1e2ad726218e5e54bbcad538c3cb837')")
    cursor.execute("INSERT INTO users VALUES ('birdy','c7a2959c321e160af793742c523b9062f7a109321c740c7cf656b2495f02a9f0')")
    cursor.execute("INSERT INTO users VALUES ('randy','78d21a3d40a5e5d433b21e6bf13b773d04262f3d4f17022df15ad96d9b6e489d')")
    print("Values inserted into table...")
    # Save and commit the changes
    connection.commit()
    print("Changes to table and database are now saved...")
    # Closes the connection to the database
    print("Closing connection to database...\n")
    connection.close()


def print_table():
    connection = sqlite3.connect('ppab6.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)


setup_db()
print_table()
