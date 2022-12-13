# Password Manager - Final Project INST326 Fall '22

## Repository Files
### pass_in.txt
This a text file containing sample input data for the program's password import functionality.  It is used for testing purposes.

### pass_out.txt
This a text file for writing output data via the program's password export functionality. It is used for testing purposes.

### skeleton.py
This file contains the main body of our program. It includes the User class, Password class, and main().

## How to Run the Program
The program can be run from the command line like any other Python program and does not require any command line arguments.
> Windows: `python skeleton.py`
> <br>Mac: `python3 skeleton.py`

## Instructions on Running and Operating the Program
- Enter `python3 skeleton.py` in the command line.<br>
- Enter your name when prompted by the program.<br>
- Enter the number corresponding to your desired action.<br>
  - Command 1 (Check password): 
    - Enter which account or website's password you would like to see when prompted by the program.
    - If you enter a website/account that is not already stored in the database, the program will prompt you until you enter a valid one; **the program will be stuck in a loop if the user selects Command 1 before any passwords are created**.
    - Once a valid account/website is entered, the program will display the account name, password, and security rating.

  - Command 2 (Update password):
    - Enter which account or website you would like to update the password for when prompted by the program.
    - If you enter a website/account that is not already stored in the database, the program will prompt you until you enter a valid one; **the program will be stuck in a loop if the user selects Command 2 before any passwords are created**.
    - Once a valid account/website is entered, the program will ask if you want to randomly generate a new password; enter "Y" or "N" (the program will not move on until you do).
      - If "Y" is entered, the program will ask if you want to change the random generator's seed; enter "Y" or "N" (the program will not move on until you do).
        - If "Y" is entered, the program will prompt you to enter a new seed; if the user's seed is not a valid integer, the program will choose one and move on.
        - If "N" is entered, the program will choose a seed and move on.
      - If "N" is entered, the program will prompt you to enter the new password you want to use.
    - Once the new password has been selected (whether the user inputted it or the computer generated it), the program will display the account name, password, and security rating.

  - Command 3 (Create password): 
    - **Choose this option first (right after entering your name)!** The program may not function properly if there is not at least one password stored. 
    - Enter which account or website you would like to create the password for when prompted by the program; it must end with .org, .com, .edu, or .gov. If it doesn't end with any of those, the program will ask again.
    - Once a valid account/website is entered, the program will ask if you want to randomly generate a new password; enter "Y" or "N" (the program will not move on until you do).
      - If "Y" is entered, the program will ask if you want to change the random generator's seed; enter "Y" or "N" (the program will not move on until you do).
        - If "Y" is entered, the program will prompt you to enter a new seed; if the user's seed is not a valid integer, the program will choose one and move on.
        - If "N" is entered, the program will choose a seed and move on.
      - If "N" is entered, the program will prompt you to enter the new password you want to use.
    - Once the new password has been selected (whether the user inputted it or the computer generated it), the program will display the account name, password, and security rating.

  - Command 4 (Import passwords): 
    - Enter the path a text file you would like to import passwords from when prompted by the program. **Each line of the text file must be formatted as follows: account/website name followed by a tab, followed by the password.** If the text file is not formatted properly, there may be some issues inputting the passwords. The file pass_in.txt contains the example format and may be used for testing the program.
      - If an invalid filepath is entered, the program will let the user know that it was invalid and ask for a new one. The program will not move on until a valid filepath is entered.
    - Once a valid filepath is entered, the program will import those passwords and display them for the user. 
    - The program will prompt the user, asking whether the accounts and corresponding passwords should be displayed in alphabetical order (by name of account/website) or chronological order (by how long each password has been in use). The user must enter "alpha" or "age," respectively; the program will not move on until you do.
    - The program will display the user's name, followed by the account name, password, and security rating for each stored password in the terminal.

  - Command 5 (Export passwords): 
    - Enter the name of a text file you would like to export passwords to when prompted by the program; it must end with "*.txt*". The program will not move on until a valid file name is entered.
    - Once a valid filepath is entered, the program will export all currently stored passwords (along with account and security rating) and prompt the user to check the file whose name was entered.

  - Command 6 (Display all):
    - The program will prompt the user, asking whether the accounts and corresponding passwords should be displayed in alphabetical order (by name of account/website) or chronological order (by how long each password has been in use). The user must enter "alpha" or "age," respectively; the program will not move on until you do.
    - The program will display the user's name, followed by the account name, password, and security rating for each stored password in the terminal.

  - Command 7 (Quit):
    - The program will terminate when this command is entered.

# Authors and Attribution
Kevin:
- main(): demonstrates f-strings and with statements. 
- User.update_password(): demonstrates usage of keyword arguments

Adam:
- User.check_security(): demonstrates usage of regular expressions
- User.import_passwords(): demonstrates sequence unpacking

Wasif:
- User.generate_password(): demonstrates usage optional parameters
- User.__str__(): demonstrates usage of a magic method and sorting with lambda function
edit_password, and age_str functions.
- display_password() *(trivial)*
- Password.age_str() *(trivial)*
- User.__init__() *(trivial)*
- Password.__init__() *(trivial)*
