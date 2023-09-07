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
            time.sleep(1)
            print("Good bye")
            time.sleep(2)
            exit(10)
        else:
            print("Not a valid input. Try again")

# as per our assessment spec, loading database on the screen for 2 seconds if user and password match and are valid/in the database


def display_db():
    db_file = open("accounts.txt", "r")
    # accessing json library so we can use the load function to store the database in a variable called file_display which then can be iterated over in the following line
    file_display = json.load(db_file)
    for username, password in file_display.items():
        print(f"Username: {username}, Password: {password}")
        time.sleep(0.5)
    time.sleep(2)
    clear_screen()

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


def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')


def ask_for_password(username):
    attempts = 2
    password = db[username]
    entered_password = input("Please enter your password: ")
    if entered_password == password:
        time.sleep(2)
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
                # time.sleep(2 or 3) then:
                # call register function

            elif no_password_user == "q":
                time.sleep(1)
                print("Good bye ")
                time.sleep(2)
                exit(60)


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
                register()

            elif new_user == "n":
                username = input("Enter your username: ")
                if username in db:
                    ask_for_password(username)
                    break

            elif new_user == "q":
                exit(30)
            else:
                print("Invalid key. Try again")
                username = input("Enter your username: ")
                if username in db:
                    ask_for_password(username)
                    break


def generate_password(option):
    password = []
    min_length = 8

    character_set = ''

    if option == 1:
        character_set = string.ascii_letters
    elif option == 2:
        character_set = string.ascii_letters + string.digits
    elif option == 3:
        character_set = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid option. Try again")

    while len(password) < min_length:
        password.append(random.choice(character_set))

    return ''.join(password)


def register():
    while True:
        new_username = input(
            "Choose your username (from 6 to 12 characters long): ").lower().strip()
        keyList = list(db.keys())

        if 6 <= len(new_username) <= 12 and new_username not in keyList:
            set_password_option = input(
                "Do you want to set your own password? (Enter [y]es or [n]o): ").strip().lower()

            if set_password_option == 'y':
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
                while True:
                    try:
                        option = int(
                            input("\nEnter an option for password strength:\n \n1: Weak (characters only) \n2: Regular (characters and numbers) \n3: Strong (characters, numbers and punctuations)\n"))
                        new_password = generate_password(option)
                        break
                    except ValueError:
                        print("Invalid option. Try again.")

            db[new_username] = new_password

            with open("accounts.txt", "w") as file:
                json.dump(db, file)

            print(
                f"User {new_username} registered with the following password: {new_password}")

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


if __name__ == "__main__":
    main()
