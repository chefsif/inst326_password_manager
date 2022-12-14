import random
import string
import re

def display_password(user, account_name): # Wasif
    """ Displays account name, password, and password age for a single 
            password.
    """
    return (f"The password for {account_name} is: "
                + f"{user.password_list[account_name].passcode}"
                + f" (in use for {user.password_list[account_name].age_str()})"
                + f" - {user.check_security(account_name)}"
            )

def main(): # Kevin
    """ Runs the main execution loop for the password manager program. Performs
        different operations and functions of the User and Password classes
        based on user-inputted commands, which are recognized via a 
        pre-designated local list of commands.
        
    Side Effects:
        Prints outputs such as list of commands, requests for user input, 
        and various function output from the User class. 
    """
    # Technique Demonstrated: f-strings and with statement(s)
    exit_check = 0
    user_name = input("Welcome to the Password Manager! What is your name?\n")
    user = User(user_name)
    
    while exit_check == 0:
        print("# -----------------------------------------------------")
        check = 0
        print(f"What would you like to do, {user_name}?")
        user_choice = int(input(
            "1: Check password\t2: Update password\t3: Create password"
              + "\t4: Import passwords\t5: Export passwords\t6: Display all"
              + " passwords\t7: Quit\n"
        ))
        # ---------------------------------------------------------------------
        if user_choice == 1:
            while check == 0:
                account_name = input(
                    "Which account's password would you like to check?\n")
                if account_name not in user.password_list.keys():
                    print("Account name is not valid, please try again.")
                else:
                    check = 1
            print(display_password(user, account_name))
        # ---------------------------------------------------------------------
        elif user_choice == 2:
            while check == 0:
                account_name = input(
                    "Which account's password would you like to update?\n")
                if account_name not in user.password_list.keys():
                    print("Account name is not valid, please try again.")
                else:
                    check = 1
            user.update_password(account_name)
            print(display_password(user, account_name))
        # ---------------------------------------------------------------------    
        elif user_choice == 3:
            while check == 0:
                account_name = input(
                    "Which account's password would you like to create?\n"
                )
                if account_name.endswith(".com") \
                or account_name.endswith(".org") \
                or account_name.endswith(".edu") \
                or account_name.endswith(".gov"):
                    check = 1
                else:
                    print("Website name did not include top level domain."
                        + " Domains currently supported are .com, .org, .edu, "
                        + "and .gov")
            user.update_password(account_name)
            print(display_password(user, account_name))
        # ---------------------------------------------------------------------
        elif user_choice == 4:
            while check == 0:
                try:
                    import_file = input("Please input the name of the import "
                                + "file including .txt at the end: ")
                    user.import_passwords(import_file)
                    check = 1
                except FileNotFoundError:
                    print("File not found")
            print("Your new passwords have been imported successfully!"
                + "\nHere is an updated display of all your accounts and"
                + " passwords:"            
            )
            print(user)
        # ---------------------------------------------------------------------
        elif user_choice == 5:
            
            while check == 0:
                export_file = input("Please name the export file, "
                                + "including .txt at the end: ")
                if ".txt" in export_file:
                    with open(export_file, 'w') as data:
                        data.write(str(user))
                    check = 1
                else:
                    print("Invalid name, remember to include .txt")
            print(
                "Your new passwords have been exported successfully!" + 
                f" Check them out in {export_file}."
            )
        # ---------------------------------------------------------------------
        elif user_choice == 6:
            print(user)
            pass
        # ---------------------------------------------------------------------
        elif user_choice == 7:
            exit_check = 1
            print("Have a nice day!")
        else:
            print("Please enter a valid command!")

class User:
    """ Represents a user with several stored passwords.
    
    Attributes:
        name (string): the user's name
        password_list {account (string) : password (password) }: a dictionary 
            storing key/value pairs of accounts and passwords, respectively.
    """
    
    def __init__(self, name): # Wasif
        """ Initializes a User object. 
        
        Args: 
            name (string): the user's name.
            
        Side effects:
            Initializes the value of password_list to an empty dictionary.
        """
        self.name = name
        self.password_list = {}
    
    def update_password(self, account): # Kevin
        """ Updates the password for a certain account the user has a password 
            in. Basically updates the existing K/V pair. If the password and 
            account do not exist, it will make a new K/V pair.

        Args:
            account (string): the account that the user wants to change the 
                password for.
    
        Returns:
            the new value for the key website in the dictionary
        """
        # Technique Demonstrated: keyword argument
        option_chosen = False
        while option_chosen == False:
            y_or_n = input("Would you like to randomly generate the"
                                        + " password? Y/N?\n")
            
            if y_or_n == "Y" or y_or_n == "y":
                seed_chosen = False
                while seed_chosen == False:    
                    set_seed = input("Would you like to change the random"
                                    + " password generator's seed? Y/N?\n")
                    
                    if set_seed == "Y" or set_seed == "y":
                        user_seed = input("Please enter your new RNG seed: ")
                        user_pass = (
                            self.generate_password(account,seed=user_seed)
                        )
                        seed_chosen = 1
                    
                    elif set_seed == "N" or set_seed == "n":
                        user_pass = self.generate_password(account)
                        seed_chosen = 1
                    
                    else:
                        print("Please choose Y or N.")
                option_chosen = True
                        
            elif y_or_n == "N" or y_or_n == "n":
                user_pass = input(f"What would you like the new password to be"
                        + f" for {account}?\n")
                self.password_list[account] = Password(user_pass)
                option_chosen = True

            else:
                print("Please choose Y or N.")
                
        return user_pass
                
    def check_security(self, account): # Adam 
        """ Calculates a security score for a password.
        
        Args: 
            account (string): the name of the website or account whose password
                security is being checked. 
                
        Returns:
            string: rating out of 5 along with an explanation of how secure the 
            password is (ex: weak, very weak, secure, very secure, etc.)
        """
        # Technique Demonstrated: regular expressions
        strength_rating = 0
        strength_eval = ""
        has_num = re.search(r"[0-9]", self.password_list[account].passcode)
        has_special = re.search(r"\W", self.password_list[account].passcode)
        has_underscore = re.search(r"_", self.password_list[account].passcode)
        has_letter = re.search(r"[a-zA-Z]", 
                                self.password_list[account].passcode)
        has_password = re.search(r"password", 
                                 self.password_list[account].passcode)
        
        if has_num != None:
            strength_rating += 1
        if has_special != None or has_underscore != None:
            strength_rating += 1
        if has_letter != None:
            strength_rating += 1
        if len(self.password_list[account].passcode) > 6:
            strength_rating += 2
        if has_password != None:
            strength_rating = 2
        
        if strength_rating == 1:
            strength_eval = "Very Weak"
        elif strength_rating == 2:
            strength_eval = "Weak"
        elif strength_rating == 3:
            strength_eval = "Average"
        elif strength_rating == 4:
            strength_eval = "Good"
        elif strength_rating == 5:
            strength_eval = "Strong"   

        return f"strength rating: {strength_rating} ({strength_eval})"

    def generate_password(self, account, seed=None): # Wasif
        """ Generates a random password for a given account.
        
        Args: 
            account (string): the name of the website or account whose password
                security is being generated.
            seed (int): an optional seed for the random number generator. 
                Defaults to None.
                
        Side effects:
            Modidies values in the attribute password_list.
        """
        # Technique Demonstrated: optional parameter
        new_password = ""
        
        # sets random number generator's seed to user input, if given
        try:
            random.seed(int(seed))
        except:
            if(seed != None):
                print("The seed you entered was not valid. " + 
                    "The application will choose one for you.")
            
        all_chars = [string.ascii_lowercase, string.ascii_uppercase,
                string.digits, string.punctuation]
        for character in range(30):
            # randomly decide what type of character to choose, then choose
            # which random character of that type to insert in the password
            new_password += random.choice(all_chars[random.randint(0,3)])
        self.password_list[account] = Password(new_password)
        return new_password
    
    def __str__(self): # Wasif
        """ Returns an informal string representation of a User object.
            Prompts user whether to display accounts sorted by password age or
            alphabetically.
        
        Returns:
            string: informal string representation of a User object displaying
                accounts and corresponding passwords. 
        """
        # Techniques Demonstrated: magic methods, sorting with lambda function,
        #   conditional expression
        user_string = "Here is all of your information:\n\n"
        user_string += f"\nUSER NAME: {self.name}\n"

        # asking user whether to sort by password age or alphabetically by 
        #   account
        option_chosen = False
        while (not option_chosen):
            criteria = input("*Please enter the word 'age' if you would like " 
                + "to sort by age or the word 'alpha' if you would like to "
                + "sort alphabetically by account/website name*: "
            )

            if criteria != "age" and criteria != "alpha":
                print("Please try again.")
            else:
                option_chosen = True

        # sorts password_list based on user input
        sorted_passwords = (
            sorted(self.password_list, 
                key = lambda account: self.password_list[account].age)
            if criteria == "age" 
            else sorted(self.password_list, key = lambda account: account)
        )

        # assembles informal string representation based on sorted list
        for account in sorted_passwords:
            user_string += (f"> Account: {account} || " + 
                f"Password: {self.password_list[account].passcode} " + 
                f"(in use for {self.password_list[account].age_str()})" + 
                f" - {self.check_security(account)}\n"
                )

        return user_string
    
    def import_passwords(self, filepath): # Adam
        """ Populates the user's password list by reading accounts and 
            passwords from a given file.
            
        Args: 
            filepath (string): the path to a file containing accounts   
                and passwords. 
        
        Side effects:
            Modidies values in the attribute password_list.        
        """
        # Techniques Demonstrated: sequence unpacking
        with open(filepath, "r") as f:
            for line in f:
                new_account, new_password = line.split("\t")
                self.password_list[new_account] = Password(new_password.strip())

class Password:
    """ Represents a password with a certain age. 
    
    Attributes:
        passcode (string): actual password
        age (int): how long the account has had the password in hours
    """  
    def __init__(self, passcode, age=1): # Wasif
        """ Initializes a Password object.
        
        Args:
            passcode (string): the actual text of the password.
            age (int): how long the password has been in use. 
                Defaults to 1 day.
            
        """
        self.passcode = passcode
        self.age = age
    
    def age_str(self): # Wasif
        """ Provides how long the password has been in use.
        
        Returns:
            string: a representation of the password's age in days.
        """
        if self.age == 1:
            return "1 day"
        elif self.age == 0:
            return "less than a day"
        else: 
            return f"{self.age} days"

if __name__ == "__main__":
    main()
