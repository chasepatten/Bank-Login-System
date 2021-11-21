import sqlite3
import hashlib


# Function used to add a new username and hashed password to the users table
def add_user(username, password):
    connection = sqlite3.connect('ppab6.db')
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO users (username, hash_password)
                   VALUES (?, ?)''', (username, password))

    connection.commit()
    connection.close()


# Function used to hash the password given by the user
def hash_password(password):
    # Function used to hash a password provided
    input_password = hashlib.sha256()
    input_password.update(password.encode('UTF-8'))
    return input_password.hexdigest()


# Functions pulls all data from a table specified and prints it out.
def fetch_table_data():
    # Creates a connection to the database specified in ''
    connection = sqlite3.connect('ppab6.db')
    # Creates a cursor object to manipulate the database with
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users')

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    connection.close()


def check_if_username_exists(username):
    connection = sqlite3.connect('ppab6.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users WHERE username = ?;', [username])
    username_check = cursor.fetchone()
    while username_check == username:
        print("This username is already taken\n Please input a new one. ")
        username_check = input(str("Please enter a username to add: "))


username_to_add = input(str("Please enter a username to add: "))
check_passed = check_if_username_exists(username_to_add)
password_to_hash = input(str("Please enter a password for this account: "))
hashed_password = hash_password()

if check_passed is True:
    password_to_hash = input(str("Please enter a password for this username: "))
    hashed_password = hash_password(password_to_hash)

add_user(username_to_add, hashed_password)
fetch_table_data()