# This is a program that will be asking users for their credentials. If the info entered is in the "database", the program will spit out the database itself and then clear the screen/close the program after 2 seconds. If the user isn't found, the program will prompt a msg to try again a few more times before forcing user to either register or exit.


import random
import string
import time
import json
import os

# checking whether user has installed pyfiglet (and avoiding cryptic error if not).
try:
    from pyfiglet import Figlet
except ModuleNotFoundError:
    pyfiglet_installed = False
else:
    pyfiglet_installed = True

# making database/dictionary (accounts.txt) available
file = open("accounts.txt", "rt")
db = json.load(file)
file.close()

# displaying welcoming msg and showing menu
print("########################################")
print("Welcome to Dean Dong Database\n")
time.sleep(2)
print("For a better user experience,\nensure you have pyfiglet installed")
time.sleep(1)
print("[optional] Run the following command:\npip install pyfiglet\n")
time.sleep(2)
print("########################################")
print("Please choose one of the following:\n")
time.sleep(1)
print("1 Login")
print("2 Register")
print("Q Quit")
print("########################################")

# main function of the program. which redirect users according to their choices (1 for login, 2 for register or q for quit)


def main():
    while True:
        user_choice = input("")
        if user_choice == "1":
            # ask user for username..
            username = input("Enter your username: ")

        # calling login function and passing "username" chosen as its argument
            login(username)

        elif user_choice == "2":
            # calling register() function if user chooses to sign-up
            register()
        elif user_choice == "q" or user_choice == "Q":
            # function sleep, from the library "time", holds the running of the program
            time.sleep(1)
            print("Good bye")
            time.sleep(2)
            exit(10)
        else:
            print("Not a valid input. Try again")

# as per our assessment specs, loading database on the screen for 2 seconds if user and password match and are valid/in the database


def display_db():
    db_file = open("accounts.txt", "r")
    # accessing json library so we can use the load function to store the database in a variable called file_display which then can be iterated over in the following line
    file_display = json.load(db_file)
    for username, password in file_display.items():
        print(f"Username: {username}, Password: {password}")
        time.sleep(0.5)
    time.sleep(2)
    clear_screen()

# this is a library that prints ASCII words on the screen at the end of the program
    if pyfiglet_installed:
        figlet = Figlet(font="slant")
        stylized_text = figlet.renderText(
            f"Hasta la vista")
        print(stylized_text)
    else:
        print(
            "Install 'pyfiglet' [pip install pyfiglet] to see stylized text.")

    time.sleep(2)
    exit(33)

# clear screen as per out assessment specs


def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# ask user to confirm password. if it matches the username provided, program runs. otherwise prompts the user to register or quit the program


def ask_for_password(username):
    # giving user 3 chances to enter correct password
    attempts = 2
    password = db[username]
    entered_password = input("Please enter your password: ")
    if entered_password == password:
        time.sleep(2)
        # if username and password match, show database
        display_db()
    else:

        while attempts > 0:
            print(f"Incorrect password. You have {attempts} attempts left")
            entered_password = input("Please enter your password: ")
            if entered_password == password:
                print("Correct password. Here's your database:")
                time.sleep(2)
                display_db()

                break
            attempts -= 1
        if attempts == 0:
            no_password_user = input(
                f"Incorrect password. You have {attempts} attempts left. Would you like to register? (enter [y]es or [q]uit)")
            if no_password_user == "y":
                print("redirecting...")
                time.sleep(2)
                register()
            # giving user the choice to quit the program
            elif no_password_user == "q":
                time.sleep(1)
                print("Good bye ")
                time.sleep(2)
                exit(60)

# if user is returning to the program, give them the option to login


def login(username):

    if username in db:
        ask_for_password(username)

    else:
        while True:
            new_user = input(
                "username not found. Would you like to register? (enter [y]es [n]o or [q]uit)")
            if new_user == "y":
                # call register function
                print("redirecting...")
                time.sleep(2)
                register()

            elif new_user == "n":
                username = input("Enter your username: ")
                if username in db:
                    time.sleep(1)
                    ask_for_password(username)
                    break

            elif new_user == "q":
                exit(30)
            else:
                print("Invalid key. Try again")
                username = input("Enter your username: ")
                if username in db:
                    time.sleep(1)
                    ask_for_password(username)
                    break


def generate_password(option):
    # initialize list that will hold 8 characters created by the program
    password = []
    # variable stopping users from entering invalid values
    min_length = 8
    # initializing variable that will handle the way characters are picked
    character_set = ''

    if option == 1:
        character_set = string.ascii_letters
    elif option == 2:
        character_set = string.ascii_letters + string.digits
    elif option == 3:
        character_set = string.ascii_letters + string.digits + string.punctuation
    else:
        # catching an error should the user enter an invalid value
        raise ValueError("Invalid option. Try again")

    while len(password) < min_length:
        # adding characters to the "password" variable initialized at the top of the function declaration
        password.append(random.choice(character_set))
# join all values stored in the variable "password" to return it as the random password
    return ''.join(password)

# one of the main functions of the program. as the name suggests, it handles the registering of the users


def register():
    while True:
        # user is given the chance to pick an username and the program checks if input is valid and if name is available/not taken
        new_username = input(
            "Choose your username (from 6 to 12 characters long): ").lower().strip()
        keyList = list(db.keys())

        if 6 <= len(new_username) <= 12 and new_username not in keyList:
            # choose user if he wants to choose the password or let the program do it instead
            set_password_option = input(
                "Do you want to set your own password? (Enter [y]es or [n]o): ").strip().lower()

            if set_password_option == 'y':
                # while loop to ensure user enters a valid input
                while True:
                    try:
                        new_password = input(
                            "Enter your password (8 to 12 characters): ")
                        if 8 <= len(new_password) <= 12:
                            break
                        else:
                            print(
                                "Password should be between 8 and 12 characters long. Try again.")
                    except ValueError:
                        print("Invalid input. Try again.")
            else:
                # handling possible errors in case user enters invalid input
                while True:
                    try:
                        option = int(
                            # description of the different password strengths
                            input("\nEnter an option for password strength:\n \n1: Weak (characters only) \n2: Regular (characters and numbers) \n3: Strong (characters, numbers and punctuations)\n"))
                        new_password = generate_password(option)
                        break
                    except ValueError:
                        print("Invalid option. Try again.")

            db[new_username] = new_password

            with open("accounts.txt", "w") as file:
                json.dump(db, file)
            # msg showing user success in registering username and password
            print(
                f"User {new_username} registered with the following password: {new_password}")
# allow user to access their account
            access_account = input(
                "Would you like to access your account now? [y]es or [n]o. ").strip().lower()
            if access_account == 'y':
                login(new_username)
            elif access_account == 'n':
                time.sleep(1)
                print("Goodbye")
                time.sleep(2)
                exit(10)
        else:
            print(
                "Username already in the database or invalid number of characters. Try again")


# handling possible errors when using functions from this file on a different file (as modules..).
if __name__ == "__main__":
    main()
