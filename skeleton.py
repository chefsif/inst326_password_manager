import sys
import re
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
    input = ""
    input1 = 0
    input2 = ""
    input3 = 0
    input4 = ""
    input5 = ""
    input6 = ""
    exit_check = 0
    check1 = 0
    check2 = 0
    check3 = 0
    check4 = 0
    check5 = 0
    
    print("Welcome to the password manager, what is your name?")
    input = input()
    list_p = User(input)
    print(f"What would you like to do, {input}?")
    while exit_check = 0:
        print("1: Check password    2: Update password    3: Create password \
              4: Import password    5: Export password    6: Quit")
        input1 = int(input())
        if input1 == 1:
            while check1 == 0:
                print("Which website's password would you like to check?")
                input2 = input()
                if input2 not in list_p.password_list.keys():
                    print("Website is not valid, please try again.")
                else:
                    check1 = 1
            print(f"The password for {input2} is \
                  {list_p.password_list[input2]}")
            print(f"The strength of the password is {list_p.check_security}")
            
        if input1 == 2:
            while check2 == 0:
                print("Which website's password would you like to update?")
                input2 = input()
                if input2 not in list_p.password_list.keys():
                    print("Website is not valid, please try again.")
                else:
                    check2 = 1
            print(f"What would you like the new password to be for {input2}?")
            input3 = input()
            print(f"The password for {input2} has been updated to {input3}")
            list_p.update_password(input2, input3)
            
        if input1 == 3:
            
            print("Which website's password would you like to create?")
            input2 = input()
            while check3 == 0:
                print("Would you like to randomly generate the password? Y/N?")
                input4 = input()
                if input4 == "Y":
                    list_p.generate_password(input2)
                    check3 = 1
                elif input4 == "N":
                    print(f"What would you like the password to be \
                          for {input2}?")
                    input3 = input()
                    print(f"The password for {input2} has been created to \
                          be {input3}")
                    list_p.update_password(input2, input3)
                    check3 = 1
                else:
                    print("Website is not valid, please try again")
        if input1 == 4:
            print("Please input the name of the import file")
            input5 = input()
            list_p.import_passwords(input5)
        if input1 == 5:
            print("Please name the export file, including .txt at the end")
            input6 = input()
            with open(input6, 'w') as data:
                data.write(str(list_p))
        if input1 == 6:
            sys.exit("Have a nice day!")
class User:
    """ Represents a user with several stored passwords.
    
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
    
    def update_password(self, website, new_pass): #Kevin
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
        self.password_list[website] = new_pass
        return new_pass
    
    
    def check_security(account): #Adam 
        """ Calculates a security score for a password.
        
        Args: 
            account (string): the name of the website or account whose password
                security is being checked. 
                
        Returns:
            string: rating out of 5 along with an explanation of how secure the 
            password is (ex: weak, very weak, secure, very secure, etc.)
        """
        # Technique Demonstrated: regular expressions
        strengthEval = 0
        num = re.search("[0-9]+")  # or "\d"
        spChar = r""
        
        letter = r"[a-zA-Z]+"
        pwLength = len(account)
        
        if num in account:
            strengthEval + 1
        if spChar in account:
            strengthEval + 1
        if letter in account:
            strengthEval + 1
        if pwLength > 6:
            strengthEval + 2
            
        return strengthEval 
            

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
    
    def import_passwords(self, filepath): #Adam
        """ Populates the user's password list by reading accounts and 
            passwords from a given file.
            
        Args: 
            filepath (string): the path to a file containing accounts   
                and passwords. 
        
        Side effects:
            Modidies values in the attribute password_list.        
        """
        
        with open(filepath, "r") as f:
            for line in f:
                account, password = line.split("\t")
                self.password_list[account] = password
                
        # Techniques Demonstrated: with statement / reading from file  


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
