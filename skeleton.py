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
    """ Represents a user with several stored paasswords.
    
    Attributes:
        name (string): the user's name
        password_list {account (string) : password (password) }: a dictionary 
            storing key/value pairs of accounts and passwords, respectively.
    """
    
    def __init__(self, name):
        """ Initializes a User object.
        
        Args: 
            name (string): the user's name.
            
        Side effects:
            Initializes the value of password_list to an empty dictionary.
        """
        pass
    
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
        pass
    
    def __str__():
        """ Returns an informal string representation of a User object.
            Prompts user whether to display accounts sorted by password age or
            alphabetically.
        
        Returns:
            string: informal string representation of a User object displaying
                accounts and corresponding passwords. 
        """
        # Techniques Demonstrated: magic methods / sorting with lambda function
        pass
    
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
        age (int): how long the account has had the password in hours
    """  
    def __init__(self, passcode, age=0):
        """ Initializes a Password object.
        
        Args:
            passcode (string): the actual text of the password.
            age (int): how long the password has been in use. 
                Defaults to 0 hours.
            
        """
        # Technique Demonstrated: optional parameter
        pass
    
    def edit_password(self, new_password, age=0):
        """ Changes the value and age of a password.
        
        Args:
            new_password (string): the new text of the password.
            age (int): how long the new password has been in use. 
                Defaults to 0 hours.
        """
        pass

if __name__ == "__main__":
    main()
