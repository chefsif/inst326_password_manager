def main():
    
    """ It will print command line arguments to give the user information
        on what they need to input into the command line and what they
        can do. Essentially the text based interface the user will interact 
        with. It will control what the user can and cannot do.  
        
    Side Effects:
        prints: Options that the user can select and what they need to input
    """
    return 0
class User:
    """ Creates a abstraction of an user
    
    Attributes:
        name (string): the user's name
        password_list {account : Password obj}: a record of all the user's
        passwords
    """
#   Methods:
#   > __init__(self, name) 
#       > initialize password_list to an empty dictionary
    def update_password(self, website, new_pass):
        """ Updates the password for a certain website the user has a password 
            in. Basically updates the existing K/V pair. If the password and 
            account do not exist, it will make a K/V pair.

        Args:
            website (str): the website that the user wants to change the 
            password for. It will only take the domain name
            (actual name of website)
        
            new_pass (Password): the new Password object that will update the 
            value
    
        Returns:
            the new value for the key website in the dictionary
        """     
#   > check_age(account)
#   > check_security(account) - Adam
#       > regular expressions
#   > generate_pass(account)
#   > display() - Wasif
#       > ask user if they want to sort alphabetically by account/website name
#           or if they want to sort by oldest to youngest password age   
#           > sort with lambda
#   > import_passwords(filepath) - Adam
#       > with statement / reading from file inputted by the user  
#
class Password:
    """ Abstraction of an password
    
    Attributes:
        passcode (string): actual password
        age (datetime): how long the account has had the password
    """  
#   Methods:
#   > __init__(self, passcode, age=0) - Wasif
#   > edit_password(self, new_pass)
if __name__ == "__main__":
    main()