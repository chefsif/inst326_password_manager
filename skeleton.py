# main() - Kevin
#   > if statements, print statements, and getting user input to figure out
#       what the user wants to do
#   > f-strings to display accounts and passwords
# 
# 
# User class:
#   Attributes:
#   > name (string): the user's name
#   > password_list {account : Password obj}: a record of all the user's 
#       passwords
#
#   Methods:
#   > __init__(self, name) 
#       > initialize password_list to an empty dictionary
#   > update_password(account, new_pass) - Kevin
#       > if password and account don't exist, make a new one
#       > update existing K/V pair
#       > ask user if they want to sort alphabetically by account/website name
#           or if they want to sort by oldest to youngest password age   
#           > sort with lambda       
#   > check_age(account)
#   > check_security(account) - Adam
#       > regular expressions
#   > generate_pass(account)
#   > __str__() - Wasif
#   > import_passwords(filepath) - Adam
#       > with statement / reading from file inputted by the user  
#
# Password class:
#   Attributes:    
#   > passcode (string): actual password
#   > age (datetime): how long the account has had the password
#   
#   Methods:
#   > __init__(self, passcode, age=0) - Wasif
#   > edit_password(self, new_pass)