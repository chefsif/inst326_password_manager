# Password Manager - Final Project INST326 Fall '22

## Repository Files
### pass_in.txt
This a text file containing sample input data for the program's password import functionality.

### pass_out.txt
This a text file containing sample output data for the program's password export functionality.

### skeleton.py
This file contains the main body of our program. It includes the User class, Password class, and main().

## How to Run the Program
The program can be run from the command line like any other Python program and does not require any command line arguments.
> <br>Windows: `python skeleton.py`
> <br>Mac: `python3 skeleton.py`

> Clear instructions on how to run your program from the command line

# Instructions
Type python3 skeleton.py in the command line.
Type in your name.
Select your desired action and press enter.
Follow the directions as prompted by the command you selected. 
Command 1 ask for a website to print the password for and will ask again if 
website is not used yet or typed incorrectly. 
Command 2 will ask for a website to update the password for and will ask again 
if website has not been used yet. It will then display the password to confirm 
it. 
Command 3 will ask for a website to create a password for and it must end 
with .org, .com, .edu, or .gov. If it doesn't end with any of those then it 
will ask again and if it is correct then it will print the password and 
associated website.
Command 4 is for importing passwords from a .txt file. It must be a .txt file
and be within the folder that contains skeleton.py.
Command 5 will export the passwords to a new .txt file. It will ask for a name
for the new file and it must end with .txt. The newly created file will be
in the same folder as skeleton.py
Command 6 will print all the websites and their associated passwords.
Command 7 is used to quit the program in the terminal.


> Clear instructions on how to use your program and/or interpret the output of the program, as applicable
> Attribution: in order to evaluate whether each member has made a substantial, original contribution to the project, please clearly and unambiguously indicate who is the primary author of each major function/method. You do not need to attribute minor program components, such as an if __name__ == "__main__": statement. Along with each function, please indicate which elements from guideline 6.D. each group member is claiming credit for.

# Authors
Kevin authored the main which demonstrated f strings and with statements. 
Kevin's update_password function demonstrated keyword arguments

Adam authored the check_security which demonstrated regular expressions and conditional expressions. 
Adam's import_passwords function demonstrates sequence unpacking.

Wasif authored the generate_password which demonstrates optional parameters, __init__ , 
__str__ demonstrates magic methods and sorting with lambda function
edit_password, and age_str functions. 

> An annotated bibliography of all sources you used to develop your project. For each source, explain how you used the source.
