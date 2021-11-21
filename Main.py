import hashlib  # imports hashlib library to hash our passwords input by user
import json  # imports the library needed to manipulate JSON files
import add_user

# Function used to determine if the username and password provided are correct
def is_valid_credentials(username, password):
    # opens the json file
    with open(r'C:\Users\chase\PycharmProjects\UserLogins\Credentials.json') as credentials:
        # loads JSON file into variable called 'json_data'
        json_data = json.load(credentials)

    # Assigns the username taken in by the function to a new variable called 'username_to_check'
    username_to_check = username
    # Assigns the password taken in by the function to a new variable called 'password_to_check'
    password_to_check = password

    # For loop used to iterate through the dictionary checking username's and passwords
    for key, value in json_data.items():
        if key == username_to_check and value == password_to_check:
            return True


# Function used to hash the password given by the user
def hash_password(password):
    # Function used to hash a password provided
    password_to_hash = hashlib.sha256()
    password_to_hash.update(password.encode('UTF-8'))
    return password_to_hash.hexdigest()


# Simple sign in page prompt
print("Welcome to the sign in page!\n")
user_name = input(str("Please enter your username: "))
pass_word = input(str("Please enter your password: "))

# Function takes in the password input by user and then hashes it
hashed_password = hash_password(pass_word)
# Function checks to see if the credentials presented by user are valid against our JSON file
login_check = is_valid_credentials(user_name, hashed_password)

# Conditional used to determine if the login check passed
if login_check is True:
    print("\n*******************************************")
    print("Welcome to my Bank!\nPlease Log In!")
    print("*******************************************")

else:
    print("\nPassword and/or Username do not match!")

add_user.add_user()