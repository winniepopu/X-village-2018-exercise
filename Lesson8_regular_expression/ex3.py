import re

class AuthSystem:
    def __init__(self):
        """Define regex"""

        
        pattern1=r'(?P<username>[A-Z]{1}\w{5,11})' 
        pattern2=r'(?P<password>[a-z0-9]{6,})'
        self.username_regex = re.compile(pattern1)
        self.password_regex = re.compile(pattern2)
    
    def _check_username(self, username):
        """Check username is valid or not"""
        if self.username_regex.search(username) is not None:
            print("Correct username")
            return True
        else: 
            print("Username format error! Your username is "+username+"")
            return False

    def _check_password(self, password):
        """Check password is valid or not"""
        if self.password_regex.search(password) is not None:
            if len(password) >12 or len(password)<6 :
                print("Password length error! Your password length is ",len(password))
                return False
            return True

        else:
            print( "Password format error! Your password is "+password+"")
            return False
        
    def authenticate(self, username, password):
        """authenticate the user"""
        if not self._check_username(username):
            return        
        if not self._check_password(password):
            return
        print("Welcome, "+username+" ")

    
# Construct a object of type AuthSystem
username= input('username:')
password= input('password:')
auth = AuthSystem()
auth.authenticate(username, password)
