#The purpose of this pseudo-code is to help you understand the logic and the problem solving techniques used in the program.

1. Import necessary libraries and modules
2. Check if pyfiglet is installed
    - If installed, set pyfiglet_installed to True
    - If not installed, set pyfiglet_installed to False
3. Open and load the database file into the "db" dictionary
4. Display a welcome message and menu options
5. Enter the main program loop:
    - Read the user's choice
    - If the choice is "1":
        - Ask the user for their username
        - Call the login(username) function
    - If the choice is "2":
        - Call the register() function
    - If the choice is "q" or "Q":
        - Display "Goodbye"
        - Exit the program
    - If the choice is invalid, display "Not a valid input. Try again"
6. Define the display_db() function:
    - Open the database file
    - Load the database into the "file_display" dictionary
    - For each username and password in "file_display":
        - Display "Username: {username}, Password: {password}"
        - Sleep for 0.5 seconds
    - Sleep for 2 seconds
    - Clear the screen
    - If pyfiglet is installed:
        - Create a Figlet object
        - Render stylized text with "Hasta la vista"
        - Display the stylized text
    - If pyfiglet is not installed, display "Install 'pyfiglet' [pip install pyfiglet] to see stylized text."
    - Sleep for 2 seconds
    - Exit the program
7. Define the clear_screen() function:
    - Check the operating system type
    - If it's 'posix', execute 'clear' to clear the screen
    - If it's not 'posix', execute 'cls' to clear the screen
8. Define the ask_for_password(username) function:
    - Set the number of password entry attempts to 2
    - Retrieve the user's password from the "db" dictionary
    - Read the entered password
    - If the entered password matches the stored password:
        - Display "Correct password. Here's your database:"
        - Call the display_db() function
    - If the entered password is incorrect:
        - Enter a loop with a limited number of attempts:
            - Display "Incorrect password. You have {attempts} attempts left"
            - Read the entered password again
            - If the entered password matches the stored password:
                - Display "Correct password. Here's your database:"
                - Call the display_db() function
                - Exit the loop
            - Decrement the remaining attempts
        - If no correct password is entered after all attempts:
            - Read the user's choice (register or quit)
            - If the choice is "y", call the register() function
            - If the choice is "q", exit the program
9. Define the login(username) function:
    - If the provided username is in the "db" dictionary:
        - Call the ask_for_password(username) function
    - If the provided username is not in the "db" dictionary:
        - Enter a loop to handle new users:
            - Read the user's choice (register, quit, or try again)
            - If the choice is "y", call the register() function
            - If the choice is "n" and the username is now in the "db" dictionary:
                - Call the ask_for_password(username) function
                - Exit the loop
            - If the choice is "q", exit the program
            - If the choice is invalid, display "Invalid key. Try again" and repeat
10. Define the generate_password(option) function:
    - Initialize an empty list named "password"
    - Set the minimum password length to 8
    - Initialize an empty string named "character_set"
    - Depending on the selected option:
        - If option is 1, set "character_set" to letters only
        - If option is 2, set "character_set" to letters and numbers
        - If option is 3, set "character_set" to letters, numbers, and punctuation
        - If the option is invalid, raise a ValueError with the message "Invalid option. Try again"
    - Enter a loop to generate a password:
        - Append a random character from "character_set" to the "password" list
        - Repeat until the password length reaches the minimum length
    - Return the joined "password" as a string
11. Define the register() function:
    - Enter a loop to handle user registration:
        - Read the desired new username
        - Get a list of existing usernames
        - Check if the new username meets length criteria and is not already taken
        - If valid:
            - Read the user's choice (set password or generate one)
            - If the choice is to set a password:
                - Enter a loop to get a valid password
                - If the password meets length criteria, break the loop
            - If the choice is to generate a password:
                - Enter a loop to get a valid password strength option
                - Generate a new password based on the selected option
            - Add the new username and password to the "db" dictionary
            - Write the updated database to the file
            - Display the registration success message
            - Read the user's choice (access account or quit)
            - If the choice is to access the account, call the login(new_username) function
            - If the choice is to quit, exit the program
        - If the new username is invalid or already taken, display an error message and repeat the loop
12. Start the main program loop if this script is executed directly
