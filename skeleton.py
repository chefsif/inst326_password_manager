import random
import string

def main():        
    """ Runs the main execution loop for the password manager program. Performs
        different operations and functions of the User and Password classes
        based on user-inputted commands, which are recognized via a 
        pre-designated local list of commands.
        
    Side Effects:
        Prints outputs such as list of commands, requests for user input, 
        and various function output from the User class. 
    """
    # Technique Demonstrated: f-strings
    
    # some example commands: new_account, update_password, check_age, 
    #   check_security, etc.
    pass

class User:
    """ Represents a user with several stored passwords.
    
    Attributes:
        name (string): the user's name
        password_list {account (string) : password (Password)}: a dictionary 
            storing key/value pairs of accounts and passwords, respectively.
    """
    
    def __init__(self, name):
        """ Initializes a User object. 
        
        Args: 
            name (string): the user's name.
            
        Side effects:
            Initializes the value of password_list to an empty dictionary.
        """
        self.name = name
        self.password_list = {}
    
    def update_password(self, website, new_pass):
        """ Updates the password for a certain website the user has a password 
            in. Basically updates the existing K/V pair. If the password and 
            account do not exist, it will make a new K/V pair.

        Args:
            website (str): the website that the user wants to change the 
            password for. It will only take the domain name
            (actual name of website)
        
            new_pass (Password): the new Password object that will update the 
            value
    
        Returns:
            the new value for the key website in the dictionary
        """
        pass    

    def check_security(account):
        """ Calculates a security score for a password.
        
        Args: 
            account (string): the name of the website or account whose password
                security is being checked. 
                
        Returns:
            string: rating out of 5 along with an explanation of how secure the 
            password is (ex: weak, very weak, secure, very secure, etc.)
        """
        # Technique Demonstrated: regular expressions
        pass

    def generate_pass(account):
        """ Generates a random password for a given account.
        
        Args: 
            account (string): the name of the website or account whose password
                security is being generated.
                
        Side effects:
            Modidies values in the attribute password_list.
        """
        new_password = ""
        all_chars = [string.ascii_lowercase, string.ascii_uppercase,
                string.digits, string.punctuation]
        for character in range(30):
            # randomly decide what type of character to choose, then choose
            # which random character of that type to insert in the password
            new_password += random.choice(all_chars[random.randint(0,3)])
        return new_password
    
    def __str__(self):
        """ Returns an informal string representation of a User object.
            Prompts user whether to display accounts sorted by password age or
            alphabetically.
        
        Returns:
            string: informal string representation of a User object displaying
                accounts and corresponding passwords. 
        """
        # Techniques Demonstrated: magic methods / sorting with lambda function
        user_string = ""
        user_string += self.name + "\n"

        # asking user whether to sort by password age or alphabetically by 
        #   account
        option_chosen = False
        while (not option_chosen):
            criteria = input("Please enter the word 'age' if you would like " 
                + "to sort by age or the word 'alpha' if you would like to "
                + "sort alphabetically by account/website name."
            )

            if criteria != "age" and criteria != "alpha":
                print("Please try again.")
            else:
                option_chosen = True
        
        # sorts password_list based on user input
        if(criteria == "alpha"):
            sorted_passwords = sorted(self.password_list, 
                key = lambda account: account
            )
        if(criteria == "age"):
            sorted_passwords = sorted(self.password_list, 
                key = lambda account: self.password_list[account].age
            )
        
        # assembles informal string representation based on sorted list
        for password in sorted_passwords:
            user_string += (f"Account: {password} -" + 
                f"Password: {self.password_list[password]}\n")
            
        return user_string.strip()
    
    def import_passwords(filepath):
        """ Populates the user's password list by reading accounts and 
            passwords from a given file.
            
        Args: 
            filepath (string): the path to a file containing accounts   
                and passwords. 
        
        Side effects:
            Modidies values in the attribute password_list.        
        """
        # Techniques Demonstrated: with statement / reading from file  
        pass


class Password:
    """ Represents a password with a certain age. 
    
    Attributes:
        passcode (string): actual password
        age (int): how long the account has had the password in days
    """  
    def __init__(self, passcode, age=1):
        """ Initializes a Password object.
        
        Args:
            passcode (string): the actual text of the password.
            age (int): how long the password has been in use.
                Defaults to 1 day.
            
        """
        # Technique Demonstrated: optional parameter
        self.passcode = passcode
        self.age = age
    
    def edit_password(self, new_password, age=1):
        """ Changes the value and age of a password.
        
        Args:
            new_password (string): the new text of the password.
            age (int): how long the new password has been in use. 
                Defaults to 1 day.
        """
        self.passcode = new_password
        self.age = age

if __name__ == "__main__":
    main()
