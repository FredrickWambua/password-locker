from user import User
from credential import Credential
import random
import string
import numbers
import getpass
import pyperclip

def create_credential(account_name, key):
    '''
    the function that creates a new credential
    '''
    new_credential = Credential(account_name, key)
    return new_credential

def save_credential(credential):
    '''
    A function that saves a new credential created
    '''
    credential.save_credential()

def display_credentials():
    '''
    A function that displays user credentials
    '''
    return  Credential.display_credentials()

def erase_credential(credential):
    '''
    A function to delete a credential
    '''
    credential.erase_credential()

def check_if_user_exists(password):
    '''
    A function that checks if the user exists for authentification
    '''
    return User.user_exists(password)

def find_account(name, password):
    '''
    A function to find an account by specifying a name
    '''
    return User.find_account(password)

def create_user(name, password):
    '''
    A function that creates a new user
    '''
    new_user = User(name, password)
    return new_user

def save_user(user):
    '''
    A function to save user
    '''
    user.save_user()

def display_users():
    '''
    A function that displays all the users
    '''
    return User.display_users()
