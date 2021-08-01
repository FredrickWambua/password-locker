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
    
