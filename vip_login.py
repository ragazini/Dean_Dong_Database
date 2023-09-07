import json
import subprocess
import sys
import time
import os


def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')


def check_credentials(username, password):
    with open("accounts.txt", "rt") as file:
        db = json.load(file)
        if username in db and db[username] == password:
            return True
    return False


if len(sys.argv) == 3:
    provided_username = sys.argv[1]
    provided_password = sys.argv[2]

    if check_credentials(provided_username, provided_password):
        # If credentials are valid, display the database
        print("Valid username and password. Displaying the database:")
        with open("accounts.txt", "rt") as file:
            db = json.load(file)
            for username, password in db.items():
                print(f"Username: {username}, Password: {password}")
            time.sleep(2)
            clear_screen()
    else:
        print("Invalid username or password. Running login.py...")
        subprocess.run(["python", "login.py"])
else:
    print("Usage: python script.py <username> <password>")
